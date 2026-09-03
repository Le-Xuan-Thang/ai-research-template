# INTRODUCTION WRITING AND LITERATURE RESEARCH SKILL

## 1. Objective

When writing or rewriting the Introduction of a scientific paper, construct a rigorous scientific argument that explains:

1. why the research problem matters;
2. what makes the problem technically difficult;
3. what relevant approaches have already been investigated;
4. what limitations remain in the existing literature;
5. what precise research gap follows from those limitations;
6. why the proposed methodology is a logical response to that gap;
7. how the study is designed to validate its claims;
8. what the principal contributions of the paper are.

The Introduction must not function as a collection of loosely connected citations.

It must form a logical progression:

**Importance → Technical challenge → Existing solutions → Limitations → Synthesis → Research gap → Proposed solution → Validation objectives → Contributions**

---

# 2. Default Length

Unless the user or target journal specifies otherwise, target approximately:

**1,200–1,600 words**

with approximately **1,300–1,500 words** preferred for a full Introduction that also incorporates the essential related-work discussion.

This word range may be reduced when the manuscript contains a separate extensive `Related Work` or `Literature Review` section.

Do not increase length by adding generic background, repetitive citations, or unnecessary descriptions of individual papers.

---

# 3. Research Is Mandatory

Before drafting a research-based Introduction, conduct an actual literature search.

Do not rely exclusively on:

* model memory;
* references appearing in another manuscript;
* citation strings supplied by the user;
* titles inferred from context;
* automatically generated bibliographic information.

Every external reference that the AI introduces must correspond to a **real publication that has been located and verified**.

If web or scholarly-search access is available, use it before writing.

---

# 4. Absolute Non-Fabrication Rule

**Never fabricate a reference.**

Do not invent:

* paper titles;
* authors;
* journals;
* publication years;
* volume or issue numbers;
* page numbers or article numbers;
* DOI values;
* datasets attributed to a paper;
* numerical results;
* methodological details;
* journal indexing status;
* journal quartiles.

A citation that “looks plausible” is not acceptable.

A paper must be found and verified before it can be cited.

If an appropriate source cannot be verified, write:

`[CITATION NEEDED: claim/topic]`

rather than inventing a citation.

If bibliographic metadata remains uncertain, use:

`[SOURCE TO VERIFY]`

and do not present the source as confirmed.

---

# 5. Preferred Literature Window

Prioritize literature published within the **most recent five-year window**.

By default, interpret this as:

**the current calendar year plus the preceding four calendar years.**

For example, when writing in 2026, prioritize publications from:

**2022–2026.**

Older publications may be used when they are:

* foundational papers;
* original papers introducing a major architecture or theory;
* authoritative standards;
* seminal datasets;
* historically necessary references;
* the original source of a method still central to the study.

Do not replace an appropriate foundational source merely because it is older than five years.

Recent literature should dominate the discussion of the **current state of the art and unresolved research gap**.

---

# 6. Journal Priority

For engineering and scientific journal papers, use the following default priority hierarchy.

## Priority A — Highest

Recent peer-reviewed articles published in:

**SCIE-indexed, JCR Q1 journals**

within the latest five-year window.

These should form the core literature supporting:

* current research trends;
* technical limitations;
* state-of-the-art methods;
* research gaps;
* comparisons between methodological directions.

---

## Priority B

Recent high-quality review papers in SCIE Q1 journals.

Use reviews primarily for:

* broad research trends;
* domain importance;
* taxonomy of methods;
* identifying major research directions.

Whenever describing a specific method, result, architecture, or claim, prefer the **original research paper** over a review that merely cites it.

---

## Priority C

Relevant articles from:

* SCIE Q2 journals;
* leading field-specific journals;
* highly selective peer-reviewed conferences where conferences are primary publication venues for the discipline.

For computer vision and machine learning, major peer-reviewed conference papers may be scientifically preferable to weak journal sources when they are the original source of a method.

Examples include field-leading venues such as:

* CVPR;
* ICCV;
* ECCV;
* NeurIPS;
* ICML;
* ICLR;

when directly relevant.

Journal preference must not cause the AI to cite a less relevant paper instead of the original authoritative source.

---

## Priority D

Authoritative institutional sources may be used for factual background when appropriate, including:

