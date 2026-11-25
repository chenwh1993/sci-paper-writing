---
name: sci-paper-writing
description: >-
  Architect, draft, polish, translate, and audit publication-grade scientific
  manuscripts (Nature, Cell, Science, Cancer Cell, Nature Medicine, Immunity,
  Nature Methods standard) across ALL nine manuscript components: Title,
  Abstract, Introduction, Results, Results Subheadings, Discussion, Figure
  Captions, Methods / STAR Methods, and Cover Letter. Empirically distilled
  from 2,725 titles, 1,464 full-text 2025-2026 high-impact biomedical/oncology
  articles, 2,990 CNS figure captions, and 307 CNS Methods/STAR Methods,
  benchmarked against Nature, MIT/Harvard, Science, and Elsevier editorial
  standards. Use whenever designing manuscript storyline from Results,
  choosing Title/Abstract/Intro/Discussion framing, drafting or polishing any
  manuscript section with authentic CNS grammar/verbs/transitions, writing a
  Cover Letter, or auditing a manuscript before submission.
---

# `sci-paper-writing` — Full-Manuscript CNS Scientific Writing & Narrative Architect Skill

An end-to-end, empirically grounded scientific writing system uniting **strategic storyline architecture** (how top-tier authors reverse-engineer Title, Abstract, Introduction, Subheadings, Discussion, and Cover Letter from a given set of Results) with **authentic CNS grammar, tense discipline, verb certainty ladders, transition corpora, Figure Captions, Methods/STAR Methods, and automated pre-submission auditing**.

Empirically distilled and cross-validated across **2020–2026**:
- **6,665** high-impact tumor-omics titles (`2,725` from 2025–2026 + `3,940` from 2020–2024) & **1,960** full-text manuscripts (`1,464` 2025–2026 derivation + `496` 2020–2024 out-of-time hold-out validation across *Nature*, *Cell*, *Science*, *Cancer Cell*, *Nat Med*, *Nat Cancer*, *Nat Genet*, *Nat Immunol*, *Nat Methods*, *Immunity*, *Sci Transl Med*, *Cancer Discov*, *Cell Rep Med*, *Nat Commun*)
- **2,990** CNS Figure Captions & **307** complete CNS Methods / STAR★METHODS sections
- Curated *Nature* Summary Paragraph, MIT/Harvard CommKit *Discussion*, *Science* *Intro/Results*, and Elsevier *Cover Letter* editorial standards.

---

## Three Operating Modes (Pick Based on User Request)

### Mode A — Storyline Architect Mode (When Starting from Results / Outline / Revision)
**Always execute before drafting prose when the user shares experimental/omics Results or asks how to frame a paper:**
1. **Classify the Study Archetype** (see [references/00-strategic-narrative-design.md](./references/00-strategic-narrative-design.md)):
   - `Mechanistic Axis + Perturbation` | `Clinical Biomarker / Therapy` | `Atlas / Spatial Resource` | `Evolution / Metastasis` | `Computational / Tech Method`
2. **Identify the Target Journal Tier** (`nature`, `nature_sister`, `nat_med`, `cell`, `cancer_cell`, `science`) because journal rules strictly govern Title length/colons, Abstract word caps (`150` vs `200` words), Subheading style (`5w` phrase vs `10w` full clause), and Limitations placement.
3. **Reverse-Engineer the Whole Manuscript from Results** (never draft Intro from textbook background!):
   - Extract the **2–3 core tension entities** from the Results → prune Introduction down to ONLY those entities (`P1` broad hook `10%` overlap → `P2–P3` focused tension `37%` overlap → strong non-trivial Gap → `Here, we...` preview).
   - Propose **3 ranked Title candidates** (Conceptual Causal vs Discovery-Target Hybrid vs Clinical/Tool Brand) matched to the journal.
   - Map the **6–7 Results Subheading Domino Chain** (`H1` Discovery/Cohort → `H2–H5` Spatial/Molecular Mechanism → `H6–H7` In Vivo Rescue / Clinical Translation).
   - Design the **Discussion 4-Layer Elevation** (Unified Conceptual Model → Paradox Reconciliation → Actionable Translational Roadmap → Constructive 3-Part Limitations).

### Mode B — Section Drafting & Idiomatic Polishing Mode
Load ONLY the relevant section reference file(s) from the table below, enforce its non-negotiable grammar/tense/verb-ladder rules, eliminate Chinglish patterns, and preserve scientific precision.

