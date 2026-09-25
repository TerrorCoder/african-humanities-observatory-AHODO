# African Humanities Open Data Observatory (AHODO)

## Open Dataset & Specification

## Dataset release

- **Current public release:** AHODO Discovery Dataset v0.3 (11,650 records)
- **Dataset / DOI:** [10.5281/zenodo.22944185](https://doi.org/10.5281/zenodo.22944185)
- **Interactive search:** [AHODO Search](https://ahodo.kairosgroup.co.zw/)
- **Source repository:** [AHODO public GitHub repository](https://github.com/TerrorCoder/african-humanities-observatory-AHODO)

The archived Zenodo release is the citable v0.3 snapshot. AHODO Search provides interactive discovery over the public dataset. The DOI does not change the rights of represented resources.

AHODO is a provenance- and rights-aware discovery dataset for African humanities and humanities-adjacent resources. This repository contains the public **AHODO Discovery Dataset v0.3**, its public data specification, source attribution, rights/provenance documentation and release materials.

The public dataset is a discovery registry, **not a corpus of the underlying works and not a representative sample** of African humanities.

The audited v0.3 release contains **11,650** records: **10,398** core humanities, **1,127** humanities adjacent and **125** broader social science. Download the [complete JSONL](dataset/v0.3/ahodo-discovery-v0.3-complete.jsonl) or [CSV](dataset/v0.3/ahodo-discovery-v0.3-complete.csv); the [core-humanities](dataset/v0.3/ahodo-discovery-v0.3-core-humanities.jsonl) and [humanities-plus-adjacent](dataset/v0.3/ahodo-discovery-v0.3-humanities-plus-adjacent.jsonl) subsets are also available. JSONL retains nested rights information; CSV is a compact index.

Start with the [dataset card](docs/DATASET_CARD.md), [data dictionary](docs/DATA_DICTIONARY.md), [source manifest](docs/SOURCE_MANIFEST.md), [rights and provenance guide](docs/RIGHTS_AND_PROVENANCE.md), [methodology](docs/METHODOLOGY.md), and [known limitations](docs/KNOWN_LIMITATIONS.md). The [public item schema](schema/item-record.schema.json) describes the JSONL format. [Licensing](docs/LICENSING.md) explains the layered repository notice and source-specific rights.

AHODO uses layered rights. AHODO-authored public materials are available for personal, educational and non-commercial research use under the [repository licensing notice](LICENSE); commercial reuse of AHODO-authored material requires permission unless separately licensed. Source-derived metadata and underlying resources retain their own rights and licences.

**10,738** records reference metadata whose licence is not established. Community-governance status `not_provided` is not permission or consent. No blanket AI-training clearance is asserted. Holding country, subject geography and language are recorded separately.

Run `python validate_release.py` from this directory to verify checksums, JSONL/CSV alignment, counts, uniqueness and subset membership. The [projection-integrity manifest](dataset/v0.3/projection-integrity.json) records how these public files relate to the audited release. The curated JSONL/CSV differ byte-for-byte because private acquisition details were removed; substantive audited discovery and rights values were preserved. `dataset-statistics.json` is a byte-identical copy of the audited release. `CITATION.cff` now includes the published dataset DOI.

Recommended citation: AHODO contributors. (2026). *AHODO Discovery Dataset v0.3: African Humanities Resource Discovery and Rights Metadata* [Dataset]. Version 0.3. https://doi.org/10.5281/zenodo.22944185. Cite the relevant source institution and resource separately. Citation metadata is available in [CITATION.cff](CITATION.cff).
