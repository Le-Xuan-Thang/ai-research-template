# REFERENCE INTEGRITY AND BIBTEX SKILL

## 1. Purpose

Whenever scientific literature is searched, cited, added, edited, or used to support manuscript content, maintain a verified and standardized BibTeX bibliography.

The bibliography must satisfy four requirements simultaneously:

**Existence → Relevance → Metadata accuracy → Formatting consistency**

A reference is not considered valid merely because a plausible BibTeX entry can be generated.

Every externally introduced reference must correspond to a real and independently verified publication or dataset.

---

# 2. Absolute Non-Fabrication Rule

Never fabricate any bibliographic information.

This prohibition includes:

* citation keys;
* paper titles;
* authors;
* journal names;
* conference names;
* publication years;
* volume numbers;
* issue numbers;
* page ranges;
* article numbers;
* DOI values;
* URLs;
* dataset DOIs;
* publisher names;
* journal indexing;
* JCR quartiles.

If a field cannot be verified, do not guess it.

Use:

`[BIBLIOGRAPHIC FIELD TO VERIFY]`

in an intermediate research record if necessary.

Do not place invented metadata into the final `.bib` file.

---

# 3. Existing BibTeX Entries Are Candidate Metadata

When the user provides an existing `.bib` file, do not automatically assume that its entries are correct.

Treat every existing entry as:

**candidate bibliographic information requiring validation when used.**

When an entry becomes relevant to the manuscript:

1. locate the publication;
2. verify its title;
3. verify authors;
4. verify publication venue;
5. verify year;
6. verify volume/issue when applicable;
7. verify page range or article number;
8. verify DOI;
9. verify that it is the intended version of the work.

Do not preserve an error merely because it already exists in `references.bib`.

---

# 4. Verification Priority

Use authoritative bibliographic sources in approximately the following order.

## Tier 1 — Preferred

* official publisher webpage;
* DOI landing page;
* official journal webpage;
* official conference proceedings;
* IEEE Xplore;
* ScienceDirect;
* SpringerLink;
* Wiley Online Library;
* ASCE Library;
* ACM Digital Library;
* CVF Open Access;
* Nature/Springer Nature official pages.

## Tier 2

* Crossref;
* PubMed;
* DBLP for computer science;
* official institutional repositories;
* official dataset repositories.

## Tier 3 — Discovery Only

* Google Scholar;
* Semantic Scholar;
* ResearchGate;
* general web search;
* citation aggregators.

Tier 3 sources may help locate a paper, but metadata should preferably be confirmed against Tier 1 or Tier 2 sources before the entry is finalized.

---

# 5. Search Result Is Not Verification

Finding a title in a search-engine result is insufficient.

Before adding the paper:

**search → open source → verify metadata → verify scientific content → create BibTeX**

Never perform:

**search snippet → generate BibTeX from memory**

---

# 6. DOI Is the Primary Identifier

When a DOI exists, verify and store it.

Use a bare DOI:

```latex
doi = {10.1016/j.autcon.2023.105217},
```

Preferred.

Do not store:

```latex
doi = {https://doi.org/10.1016/j.autcon.2023.105217},
```

The `doi` field contains the DOI identifier, not the DOI URL.

If a clickable URL is needed, the bibliography style can normally generate it from the DOI automatically.

---

# 7. DOI Normalization

Normalize DOI values by:

* removing `https://doi.org/`;
* removing `http://doi.org/`;
* removing `doi:`;
* removing unnecessary whitespace;
* retaining the DOI string itself.

Example:

```latex
doi = {10.1109/TITS.2023.3266776},
```

Do not modify capitalization or characters when doing so could alter the identifier.

---

# 8. DOI Verification

Before accepting a DOI, verify that it resolves to the same:

* title;
* authors;
* venue;
* publication.

Never infer a DOI from a similar paper.

A valid-looking DOI belonging to another paper is an invalid reference.

---

# 9. Prefer the Published Version

When both a preprint and a peer-reviewed version of essentially the same work exist, normally cite the authoritative published version.

Priority:

**peer-reviewed journal/conference version > accepted manuscript > preprint**

For example, if a method initially appeared on arXiv and was later formally published at CVPR, ICCV, ECCV, ICLR, or a journal, normally use the formal publication.

However, do not replace a preprint automatically when the later publication is a substantially extended or different work.

First verify whether both records represent the same scientific version.

---

# 10. Preprint Handling

A preprint is acceptable when:

* no peer-reviewed version exists;
* the preprint is the original authoritative source of the method;
* the specific version being discussed is only available as a preprint.

Do not represent a preprint as a journal article merely to make the bibliography appear stronger.

Prefer a representation such as:

```latex
@misc{author2024method,
  author        = {...},
  title         = {...},
  year          = {2024},
  eprint        = {...},
  archivePrefix = {arXiv},
}
```

when compatible with the bibliography system.

Do not claim that an arXiv/CoRR source is:

* SCIE;
* Q1;
* peer reviewed;

unless there is a separate verified formal publication.

---

# 11. Do Not Blindly Replace Preprints

A later journal article may expand or modify an earlier preprint.

For example:

**2021 preprint**
and
**2024 expanded journal paper**

may not be bibliographically interchangeable.

If the manuscript describes the original 2021 method, cite the source that actually supports that description.

If it discusses the later extended framework, cite the journal version.

Citation selection must be based on the **claim being supported**, not merely on publication prestige.

---

# 12. Canonical Entry Types

Use appropriate entry types.

## Journal article

```latex
@article{key,
  author  = {...},
  title   = {...},
  journal = {...},
  year    = {...},
  volume  = {...},
  number  = {...},
  pages   = {...},
  doi     = {...}
}
```

## Conference paper

```latex
@inproceedings{key,
  author    = {...},
  title     = {...},
  booktitle = {...},
  year      = {...},
  pages     = {...},
  doi       = {...}
}
```

## Preprint

Use `@misc` or the entry type required by the selected BibTeX/BibLaTeX environment.

## Dataset

Use `@dataset` only if supported by the bibliography system.

Otherwise use a compatible `@misc` entry.

Never choose the entry type based on appearance alone.

---

# 13. Minimum Fields for Journal Articles

A journal article should normally contain:

```latex
author
title
journal
year
volume
pages or article number
doi
```

Include:

```latex
number
```

when an issue number exists and is relevant.

Optional metadata may be retained only when it serves a purpose.

---

# 14. Minimum Fields for Conference Papers

A conference paper should normally contain:

```latex
author
title
booktitle
year
pages
doi
```

when DOI and pages exist.

Do not insert empty fields such as:

```latex
volume = {},
number = {},
```

Remove them.

---

# 15. Dataset References

When a dataset itself is used and has an official persistent record, cite the dataset record rather than inventing a paper citation.

Verify:

* dataset title;
* creators/authors;
* repository;
* release/version;
* year;
* DOI or persistent identifier.

Examples of acceptable repositories may include:

* Zenodo;
* Figshare;
* Mendeley Data;
* IEEE DataPort;
* institutional repositories.

If the dataset also has a companion paper, determine whether the manuscript needs:

* the dataset record;
* the dataset paper;
* or both.

Do not assume they are interchangeable.

---

# 16. `@dataset` Compatibility

The entry type:

```latex
@dataset
```

is primarily associated with BibLaTeX-compatible workflows.

If the manuscript uses traditional BibTeX/natbib and the selected `.bst` does not support `@dataset`, use an appropriate compatible entry such as:

```latex
@misc
```

Do not allow an unsupported entry type to silently disappear from the bibliography.

---

# 17. Citation Key Convention

Default citation-key format:

```text
firstauthorYYYYkeyword
```

Examples:

```latex
xiang2023dtrc
wang2024dualpath
zhuang2025review
```

Rules:

* lowercase;
* ASCII where possible;
* no spaces;
* no punctuation unless necessary;
* stable;
* human-readable;
* unique.

Use the canonical publication year associated with the cited version.

---

# 18. Citation Key Stability

Once a citation key is actively used throughout a manuscript, do not rename it casually.

If a key must be changed because the cited version changes:

1. update the `.bib` entry;
2. update every `\cite{}` occurrence;
3. verify that no old key remains;
4. compile/check for undefined references.

Never change the `.bib` key without updating the manuscript.

---

# 19. Key–Year Consistency

For newly created entries, the year embedded in the citation key should normally match the bibliographic `year`.

Avoid:

```latex
author2018method
```

with:

```latex
year = {2017}
```

unless the mismatch is intentionally preserved for backwards compatibility with an existing manuscript.

If an existing mismatch is retained, flag it during bibliography audit.

---

# 20. Author Formatting

Separate authors using:

```latex
and
```

Example:

```latex
author = {Xiang, Chao and Guo, Jingjing and Cao, Ran and Deng, Lu},
```

Do not separate authors with commas alone.

Preserve:

* compound surnames;
* accents;
* hyphenated names;
* particles;
* institutional authors.

Do not guess surname structure.

---

# 21. Corporate Authors

Protect institutional authors with braces when necessary:

```latex
author = {{World Health Organization}},
```

so BibTeX does not interpret the organization as a person's first and last names.

---

# 22. Title Preservation

BibTeX styles may modify capitalization.

Protect technical terms, acronyms, model names, and proper nouns where necessary.

Examples:

```latex
title = {{U-Net}: Convolutional Networks for Biomedical Image Segmentation},
```

```latex
title = {A Dual-Path Network Combining {CNN} and {Transformer} for Crack Segmentation},
```

Protect terms such as:

* CNN;
* RNN;
* LSTM;
* SHM;
* IoU;
* Transformer;
* ImageNet;
* U-Net;
* ResNet;
* DeepLabV3+;
* ESGA-Net;
* dataset names.

Do not indiscriminately wrap the entire title in double braces unless necessary.

---

# 23. Journal and Conference Names

Use the official publication name consistently.

Do not alternate randomly between:

```text
IEEE/CVF Conference on Computer Vision and Pattern Recognition
```

and:

```text
CVPR
```

within manually constructed entries unless the bibliography source/style dictates it.

Prefer canonical metadata from the official proceedings.

Let the `.bst`/BibLaTeX style control final abbreviation when possible.

---

# 24. Page Ranges

Use BibTeX range notation:

```latex
pages = {3006--3026},
```

not:

```latex
pages = {3006-3026},
```

The double hyphen produces the correct typographic en dash.

---

# 25. Article Numbers Are Not Page Ranges

Many modern journals use article numbers.

For example:

```latex
pages = {105217},
```

may be an article number rather than a conventional page.

Do not invent a page range around it.

Preserve the metadata supplied by the publisher.

---

# 26. Volume and Issue

For journal papers:

```latex
volume = {...},
number = {...},
```

when available.

Do not invent an issue number.

For conference papers, do not create empty fields such as:

```latex
volume = {},
number = {},
```

unless required by a specific bibliography workflow.

---

# 27. URL Policy

For journal or conference papers with a DOI, the DOI should normally be the primary persistent identifier.

A `url` field may be retained when useful, but:

* prefer an official publisher/proceedings URL;
* use HTTPS;
* remove tracking parameters;
* avoid temporary search-result URLs.

Do not duplicate:

```latex
doi = {10....},
url = {https://doi.org/10....}
```

unless the target bibliography style explicitly requires both.

---

# 28. Remove Retrieval Noise

Do not normally retain fields imported by DBLP, IEEE, ScienceDirect, or reference managers that are irrelevant to manuscript bibliography generation.

Examples include:

```latex
abstract
keywords
timestamp
biburl
bibsource
```

Remove them unless the user explicitly uses the `.bib` file as a literature database rather than purely as a bibliography.

---

# 29. Abstracts Do Not Belong in the Publication BibTeX by Default

For a manuscript bibliography file, remove:

```latex
abstract = {...}
```

unless abstracts are deliberately being retained for an internal research workflow.

The `.bib` file used for publication should remain compact and auditable.

---

# 30. Keywords Do Not Belong in the Publication BibTeX by Default

Remove imported:

```latex
keywords = {...}
```

unless they serve a specific bibliography-management purpose.

They are normally not used by journal bibliography styles.

---

# 31. Publisher Field

For journal articles, `publisher` is generally unnecessary when the target style does not use it.

Do not add:

```latex
publisher = {Elsevier},
```

to some journal papers while omitting it from others without a reason.

Prefer a minimal, consistent metadata set.

---

# 32. ISBN and Editor Fields

For conference proceedings or book chapters, `isbn`, `editor`, `publisher`, and `address` may be valid.

Retain them when:

* they are verified;
* they are required by the bibliography style;
* they identify the source correctly.

Do not retain them merely because a publisher export included them if they are irrelevant to the selected reference style.

---

# 33. Metadata Conflicts

Different authoritative databases occasionally report different page numbers, online-publication years, or proceedings metadata.

When authoritative sources disagree:

1. do not guess;
2. identify the exact cited publication version;
3. prefer metadata associated with the DOI/publisher record of that version;
4. preserve consistency throughout the manuscript;
5. flag the discrepancy if it cannot be resolved confidently.

Do not silently combine fields from different versions.

---

# 34. Online Year Versus Issue Year

A paper may have:

* online publication year;
* issue/volume year;
* conference year;
* proceedings publication year.

Use the year associated with the bibliographic version actually being cited.

Do not choose the year merely to match the citation key.

---

# 35. Conference-Year Ambiguity

Workshop proceedings are sometimes formally published in a later Springer volume.

For example:

**conference held in 2022**
but
**book volume copyright/publication metadata in 2023**

Verify the canonical citation recommended by the conference/publisher.

Do not automatically infer either year.

---

# 36. Primary Source Rule

If the manuscript discusses:

* a particular architecture;
* loss function;
* optimizer;
* dataset;
* metric;

cite the original source whenever possible.

Examples:

**U-Net** → original U-Net paper.

**AdamW** → original peer-reviewed AdamW publication when appropriate.

**clDice** → original clDice paper.

Do not cite a later crack-segmentation paper merely because it happens to use U-Net, AdamW, or clDice.

---

# 37. Method Version Rule

A method may have multiple versions.

Examples:

* conference version;
* extended journal version;
* `-II`;
* revised architecture;
* dataset extension.

Do not merge different versions into one BibTeX record.

Each scientifically distinct publication requires its own entry.

---

# 38. Duplicate Reference Detection

Before adding a new entry, search the existing `.bib` file by:

* DOI;
* normalized title;
* first author;
* year.

Do not create duplicate entries with different keys.

For example:

```latex
smith2024crack
```

and:

```latex
smith2024segmentation
```

must not point to the same DOI unless there is a deliberate reason.

---

# 39. DOI-Based Duplicate Detection

DOI should be treated as the strongest duplicate identifier.

If two entries have the same DOI, investigate them immediately.

Normally they represent the same publication and should be merged.

---

# 40. Title-Based Duplicate Detection

Normalize titles by ignoring:

* capitalization;
* surrounding braces;
* punctuation;
* minor typography.

If two entries have effectively identical titles and authors, verify whether they are duplicates or distinct publication versions.

---

# 41. Reference Selection and BibTeX Creation Are Separate Tasks

The workflow must be:

**Find source**
→ **verify scientific relevance**
→ **choose source**
→ **verify bibliographic metadata**
→ **add BibTeX**

Do not generate BibTeX for every search result.

Only selected references belong in the manuscript bibliography.

---

# 42. Q1/SCIE Status Should Not Be Stored as Bibliographic Metadata

Journal quality information such as:

* SCIE;
* JCR category;
* JCR quartile;
* JCR year;

is research-selection metadata, not standard publication metadata.

Do not create fields such as:

```latex
quartile = {Q1},
scie = {yes},
```

inside the publication `.bib` file unless an explicitly separate internal database requires them.

Keep this information in the **Citation Evidence Ledger**.

This is important because quartile classifications can change between JCR years.

---

# 43. Verification Ledger and BibTeX Must Be Separate

Maintain two conceptual layers.

## Research verification record

Contains:

* SCIE status;
* JCR quartile;
* JCR year;
* claim supported;
* relevance;
* source verification;
* notes.

## `references.bib`

Contains bibliographic metadata required to identify and cite the publication.

Do not contaminate the final bibliography with research-management metadata.

---

# 44. Recommended Evidence Ledger

Internally maintain:

| Key     | DOI     | Real source | Venue     | Year     | SCIE       | JCR         | Claim supported | Metadata verified |
| ------- | ------- | ----------- | --------- | -------- | ---------- | ----------- | --------------- | ----------------- |
| `[KEY]` | `[DOI]` | Yes         | `[VENUE]` | `[YEAR]` | `[YES/NO]` | `[Q1/etc.]` | `[CLAIM]`       | Yes               |

This ledger is used for source integrity.

It does not need to be included in the manuscript.

---

# 45. Citation Key Must Point to Exactly One Source

A citation key must have a one-to-one mapping:

[
\text{citation key}
\longleftrightarrow
\text{one verified bibliographic source}.
]

Never reuse a key for a replacement paper without checking every manuscript citation.

---

# 46. Citation–BibTeX Integrity

Every:

```latex
\cite{key}
```

must correspond to one existing `.bib` entry.

Every `.bib` entry cited in the manuscript must resolve without warnings.

When editing references, check for:

* undefined citations;
* duplicated keys;
* unused duplicate entries;
* malformed entries.

---

# 47. Citation–Claim Integrity

Bibliographic correctness alone is insufficient.

For every citation:

[
\text{citation key}
\rightarrow
\text{real publication}
\rightarrow
\text{verified content}
\rightarrow
\text{specific manuscript claim}.
]