### Mode C — Automated Audit & Scaffolding Mode
Run [`scripts/audit_manuscript.py`](./scripts/audit_manuscript.py) to catch word-limit overflows, weak gaps, subject-style figure citations (`Fig. 1 shows`), verb overclaiming, P1 raw-stat repetition in Discussion, missing Cell Press Limitations, Cover Letter hype/compliance omissions, or Figure Caption / Methods reproducibility flaws:
```bash
python scripts/audit_manuscript.py audit --section all --journal nature --file manuscript.md
python scripts/audit_manuscript.py audit --section abstract --journal cell --file abstract.txt
python scripts/audit_manuscript.py scaffold --archetype mechanistic --journal cancer_cell
```

---

## Ten Non-Negotiable Full-Manuscript CNS Laws

1. **Journal-Calibrated Titles** ([01-title-and-abstract.md](./references/01-title-and-abstract.md)): *Nature* `~9w / 0% colons`, *Science* `~10w / 0% colons`, *Cell/Cancer Cell* `11–12w`, *Nat Med* `~14w / 46% clinical colon / 2.4% declarative` (no hype!), *Nat Methods* `ToolName: ...` (`38%` colon). Mechanistic papers use active causal clauses (`84.3%`: `drives`, `promotes`, `controls`, `reprograms`). Never open with `"Study on..."` or `"Analysis of..."`.
2. **Findings-Centered, Anti-Methods-Bloat Abstracts** ([01-title-and-abstract.md](./references/01-title-and-abstract.md)): Hard caps: *Nature* `~200w`, *Nat Med* `~218w`, *Nature* sisters + *Cell*/*Cancer Cell* `≤150w`, *Science* `≤125w`. Allocate ~50% of sentences to core quantitative findings (`Here, we show/identify/present...`), compress Methods to ≤1 sentence (`3.5%` empirical share), and never write a mini-full-text methods log.
3. **Reverse-Engineered Introduction Funnel & Zero Weak Gaps** ([02-introduction.md](./references/02-introduction.md)): `3–4` paragraphs (`Nature ~390w`, `Cell/Cancer Cell ~470–530w`). Introduce ONLY the 2–3 concepts paid off in Results. Never use weak `"few studies have investigated"` gaps (`1.1%` in 2025–2026 CNS); anchor Gaps in mechanistic unknown (`67%`), spatial/single-cell blindspot (`60%`), clinical resistance (`53%`), or technical bottleneck (`22%`). Respect 3-tense split (Present `55%` / Past `31%` / Present Perfect `15%`).
4. **Journal-Matched Results Subheadings (`6–7` Domino Modules)** ([03-results-and-subheadings.md](./references/03-results-and-subheadings.md)): *Nature* uses crisp `5–7` word headlines; *Cell / Cancer Cell / Immunity / Sci Transl Med* use `10–12` word active declarative takeaway sentences (`52–68%`). Order logically so each module's discovery motivates the next (`To investigate/determine/test...`).
5. **Inline Parenthetical Figure Citations (`765 : 1`) & Strict Results Past Tense (`4.9 : 1`)** ([03-results-and-subheadings.md](./references/03-results-and-subheadings.md)): Always cite figures parenthetically at clause end (`...increased tumor infiltration (Fig. 1a)`), **NEVER** as sentence subjects (`"Fig. 1a shows..."`). Write Results observations in Simple Past; avoid `data not shown` (`2.9%`).
6. **4-Tier Certainty Verb Ladder — Never Overclaim or Randomly Swap Verbs** ([03-results-and-subheadings.md](./references/03-results-and-subheadings.md)): Match verb strength strictly to evidence: Genetic rescue/in vivo causality (`demonstrated`, `established`, `abolished`, `rescued`, `drove`) > Direct assay/omics observation (`showed`, `identified`, `enriched`, `increased`, `induced`) > Computational inference (`indicated`, `suggested`, `supported`, `consistent with`) > Correlative cohort observation (`associated with`, `correlated with`, `linked to`, `may/might`). Avoid `"proved"` (`<0.1%`).
7. **Zero-Repetition, 4-Layer Elevated Discussion** ([04-discussion.md](./references/04-discussion.md)): Follow MIT/Harvard 5 blocks. **99.6%** of top-journal Discussion P1s do NOT repeat raw P values or percentages — open with a 2–3 sentence unified conceptual model answering Introduction's big question. Reconcile prior literature (`Consistent with...`, `Whereas prior studies..., our data...`), specify concrete translational utility (`77%`), and obey journal Limitations norms (**mandatory `Limitations of the study` subheading in Cell Press** `85–98%`, standalone paragraph in *Nat Med* `70%`, woven constructively in *Nature* `26%`).
8. **30-Second Editor-Focused Cover Letter** ([05-cover-letter.md](./references/05-cover-letter.md)): Strictly 1 page (`300–500` words). Targeted Editor greeting; 2–3 sentence strategic breakthrough (**never** paste the Abstract); specific journal-scope fit citing 1–2 recent papers from that journal; 4 mandatory compliance statements (originality, COI, funding, ethics); zero empty superlatives (`groundbreaking`, `first ever`).
9. **Telegraphic Participial Figure Captions (`5 : 1` `-ing`)** ([06-figure-captions.md](./references/06-figure-captions.md)): Exact journal syntax (*Nature* `Fig. 1 | ...` + `a, b,` + British spelling + `≤350w`; *Cell* `Figure 1. ...` + `(A)` + American spelling); mandatory `n` + biological unit, boxplot/error-bar anatomy, two-sided test + FDR, scale bars, and Source Data.
10. **Past-Passive Reproducible Methods (`9.89 : 1`)** ([07-methods-and-star.md](./references/07-methods-and-star.md)): Match *Nature* Online Methods vs *Cell* STAR★METHODS (+ Key Resources Table) vs *Science*; disclose exact software versions, genome builds, IRB/IACUC, STR/mycoplasma authentication, patient-level/pseudobulk stats, and permanent data/code accessions.

---

## Reference Library (Load On Demand)

| Reference File | Load When Working On |
| :--- | :--- |
| [references/00-strategic-narrative-design.md](./references/00-strategic-narrative-design.md) | **Higher-order storyline design**: mapping identical Results to optimal Title, Abstract hook, reverse-engineered Intro, Subheading arc, and Discussion elevation across 5 Study Archetypes + 5 CNS end-to-end blueprints |
| [references/01-title-and-abstract.md](./references/01-title-and-abstract.md) | Drafting/polishing **Title**, **Abstract**, and mandatory journal **Companion Micro-Texts** (*Cell* `Highlights` & `In brief`, AACR `Significance`, *Science* `Teaser`) |
| [references/02-introduction.md](./references/02-introduction.md) | Drafting/polishing **Introduction** (funnel blueprint, 5 strong Gap types, 3-tense rules, transition stems, 10-point check, Chinglish fixes) |
| [references/03-results-and-subheadings.md](./references/03-results-and-subheadings.md) | Drafting/polishing **Results & Subheadings** (journal subheading norms, 3-move paragraph anatomy, inline `(Fig. 1a)` law, 4-tier Certainty Verb Ladder, cohesion bridges, Chinglish fixes) |
| [references/04-discussion.md](./references/04-discussion.md) | Drafting/polishing **Discussion & Limitations** (MIT/Harvard 5-block model, P1 synthesis stems, literature reconciliation, translational framing, constructive 3-part Limitations phrasebank) |
| [references/05-cover-letter.md](./references/05-cover-letter.md) | Drafting **Cover Letters** (Elsevier/CNS 5-step structure, Good vs Bad phrasing, 4 compliance declarations, 4 journal-ready templates) |
| [references/06-figure-captions.md](./references/06-figure-captions.md) | Drafting/auditing **Figure Captions** (journal specs, `-ing` syntax, 13 chart templates, mandatory stats/boxplot/scale-bar disclosures) |
| [references/07-methods-and-star.md](./references/07-methods-and-star.md) | Drafting/auditing **Methods & STAR★METHODS** (Nature/Cell KRT/Science schemas, past-passive grammar, wet-lab/single-cell/spatial/stats/data-code templates) |
| [references/08-comprehensive-phrasebank-and-collocations.md](./references/08-comprehensive-phrasebank-and-collocations.md) | **Exhaustive 1,960-paper Phrasebank & Verb Precision Guide**: 5 verb confusion matrices (evidence, positive/negative causation, state-change, spatial), top 4-gram openers, and 12 ready-to-migrate micro-scenario sentence frame banks |
| [references/09-citation-and-reference-architecture.md](./references/09-citation-and-reference-architecture.md) | Planning **Reference Budgets & Per-Section Citation Distribution** (journal caps across 20 journals, Intro/Results/Discussion/Methods exact share & density, `95.1%` 1–3 anti-stuffing law, Intro↔Discussion reuse, reference recency) |
| [references/10-figure-and-supplement-architecture.md](./references/10-figure-and-supplement-architecture.md) | Planning **Main vs Extended Data/Supp Figure Counts, Subpanel Budgets & Content Triage** (20-journal exact figure/panel caps, Main-vs-Supp empirical enrichment matrix, `Fig. 1 → Fig. 7` storyboard, 1:1 `Main ↔ Supp/ED` pairing map) |
| [scripts/audit_manuscript.py](./scripts/audit_manuscript.py) | Running automated grammar, rule-compliance, and reproducibility audits or generating journal-calibrated manuscript scaffolds |
