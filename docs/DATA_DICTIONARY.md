# Data dictionary

JSONL is the canonical structured export. Empty arrays mean the source did not establish a value; null has the field-specific meaning below. CSV is a flattened index and omits nested rights, attribution and community-governance detail. Use JSONL and the source manifest for reuse decisions.

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable AHODO item ID |
| `parent_collection_id` | string | Released parent collection ID |
| `source_id` | string | Source family in the public source manifest |
| `authoritative_id` | string | Institution-supplied item identifier |
| `canonical_url` | URL or null | Evidenced item URL; null means no item URL established |
| `canonical_url_status` | established / not_established | Explicit URL assessment |
| `title` | string | Normalized display title |
| `material_types` | array of strings | Source-grounded material types |
| `contributors` | array | Source-grounded display names and roles; no nationality inference |
| `dates` | array | Labeled dates from source metadata |
| `languages` | array of ISO 639-3 codes | Source-stated languages; empty means unstated |
| `subject_geography` | object | Status, countries and evidence IDs; independent of holder and language |
| `holding_institution` | object | Holder name, homepage and country |
| `rights_reference` | object | Collection/resource IDs resolving in source manifest |
| `scope_classification` | enum | core_humanities, humanities_adjacent or broader_social_science |
| `rights_assessment` | object | Resource-specific licence, copyright, attribution, computational reuse, other-rights and review findings |
| `community_governance` | object | Stated governance status, notices and labels; not_provided is not permission |
| `public_provenance` | object | Source ID, acquisition category and retrieval time |
| `licensed_catalogue_text` | object, optional | African Minds licensed catalogue synopsis and source-verbatim credits |