If any link in this chain fails, the citation is invalid.

---

# 48. Numerical Claims Require Source-Level Verification

When the manuscript states:

`Method X achieved an IoU of 64.30%.`

the AI must verify:

* Method X;
* exact dataset;
* exact metric;
* exact numerical value;
* experimental context;

from the source itself.

The `.bib` entry only proves bibliographic existence; it does not prove the manuscript's numerical statement.

---

# 49. Do Not Use Bibliographic Metadata as Scientific Evidence

Fields such as:

```latex
abstract
keywords
title
```

may help discover relevance, but they are not always sufficient to support detailed technical claims.

Read the original source where necessary.

---

# 50. Special Characters

Escape LaTeX-sensitive characters correctly when required.

Examples:

```latex
\&
\%
\_
```

Preserve accented author names with BibTeX/BibLaTeX-compatible encoding.

Do not remove diacritics simply to avoid formatting problems.

---

# 51. Protect Mathematical or Technical Symbols in Titles

When titles contain mathematical or technical expressions, ensure that they compile correctly.

Examples may require:

```latex
{$L_1$}
```

or protected acronyms.

Do not rewrite the published title simply to make BibTeX easier.

---

# 52. Do Not Modify Official Titles

Preserve the title of the publication.

Do not:

* improve grammar;
* Americanize/Britishize spelling;
* alter hyphenation;
* change model names;
* change capitalization semantically;
* shorten the title.

Only apply LaTeX protection necessary for correct rendering.

---

# 53. Avoid Manual Bibliographic Invention

Do not construct an entry from memory such as:

```latex
@article{...,
 journal = {Automation in Construction},
 year = {2024},
 ...
}
```

merely because the venue seems plausible.

Every field must derive from verified metadata.

---

# 54. Bibliographic Cleaning Must Not Change Scientific Identity

Formatting cleanup may change:

```latex
doi = {https://doi.org/10.xxx}
```

to:

```latex
doi = {10.xxx}
```

but must not change the cited work itself.

A cleaning operation is distinct from a source-replacement operation.

---

# 55. Source Replacement Requires Explicit Verification

Replacing a preprint with a journal/conference publication requires verifying that the replacement supports the same manuscript claim.

If the newer publication substantially changes:

* architecture;
* authorship;
* experimental setup;
* scope;

do not silently replace it.

---

# 56. Minimal Publication BibTeX

Prefer compact entries.

A clean journal entry should resemble:

```latex
@article{xiang2023dtrc,
  author  = {Xiang, Chao and Guo, Jingjing and Cao, Ran and Deng, Lu},
  title   = {A Crack-Segmentation Algorithm Fusing Transformers and Convolutional Neural Networks for Complex Detection Scenarios},
  journal = {Automation in Construction},
  volume  = {152},
  pages   = {104894},
  year    = {2023},
  doi     = {10.1016/j.autcon.2023.104894}
}
```

Do not retain unnecessary imported metadata merely because it was available.

---

# 57. Recommended Conference BibTeX

Example structure:

```latex
@inproceedings{key,
  author    = {...},
  title     = {...},
  booktitle = {...},
  year      = {...},
  pages     = {xxxx--xxxx},
  doi       = {...}
}
```

Only include fields that are correct and useful.

---

# 58. Recommended Dataset Entry

For BibLaTeX when supported:

```latex
@dataset{key,
  author    = {...},
  title     = {...},
  year      = {...},
  publisher = {...},
  doi       = {...},
  url       = {...}
}
```

For conventional BibTeX when `@dataset` is unsupported:

```latex
@misc{key,
  author       = {...},
  title        = {...},
  year         = {...},
  howpublished = {...},
  doi          = {...},
  url          = {...}
}
```

Use only verified metadata.

---

# 59. File-Level Formatting Consistency

Within one `references.bib` file, use consistent:

* entry-type capitalization;
* indentation;
* field ordering;
* braces;
* DOI format;
* page-range notation;
* key naming.

Prefer:

```latex
@article
@inproceedings
@misc
```

consistently rather than mixing:

```latex
@ARTICLE
@article
@InProceedings
@INPROCEEDINGS
```

although BibTeX itself is generally case-insensitive.

Consistency improves auditability.

---

# 60. Recommended Field Order

For journal articles:

```text
author
title
journal
year
volume
number
pages
doi
url
```

For conference papers:

```text
author
title
booktitle
year
pages
publisher
doi
url
```