* standards organizations;
* government agencies;
* major professional societies;
* official technical reports.

These sources should not replace peer-reviewed research when supporting scientific or methodological claims.

---

# 7. Q1 and SCIE Verification

Do not assume that a journal is Q1 or SCIE based on reputation.

For every source whose quality is being characterized as **Q1 SCIE**, verify:

1. the journal is indexed in the **Science Citation Index Expanded (SCIE)**;
2. its relevant JCR category;
3. its latest available JCR quartile;
4. the JCR year to which that quartile refers.

Prefer the Clarivate Master Journal List for SCIE coverage.

Prefer Journal Citation Reports for JIF/JCI quartile information.

A journal may belong to multiple categories and may have different quartiles across categories.

Therefore, never write simply:

`Journal X is Q1`

unless the applicable quartile has been verified.

---

# 8. Never Confuse Quartile Systems

Distinguish explicitly between:

* **JCR Q1**;
* **JCI Q1**;
* **SJR Q1 / SCImago Q1**;
* **Scopus CiteScore percentile/quartile**.

Do not treat them as interchangeable.

If the requirement is **Q1 SCIE**, prioritize verified JCR Q1 journals indexed in SCIE.

If only an SJR Q1 classification can be verified, do not label the journal as JCR Q1.

---

# 9. Source Verification Protocol

Before using a paper in the Introduction, verify it through the following process.

## Step 1 — Locate the publication

Search using combinations of:

* research topic;
* methodological keywords;
* proposed technical concept;
* task;
* dataset;
* author or title when known.

---

## Step 2 — Confirm the paper exists

Find at least one reliable bibliographic source, preferably:

1. publisher webpage;
2. DOI landing page;
3. IEEE Xplore, SpringerLink, ScienceDirect, Wiley, ASCE Library, Nature, etc.;
4. official institutional repository;
5. Crossref metadata.

Search-engine snippets alone are insufficient for final verification.

---

## Step 3 — Verify metadata

Confirm:

* exact title;
* author list;
* journal/conference;
* publication year;
* volume/issue/article number when available;
* DOI when available.

---

## Step 4 — Verify scientific relevance

Read at least the abstract and any accessible relevant sections.

Confirm that the source genuinely supports the sentence for which it will be cited.

Do not cite a paper simply because its title contains related keywords.

---

## Step 5 — Verify numerical claims

If reporting a value such as:

* IoU;
* Dice;
* F1;
* accuracy;
* FPS;
* FLOPs;
* number of parameters;
* sample size;

verify the exact value from the original paper or publisher record.

Never copy numerical values from an unverified secondary source.

---

## Step 6 — Verify journal quality when required

Check SCIE indexing and JCR quartile separately.

Do not infer them from the paper's citation count or publisher reputation.

---

# 10. Maintain a Citation Evidence Ledger

Before drafting, internally organize selected sources using a structure equivalent to:

| Citation | Real paper verified? | Year | Journal/Venue | SCIE | JCR Quartile | Claim supported             | DOI/source verified? |
| -------- | -------------------- | ---- | ------------- | ---- | ------------ | --------------------------- | -------------------- |
| Source A | Yes                  | 2025 | [...]         | Yes  | Q1           | limited-data challenge      | Yes                  |
| Source B | Yes                  | 2024 | [...]         | Yes  | Q1           | boundary-aware segmentation | Yes                  |

Do not cite a source until the relevant claim is recorded as supported.

The purpose of this process is to prevent **citation hallucination** and **citation–claim mismatch**.

---

# 11. Research by Concepts, Not Only by Paper Names

When the proposed method contains several technical ideas, independently research each concept.

For example, a method involving:

* multi-scale modeling;
* global attention;
* edge guidance;
* topology-aware loss;
* limited-data learning;

requires separate literature searches for each relevant research direction.

Do not search only for papers that resemble the final proposed architecture.

The research gap should emerge from a broad understanding of the literature rather than from confirmation bias.

---

# 12. Recommended Introduction Architecture

Use the following structure as the default for a complete engineering/AI Introduction.

## Paragraph 1 — Domain Importance and Practical Motivation

Establish:

* the broader engineering/scientific problem;
* why it matters;
* its practical consequences;
* why the specific task being studied is useful.

Typical progression:

