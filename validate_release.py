"""Validate the public AHODO v0.3 files without internal pipeline dependencies."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "dataset/v0.3"
PREFIX = "ahodo-discovery-v0.3-"
SETS = ("complete", "core-humanities", "humanities-plus-adjacent")
REQUIRED = {"id", "parent_collection_id", "source_id", "authoritative_id", "canonical_url",
            "canonical_url_status", "title", "material_types", "contributors", "dates",
            "languages", "subject_geography", "holding_institution", "rights_reference",
            "scope_classification", "rights_assessment", "community_governance", "public_provenance"}

def read(path):
    return json.loads(path.read_text(encoding="utf8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    with path.open("r", encoding="utf8", newline="") as stream:
        for line in stream:
            if line.strip():
                yield json.loads(line)


def contains_private_path(value):
    if isinstance(value, str):
        return bool(re.match(r"^[A-Za-z]:[\\/]", value) or value.startswith(("/Users/", "/home/")))
    if isinstance(value, list):
        return any(contains_private_path(v) for v in value)
    if isinstance(value, dict):
        return any(contains_private_path(v) for v in value.values())
    return False


def main():
    assert DATA.is_dir(), DATA
    checks = read(DATA / "checksums.json")["files"]
    assert set(checks) == {p.name for p in DATA.iterdir() if p.is_file() and p.name != "checksums.json"}
    for name, expected in checks.items():
        assert digest(DATA / name) == expected, name
    stats = read(DATA / "dataset-statistics.json")
    projection = read(DATA / "projection-integrity.json")
    families = read(DATA / "source-manifest.json")["families"]
    sources = {f["source_id"]: f for f in families}
    rights_pairs = {(c["collection_id"], c["resource_id"]) for f in families for c in f["resource_rights"]}
    seen_sets = {}
    source_counts = Counter()
    scope_counts = Counter()
    rights_counts = Counter()
    for subset in SETS:
        path = DATA / f"{PREFIX}{subset}.jsonl"
        assert digest(path) == projection["subsets"][subset]["public_jsonl_sha256"]
        ids = []
        with (DATA / f"{PREFIX}{subset}.csv").open(encoding="utf-8-sig", newline="") as stream:
            csv_ids = [row["id"] for row in csv.DictReader(stream)]
        for record in rows(path):
            assert REQUIRED <= record.keys() <= REQUIRED | {"licensed_catalogue_text"}
            assert record["canonical_url"] is not None or record["canonical_url_status"] == "not_established"
            assert record["source_id"] in sources
            assert record["public_provenance"]["source_id"] == record["source_id"]
            assert record["public_provenance"]["acquisition_method"] == sources[record["source_id"]]["acquisition_method"]
            ref = record["rights_reference"]
            assert ref["parent_collection_id"] == record["parent_collection_id"]
            assert (ref["parent_collection_id"], ref["resource_id"]) in rights_pairs
            assert ref["resource_id"] == record["rights_assessment"]["resource_id"]
            assert not contains_private_path(record)
            ids.append(record["id"])
            if subset == "complete":
                source_counts[record["source_id"]] += 1
                scope_counts[record["scope_classification"]] += 1
                rights_counts[record["rights_assessment"]["licence_status"]] += 1
        assert ids == sorted(ids) and len(ids) == len(set(ids))
        assert ids == csv_ids
        assert len(ids) == projection["subsets"][subset]["records"]
        seen_sets[subset] = set(ids)
    assert len(seen_sets["complete"]) == stats["record_count"]
    assert len(seen_sets["core-humanities"]) == stats["core_humanities"]
    assert seen_sets["core-humanities"] <= seen_sets["humanities-plus-adjacent"] <= seen_sets["complete"]
    assert source_counts == stats["source_families"]
    assert scope_counts == stats["scope"]
    assert rights_counts == stats["rights_status"]
    assert {f["source_id"]: f["released_item_count"] for f in families} == dict(source_counts)
    assert (ROOT / "LICENSE").exists() and (ROOT / "CITATION.cff").exists()
    assert (ROOT / "schema/item-record.schema.json").exists()
    print(json.dumps({"status": "PASS", "records": len(seen_sets["complete"]),
                      "core_humanities": len(seen_sets["core-humanities"]),
                      "files_hashed": len(checks), "source_families": len(sources)}))


if __name__ == "__main__":
    main()