Consistency is more important than the exact order.

---

# 61. No Empty Fields

Remove:

```latex
volume = {},
number = {},
pages = {},
doi = {},
url = {},
```

An absent field is preferable to a meaningless empty field.

---

# 62. Comment Policy

Use `%` comments only for internal organization when useful.

Do not place unverifiable claims in comments such as:

```latex
% Q1 SCIE
```

unless the classification has been verified and the JCR year is recorded elsewhere.

Bibliographic comments must never substitute for a proper verification ledger.

---

# 63. Current-Year Publications

For papers published online ahead of issue assignment:

* verify official publication status;
* use the metadata currently provided by the publisher;
* do not invent a volume or issue;
* update metadata later if necessary.

A real online-first paper may legitimately have incomplete volume/issue information.

---

# 64. Recent Preprints

For very recent work without formal publication:

* verify arXiv identifier;
* verify authors/title/version;
* cite explicitly as a preprint;
* do not classify it as Q1/SCIE.

Prefer peer-reviewed literature for core research-gap claims whenever suitable alternatives exist.

---

# 65. Retracted or Corrected Papers

When encountered, verify whether a publication has:

* correction;
* erratum;
* expression of concern;
* retraction.

Do not use a retracted paper as normal evidence.

If the corrected version is relevant, cite the appropriate record.

---

# 66. Audit Existing `.bib` Before Submission

Before manuscript submission, perform a complete bibliography audit.

Check:

* duplicated keys;
* duplicate DOIs;
* malformed entries;
* incorrect entry types;
* missing DOI where one exists;
* DOI stored as URL;
* wrong years;
* wrong page ranges;
* empty fields;
* unused metadata;
* preprints with published replacements;
* unsupported `@dataset` entries;
* title capitalization;
* inconsistent author formatting;
* citation keys that no longer match the intended paper.

---

# 67. Cross-Check Against Manuscript

Before final submission:

1. collect all `\cite{}` keys from the manuscript;
2. verify each exists in `references.bib`;
3. verify every cited entry is the intended source;
4. identify unused bibliography entries;
5. identify duplicate sources;
6. compile the manuscript;
7. ensure no `undefined citation` warnings remain.

---

# 68. Never Modify Evidence Silently

If verification discovers that an existing reference is wrong:

* correct the bibliographic metadata if the source identity is clear;
* flag the correction when it materially affects the manuscript;
* recheck every sentence using the citation.

If the reference itself does not support the manuscript claim, the prose must also be revised.

Do not correct `.bib` while leaving an unsupported scientific statement unchanged.

---

# 69. Handling Unverified References

If the AI cannot verify an existing citation:

do not invent missing information.

Mark it internally as:

`[REFERENCE UNVERIFIED]`

and either:

* find the correct source;
* replace it with a verified source supporting the same claim;
* or remove/rewrite the unsupported claim.

---

# 70. Final BibTeX Integrity Checklist

For every bibliography entry:

* `[ ]` The publication actually exists.
* `[ ]` It is the intended publication/version.
* `[ ]` The author list is correct.
* `[ ]` The exact title is correct.
* `[ ]` The venue is correct.
* `[ ]` The publication year is correct.
* `[ ]` Volume/issue are correct if applicable.
* `[ ]` Pages/article number are correct.
* `[ ]` DOI is correct and resolves to the publication.
* `[ ]` DOI is stored in normalized form.
* `[ ]` Entry type is appropriate.
* `[ ]` Citation key is unique.
* `[ ]` Citation key is stable.
* `[ ]` Page ranges use `--`.
* `[ ]` No meaningless empty fields remain.
* `[ ]` No unnecessary import metadata remain.
* `[ ]` Acronyms/proper names in titles are protected where required.
* `[ ]` A peer-reviewed version has been preferred when appropriate.
* `[ ]` Preprints are not misrepresented as journal publications.
* `[ ]` Dataset entries are compatible with the bibliography system.
* `[ ]` The source supports the claim for which it is cited.

---

# 71. Core Reference Rule

A scientific reference is valid only when:

[
\boxed{
\text{Real source}
+
\text{Correct version}
+
\text{Verified metadata}
+
\text{Correct claim support}
}
]

If any of these components cannot be established, the AI must not fabricate the missing information.

---

# 72. Core BibTeX Rule

**Do not write a BibTeX entry because a paper probably exists. Find the real publication first, verify the authoritative metadata, verify that it supports the manuscript claim, and only then add the entry to `references.bib`.**