**broader problem → target phenomenon → practical need → shortcomings of conventional practice → motivation for automated/computational method**

Example structure:

`[DOMAIN PROBLEM] has become an important concern for [STAKEHOLDERS/APPLICATION]. Among [...], [TARGET PHENOMENON] is particularly important because [...]. Reliable [TASK] is therefore essential for [...]. However, conventional [METHOD] remains [...]. These limitations have motivated increasing interest in [RESEARCH DIRECTION] [CITATION].`

Do not overload the first paragraph with technical architecture details.

---

# 13. Paragraph 2 — Technical Nature of the Problem

Explain why the specific task remains technically difficult.

Identify the characteristics of the data/problem rather than making a generic statement.

Possible issues include:

* small or sparse targets;
* weak boundaries;
* noise;
* environmental variability;
* class imbalance;
* long-range dependency;
* limited observations;
* nonstationarity;
* domain shift;
* topology;
* computational constraints.

The paragraph should conclude with **what capabilities an effective method therefore requires**.

Structure:

**problem characteristics → technical consequences → required modeling capabilities**

Example:

`Consequently, an effective model should not only [OBJECTIVE 1] but also [OBJECTIVE 2].`

This sentence creates the criteria used later to evaluate existing approaches.

---

# 14. Paragraphs 3–4 — Major Literature Streams

Organize related work by **methodological direction**, not as a random chronology.

For example:

### Stream 1

CNN-based approaches

### Stream 2

Transformer-based or hybrid approaches

### Stream 3

semi-supervised / limited-data learning

or any grouping appropriate to the research topic.

Within each stream:

1. briefly introduce the methodological direction;
2. select a small number of representative recent studies;
3. state what each study contributed;
4. include important quantitative evidence only when useful;
5. synthesize the strengths of the stream;
6. identify the remaining limitations.

Use:

**literature → evidence → synthesis**

not:

**Paper A did X. Paper B did Y. Paper C did Z.**

---

# 15. Selecting Representative Papers

Prefer approximately **2–4 representative studies per major literature stream**.

Selection should prioritize:

1. direct relevance;
2. recency;
3. Q1 SCIE status;
4. methodological influence;
5. originality;
6. experimental quality.

Do not list ten papers simply to increase citation count.

A few highly relevant papers discussed analytically are preferable to citation dumping.

---

# 16. How to Discuss an Individual Study

A compact literature description should normally contain:

**Author/method → key idea → relevant outcome**

Example pattern:

`Author et al. proposed [METHOD], which employs [KEY MECHANISM] to [PURPOSE]. The method achieved [RELEVANT RESULT] on [DATASET].`

Only include the numerical result if it serves the argument.

After discussing multiple studies, provide a synthesis sentence such as:

`Although these approaches improve [...], they remain limited by [...].`

The synthesis sentence is more important than an exhaustive description of every architecture.

---

# 17. Never Criticize a Study Without Evidence

Do not invent limitations of prior work merely to motivate the proposed method.

A limitation must be supported by:

* the original paper;
* comparative evidence;
* a review;
* a defensible architectural consequence;
* or an explicit synthesis of multiple verified sources.

Avoid unsupported statements such as:

`Existing methods have poor generalization.`

unless evidence supports this conclusion.

Prefer technically precise language:

`These approaches primarily emphasize [...], whereas [...], particularly under [CONDITION], remains less explored.`

---

# 18. Research-Gap Synthesis Paragraph Is Mandatory

Before introducing the proposed method, include a dedicated synthesis paragraph.

This is one of the most important components of the Introduction.

The paragraph should:

1. summarize the major strategies explored by previous studies;
2. acknowledge what those strategies achieve;
3. explain what combination of issues remains insufficiently addressed;
4. derive specific technical requirements for the present study.

Preferred logic:

**what exists → what each direction solves → what remains unresolved when considered jointly → design requirements**

Do not jump directly from:

`Previous method X has limitation Y.`

to:

`Therefore, we propose our model.`

---

# 19. Avoid Absolute Gap Claims

Use extreme caution with statements such as:

* `No previous study has ...`
* `This is the first study to ...`
* `No existing method ...`

Such claims require an unusually comprehensive search.

Prefer defensible formulations:

* `comparatively few studies have jointly considered ...`;
* `existing studies have largely focused on ...`;
* `these aspects have typically been investigated separately`;
* `limited attention has been given to ... under [CONDITION]`;
* `a remaining challenge is ...`.

Only use `first` or `no previous work` when an exhaustive literature search provides strong evidence.

---

# 20. Convert the Gap into Explicit Technical Requirements

When several unresolved issues exist, state them explicitly.

For example:

`Three issues are particularly relevant.`

Then explain:

`First, ...`

`Second, ...`

`Third, ...`

Each issue should later correspond to a component, objective, or training strategy in the proposed method.

The structure should resemble:

**Issue 1 → Design response 1**

**Issue 2 → Design response 2**

**Issue 3 → Design response 3**

This creates a traceable scientific argument.

---

# 21. Proposed Method Paragraph

After establishing the gap, introduce the proposed method.

Use transitions such as:

* `To address these issues, this study proposes ...`
* `Motivated by these considerations, we develop ...`
* `To overcome these limitations, we propose ...`

Explain:

1. method name;
2. main objective;
3. high-level design philosophy;
4. major technical components;
5. what problem each component addresses.

Do not provide equations or excessive implementation detail here.

---

# 22. Method Components Must Map to the Gap

The Introduction must make the reasoning traceable.

For example:

**thin and elongated morphology**
→ directional/strip context modeling

**long-range dependency**
→ global attention

**weak boundaries / contaminated skip features**
→ edge-guided gating

**fragmented predictions**
→ topology-aware supervision

If a proposed component has no preceding motivation in the Introduction, either:

* add the necessary literature-supported motivation;
* or reconsider whether the component belongs in the contribution narrative.

Do not present modules as an arbitrary collection of architectural additions.

---

# 23. Experimental Objectives Paragraph

For studies with extensive benchmarking, include a short paragraph describing the principal experimental objectives before listing the contributions.

A preferred structure is:

`The experimental study is designed around [NUMBER] main objectives.`

Typical objectives may include:

1. evaluate accuracy/generalization across independent datasets;
2. compare against representative competing methods under a controlled protocol;
3. quantify robustness/statistical variability;
4. evaluate computational complexity;
5. perform component ablations;
6. evaluate topology, boundary accuracy, or another contribution-specific property.

This paragraph should explain **how the paper will test its central claims**, not provide the Results.

If this information is not yet available, use placeholders.

---

# 24. Contributions Section

After the motivation, literature synthesis, proposed method, and validation objectives, present the principal contributions.

Preferred number:

**3–5 contributions.**

Each contribution should state a substantive scientific contribution rather than a generic manuscript activity.

Possible categories include:

1. overall framework;
2. novel architectural module;
3. novel learning objective;
4. methodological integration;
5. rigorous experimental/evaluation contribution.

Avoid weak contributions such as:

`We conduct experiments on several datasets.`

Prefer:

`An extensive controlled evaluation is conducted across [DATASETS] using [PROTOCOL], enabling [SPECIFIC SCIENTIFIC BENEFIT].`

---

# 25. Contribution Ordering

Order contributions from conceptual to empirical:

1. overall methodological framework;
2. principal novel modules;
3. learning/training formulation;
4. experimental methodology or benchmark contribution.

Contribution statements must be consistent with:

* Abstract;
* Methodology;
* Experiments;
* Results;
* Conclusion.

Do not advertise a contribution that is not subsequently demonstrated.

---

# 26. Avoid Double-Counting Contributions

Do not split one small design into several contributions simply to make the list longer.

For example, if two attention blocks are minor parts of a single feature-fusion mechanism, consider grouping them into one contribution.

Each bullet should represent a clearly distinguishable scientific advance.

---

# 27. Paper Organization Paragraph

If consistent with the target journal style, end the Introduction with a concise roadmap.

Example structure:

`The remainder of this paper is organized as follows. Section~\ref{...} ...`

Keep this paragraph short.

Do not summarize the manuscript a second time.

If the target journal discourages paper-organization paragraphs, omit it.

---

# 28. Citation Placement

Every literature-dependent scientific claim must be supported by an appropriate citation.

Citations are especially expected for:

* statements about the importance or prevalence of a problem;
* limitations of conventional approaches;
* characteristics reported by previous research;
* existing architectures;
* state-of-the-art methodological directions;
* annotation cost/scarcity;
* reported numerical results;
* known limitations of loss functions;
* claims about topology, generalization, efficiency, etc.

Do not attach citations randomly to the end of a paragraph if it is unclear which statement they support.

---

# 29. Citation–Claim Alignment

A citation must support the **specific claim immediately associated with it**.

Before citing a paper, ask:

`If a reviewer opens this paper, will they find evidence supporting this exact statement?`

If not, find another source or weaken the statement.

A real paper used for the wrong claim is still an invalid citation.

---

# 30. Use Primary Sources

When describing a specific proposed method, cite the original publication.

Do not write:

`Transformer-based crack segmentation has been proposed in [review citation]`

when the original Transformer crack-segmentation paper can be cited directly.

Reviews are useful for synthesis; original papers are preferred for individual methods and numerical results.

---

# 31. Numerical Results from Prior Studies

Include prior numerical results only when they serve a purpose such as:

* establishing current performance;
* demonstrating a trade-off;
* showing computational efficiency;
* motivating a specific gap.

Do not fill the Introduction with benchmark values.

Every reported value must be verified against the original source.

Maintain the original:

* metric definition;
* dataset;
* evaluation condition;
* image resolution when relevant.

Do not compare numbers across papers as though they were directly comparable when protocols differ.

---

# 32. Fairness When Discussing Prior Work

Do not make unfair comparisons between studies trained on different:

* datasets;
* data splits;
* image resolutions;
* preprocessing;
* annotation regimes;
* evaluation metrics.

If protocols differ, describe results as evidence from each paper, not as a controlled ranking.

Reserve direct performance ranking for controlled experiments in the current study.

---

# 33. Recent Literature Must Dominate the Gap

For the research-gap and current-state-of-the-art paragraphs, most supporting references should normally come from the latest five years.

Older references should not dominate these paragraphs unless the field has little recent work.

The literature search must extend to the current date.

Do not stop at the references already known to the user.

---

# 34. Search Beyond the User's Existing Bibliography

When the user provides a draft containing references, treat them as **candidate references**, not automatically verified references.

For each existing citation:

1. verify that the paper exists;
2. verify metadata;
3. verify the cited claim;
4. determine whether a newer or stronger source is available.

Do not preserve a questionable citation merely because it already appears in the manuscript.

---

# 35. Do Not Replace Good Sources Unnecessarily

If an existing citation is:

* real;
* highly relevant;
* authoritative;
* correctly supports the claim;

retain it even if another recent paper exists.

The goal is to improve evidential quality, not to replace references mechanically.

---

# 36. Literature Search Strategy

Before writing, construct searches covering at least:

### Search A — Domain importance

`[DOMAIN] + [PROBLEM] + review`

### Search B — Task-specific challenges

`[TASK] + challenges + [KEY PROPERTY]`

### Search C — Existing methodology family 1

`[TASK] + CNN / convolution / [METHOD FAMILY]`

### Search D — Existing methodology family 2

`[TASK] + Transformer / attention / hybrid`

### Search E — Proposed technical concept

`[TASK] + [COMPONENT OR TECHNICAL CONCEPT]`

### Search F — Research condition

`[TASK] + limited data / small dataset / noise / domain shift / etc.`

### Search G — Evaluation issue

`[TASK] + topology / boundary / connectivity / computational efficiency / etc.`

Adapt these searches to the paper.

---

# 37. Search Iteratively

Do not stop after the first search result.

Use an iterative process:

**broad search → identify terminology → narrower search → identify representative papers → follow related/citing papers → verify final sources**

If a relevant 2022 paper exists, search for papers from 2023–2026 that:

* extend it;
* challenge it;
* compare with it;
* address the same limitation.

---

# 38. Research Before Prose

Do not begin writing polished paragraphs while the literature search remains incomplete.

Preferred workflow:

1. understand manuscript topic;
2. identify proposed contributions;
3. map required evidence;
4. search literature;
5. verify sources;
6. construct research-gap logic;
7. draft Introduction;
8. audit every citation;
9. refine language.

This reduces the risk of writing a narrative first and later searching for citations merely to justify it.

---

# 39. Evidence Must Precede Strong Claims

Do not decide in advance that the literature has a particular gap and then selectively search only for supporting evidence.

Search broadly enough to determine whether another recent method already addresses the same combination of issues.

If such work exists:

* acknowledge it;
* refine the distinction;
* redefine the gap honestly.

The skill must prefer scientific accuracy over preserving a preconceived novelty claim.

---

# 40. Handling Closely Related Recent Work

If a paper is discovered that closely resembles the proposed methodology:

1. do not hide it;
2. cite it;
3. identify the precise difference;
4. determine whether the proposed novelty claim must be weakened or reformulated.

If the discovered work invalidates a proposed `first`, `novel`, or `unexplored` claim, remove or revise that claim.

---

# 41. Missing Information

As with the Abstract Skill, never invent unavailable study-specific information.

Use precise placeholders such as:

* `[METHOD_NAME]`
* `[TARGET_APPLICATION]`
* `[DATASET_NAMES]`
* `[NUMBER_OF_DATASETS]`
* `[NUMBER_OF_BASELINES]`
* `[EXPERIMENTAL_OBJECTIVE]`
* `[CONTRIBUTION]`
* `[COMPUTATIONAL_ANALYSIS]`
* `[CITATION NEEDED: specific claim]`

Continue drafting when possible rather than stopping solely because some study information is unavailable.

---

# 42. Missing Literature Evidence

A missing citation is fundamentally different from a missing method name or result.

If literature research fails to identify evidence for a scientific claim:

**do not state the claim as fact.**

Choose one of:

1. weaken/reformulate the statement;
2. remove it;
3. insert `[CITATION NEEDED: ...]`;
4. explicitly state that support could not be verified.

Never generate a fake `\cite{}` key to make the paragraph appear complete.

---

# 43. LaTeX Citation Rules

When producing LaTeX manuscript text:

Use citation commands consistently with the manuscript's citation package.

Typical forms include:

```latex
\cite{key}
```

```latex
\citet{key}
```

```latex
\citep{key}
```

Use author-integrated citation when the authors are grammatical subjects:

```latex
\citet{smith2025method} proposed ...
```

Use parenthetical citation when the reference supports a statement:

```latex
... remains difficult under limited annotated data
\cite{smith2025method,jones2024review}.
```

Never create a citation key unless it corresponds to a verified real bibliographic entry.

---

# 44. Bibliographic Key Integrity

When adding new literature to a LaTeX manuscript, maintain a traceable mapping:

**citation key → verified paper → DOI/publisher record**

A recommended key convention is:

`firstauthor + year + shortkeyword`

for example:

```latex
xiang2023dtrc
```

but the exact convention should follow the user's existing `.bib` style.

Do not silently create multiple keys for the same publication.

---

# 45. BibTeX Integrity

If BibTeX entries are requested, obtain bibliographic information from a reliable source.

Verify at minimum:

* `title`;
* `author`;
* `journal` or `booktitle`;
* `year`;
* `volume`;
* `pages` or article number when available;
* `doi`.

Do not invent missing BibTeX fields.

If a field cannot be verified, omit it or mark it for verification rather than guessing.

---

# 46. Language Style

Use formal scientific English appropriate for high-quality engineering journals.

Prefer:

* precise technical language;
* evidence-based statements;
* logical transitions;
* measured novelty claims;
* synthesis rather than promotional language.

Avoid:

* exaggerated claims;
* conversational expressions;
* rhetorical questions;
* excessive adjectives;
* generic filler;
* repeated `In recent years` openings.

---

# 47. Paragraph Connectivity

Every paragraph should have:

1. a clear topic sentence;
2. supporting evidence;
3. synthesis;
4. a transition toward the next paragraph.

The final sentence of a literature paragraph should often establish the reason for discussing the next research direction.

Example progression:

**CNN strengths → local/context limitation**
→ motivates Transformer discussion.

**Transformer strengths → complexity/data limitation**
→ motivates specialized crack-aware mechanisms.

**specialized mechanisms → remaining fragmented treatment**
→ motivates unified proposed framework.

This is preferable to isolated paragraphs.

---

# 48. Avoid Literature Catalogues

Do not produce paragraphs of the form:

`A proposed X. B proposed Y. C proposed Z. D proposed W.`

After discussing representative papers, synthesize them.

Use statements such as:

`Collectively, these studies demonstrate that [...]. However, [...].`

The scientific value of the Introduction lies in the synthesis, not the number of paper names mentioned.

---

# 49. Research Gap Must Be Earned

The phrase:

`To address these challenges, we propose ...`

may appear only after the preceding literature discussion has established:

* what has been tried;
* what has worked;
* what remains problematic;
* why the remaining problem matters.

The proposed method should feel like a logical consequence of the literature review.

---

# 50. Default Structural Template

For a full Introduction, use approximately:

### Paragraph 1

**Problem significance and practical motivation**

### Paragraph 2

**Task-specific technical challenges**

### Paragraph 3

**Established methodological family**

### Paragraph 4

**More recent/alternative methodological family + practical constraint**

### Paragraph 5

**Cross-literature synthesis + precise research gap + explicit unresolved issues**

### Paragraph 6

**Proposed method and gap-to-design mapping**

### Paragraph 7

**Experimental objectives / validation strategy**

### Contribution list

**3–5 main contributions**

### Final paragraph

**Paper organization, when appropriate**

Do not follow this mechanically if the topic requires a different organization, but preserve the underlying argumentative logic.

---

# 51. Adaptation When a Separate Related Work Section Exists

If the manuscript contains a substantial separate `Related Work` section:

* shorten Paragraphs 3–5;
* cite only the most representative papers;
* avoid extensive numerical comparisons;
* retain enough literature to establish the research gap;
* move detailed method-by-method discussion to Related Work.

The Introduction must still establish novelty independently.

---

# 52. Introduction Audit — Scientific Logic

Before returning the Introduction, verify:

* Is the practical/scientific importance clear?
* Is the technical problem clearly defined?
* Are the main challenges specific?
* Are the major literature streams covered?
* Is recent literature sufficiently represented?
* Does each cited paper actually exist?
* Does each citation support its associated claim?
* Have journal quality claims been verified?
* Is the research gap based on literature synthesis?
* Is the gap stated cautiously enough?
* Does every major method component respond to an identified issue?
* Are experimental objectives aligned with the paper's claims?
* Are contributions distinct and defensible?
* Does the Introduction lead naturally to the Methodology?

---

# 53. Introduction Audit — Citation Integrity

For every citation added by the AI, verify:

* `[ ]` The publication exists.
* `[ ]` The exact title is verified.
* `[ ]` Authors are verified.
* `[ ]` Publication year is verified.
* `[ ]` Journal/conference is verified.
* `[ ]` DOI or authoritative publication page is located when available.
* `[ ]` The relevant claim is supported by the source.
* `[ ]` Any reported numerical value is exact.
* `[ ]` SCIE status is verified if claimed.
* `[ ]` JCR Q1 status is verified if claimed.
* `[ ]` JCR Q1 has not been confused with SJR Q1.
* `[ ]` A more appropriate primary source has not been ignored.

If any required verification fails, do not present the citation as verified.

---

# 54. Introduction Audit — Recency

Check the publication-year distribution.

For the current state-of-the-art discussion:

* prioritize literature from the most recent five years;
* include current-year publications when available;
* retain older seminal work only where scientifically justified.

If almost all references are old while substantial recent literature exists, conduct another search before finalizing.

---

# 55. Introduction Audit — Novelty

Before writing:

`To the best of our knowledge...`

or:

`This is the first...`

perform a dedicated novelty search using combinations of all central technical concepts.

If equivalent or closely related recent work is found, revise the claim.

If novelty cannot be established confidently, use a narrower factual statement describing exactly what this study combines or evaluates.

---

# 56. Final Research Integrity Rule

The quality of an Introduction is determined not by how many references it contains, but by whether the literature creates a defensible chain of reasoning.

The required reasoning pattern is:

**verified evidence**
→ **literature synthesis**
→ **identifiable limitation**
→ **research gap**
→ **methodological response**
→ **testable contribution**

At no point may fabricated literature, unverifiable metadata, unsupported numerical results, or assumed journal rankings be used to complete this chain.

# CORE RULE

**Research first, verify every source, synthesize the literature, derive the gap from evidence, and only then introduce the proposed method. If a source or claim cannot be verified, use a placeholder or remove the claim—never fabricate it.**
