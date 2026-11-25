# Reference Count Budgets & Per-Section Citation Architecture (`n = 1,009`–`1,016` CNS Manuscripts, `65,117` Dated Citations)

Empirically distilled from **1,009** high-impact tumor-omics manuscripts (2023–2026) for total reference counts, **1,016** manuscripts (`937` with complete 4-section parsing) for exact per-section citation allocation, and **65,117** dated references for citation recency.

---

## 1. Total Reference Count Budgets by Target Journal (`n = 1,009`)

Overall corpus median: **`71` total references** (IQR `56–84`, P10–P90 `45–101`).

> **Crucial *Nature* Portfolio Rule**: *Nature* and its sister journals split references into **Main-Text References** (listed after *Online content*, capped around ~50–60) + **Methods-Only References** (numbered continuously after *Methods*, adding ~20–30 refs that do NOT eat into the main-text budget!).

| Target Journal | `n` | Total Refs Median (IQR) | P10–P90 Range | Main-Text Only Median | Editorial Target Budget |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Mol Cell / Cell / Cell Metab / Immunity** | 94 | **84–91** (`67–111`) | 56–134 | — *(single unified list)* | **70–105** refs (*Cell Press* allows generous mechanistic & STAR Methods citations) |
| **Nature** | 87 | **80** (`66–86`) | 56–101 | **53** | **~50** main-text refs + **~25–30** Methods refs |
| **Science** | 23 | **80** (`66–98`) | 62–114 | — | **65–95** refs (main + supplementary references & notes) |
| **Nat Genet** | 50 | **78** (`61–91`) | 52–110 | **59** | **~55–60** main refs + **~20** Methods refs |
| **Sci Immunol / Cancer Cell** | 112 | **77–78** (`63–97`) | 44–109 | — | **65–95** refs |
| **Cancer Discov** | 50 | **74.5** (`57–84`) | 49–95 | — | **60–85** refs |
| **Nat Cancer / Nat Methods / Nat Cell Biol / Nat Biotechnol** | 151 | **71** (`51–87`) | 38–100 | **52–60** | **~50–60** main refs + **~15–20** Methods refs |
| **Cell Rep Med / Cancer Res / Nat Med / Nat Commun** | 237 | **66–70** (`51–84`) | 39–100 | **50** (*Nat Med*) | **55–80** refs (*Nat Med* caps main text near ~50–60!) |
| **Nat Immunol / J Clin Invest / Sci Transl Med** | 131 | **63–64** (`49–77`) | 39–87 | **52** (*Nat Immunol*) | **50–75** refs |
| **Clin Cancer Res** | 60 | **49** (`40–55`) | 32–72 | — | **Strict ~50-ref editorial ceiling!** |

---

## 2. Exact Citation Distribution Across the 4 Manuscript Sections (`n = 937`–`1,016`)

### 2.1 Overall 4-Section Allocation & Citation Density (Overturning the "Results Barely Cites" Myth!)

| Manuscript Section | Share of All 4 Sections (Unique Refs) | Share of All 4 Sections (Total Mentions) | Share of Main-Text 3 Sections Only (`n=1,016`) | **Citation Density (Cites / 100 Words)** | Approximate Refs in a 75-Ref Paper |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Introduction** | **`25.8%`** (med `24.2%`) | **`25.1%`** (med `23.5%`) | **`34.0%`** (med `31.6%`) | **`4.5` / 100w** *(IQR 3.1–6.0 — **#1 densest!**)* | **18–22** unique refs |
| **Results** | **`29.1%`** (med `28.8%`) | **`29.2%`** (med `29.0%`) | **`40.8%`** (med `40.6%`) | **`0.9` / 100w** *(IQR 0.6–1.3)* | **20–24** unique refs |
| **Discussion** | **`21.0%`** (med `20.0%`) | **`18.9%`** (med `18.0%`) | **`25.1%`** (med `24.3%`) | **`1.9` / 100w** *(IQR 1.3–2.7 — **#2 densest**)* | **15–18** unique refs *(+ ~17% re-cited from Intro!)* |
| **Methods / STAR** | **`24.1%`** (med `22.9%`) | **`26.7%`** (med `25.5%`) | *(excluded)* | **`0.7` / 100w** *(IQR 0.5–1.0)* | **16–22** unique refs *(software, pipelines, cohorts)* |

### 2.2 Journal-Family Citation Footprint (`mean %` of All-4 Mentions)

| Journal Family | Introduction | Results | Discussion | Methods | Key Editorial Distinction |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Nature Portfolio** | `25.3%` | `27.7%` | `14.6%` | **`32.4%`** | **Nearly 1/3 of all citations go to Online Methods** (keeping Main Text sleek under the ~50–60 ref budget); ultra-compact Discussion (`14.6%`). |
| **Cell Press** | `21.5%` | **`33.0%`** | `19.3%` | `26.2%` | Long, heavily contextualized Results (`33.0%` of all mentions; `45.2%` of main-text mentions) citing gene signatures, prior mouse models, and orthogonal cohorts inline. |
| **Science Family** | `22.0%` | **`33.8%`** | `21.6%` | `22.5%` | Dense mechanistic Results citations + balanced Intro/Discussion/Methods. |
| **Oncology Specialists** (*Cancer Discov*, *JCI*, *CR/CCR*) | **`28.5%`** | `26.5%` | **`22.4%`** | `22.6%` | Heavier clinical/trial framing in Introduction (`28.5%`) and clinical-trial comparison in Discussion (`22.4%`). |

---

## 3. What Exactly Should Be Cited in Each Section? (Zero Misplaced Citations)

1. **Introduction (`4.5` cites / 100w — High-Density Funnel)**:
   - Landmark disease burden / clinical trial outcomes (P1, 2–4 refs).
   - Core biological/TME background specifically tied to your 2–3 Results entities (P2, 8–12 refs).
   - Papers exposing the exact **Gap / Paradox / Technical Bottleneck** (P3, 4–6 refs).
   - Prior work from your own lab or foundational platform cited in the approach preview (P4, 1–2 refs).
2. **Results (`0.9` cites / 100w — Why Multi-Omics Results Holds `29%` of All Refs!)**:
   - **Never** dump literature reviews inside Results; cite ONLY **4 legitimate inline categories**:
     1. **Published marker genes, cell-state signatures & reference atlases** (`enriched for a myeloid mimicry signature previously described in glioma¹²`).
     2. **Public validation cohorts / clinical trials** (`TCGA, CheckMate, IMvigor210 cohorts¹³⁻¹⁵`).
     3. **Experimental models, genetic lines & key algorithms** when first named in prose (`using Perturb-map¹⁶`, `inferred via Slingshot¹⁷`).
     4. **One-clause premise justifying the next experimental pivot** (`Because X has been linked to Y¹⁸, we next tested whether...`).
3. **Discussion (`1.9` cites / 100w — Intro↔Discussion Loop Closure)**:
   - **Empirical Intro ↔ Discussion Reuse**: CNS authors re-cite a median **`16.7%`** (IQR `8.0–28.6%`) of their Introduction references inside Discussion to **close the exact conceptual loop** opened in Introduction!
   - Add **10–15 NEW references** not cited in Intro: conflicting/complementary mechanistic papers in other tumor types, recent clinical trials of candidate drugs/combinations, and methodological caveats/next-gen tools.
4. **Methods / STAR Methods (`0.7` cites / 100w — Full Software & Protocol Provenance)**:
   - Cite the original publication for EVERY non-trivial computational package (`Seurat`, `Scanpy`, `Harmony`, `CellChat`, `DESeq2`, `inferCNV`, `Monocle`, `SCENIC`, `Squidpy`), reference genome/signature database (`MSigDB`), clinical staging criteria (`RECIST v1.1`), and `"as previously described"` wet-lab protocols.

---

## 4. Citation Cluster-Size Discipline & Reference Recency Standards

### 4.1 Anti-Stuffing Law (`95.1%` of Citations Are `1–3` Refs!)
Directly validating the editorial anti-citation-stuffing rule across `1,016` manuscripts:

| Citations per Anchor | Empirical Share | Editorial Rule |
| :--- | :---: | :--- |
| **1 single reference** (`¹`) | **`75.4%`** | **Default CNS standard** — one surgical primary paper per specific claim! |
| **2 paired references** (`¹,²`) | **`14.0%`** | Ideal for dual confirmation or two landmark cohorts. |
| **3 references** (`¹⁻³`) | **`5.7%`** | Acceptable for broad consensus sentences in Intro P1 or multi-cohort lists. |
| **4 references** (`¹⁻⁴`) | `2.4%` | Use sparingly (`≤1–2` times per paper). |
| **5+ stuffed references** (`¹⁻⁸`) | **`2.5%` (AVOID!)** | Signals lazy reading or copy-pasted review blocks; break into specific claims with 1–2 targeted primary citations each! |

### 4.2 Reference Recency / Age Target (`n = 65,117` Dated References)
- **Median citation age**: **`6` years** (IQR **`3–10` years**, P10–P90 `2–16` years).
- **Frontier freshness (`≤ 3` years old)**: **`26.9%`** (~1/4 of your bibliography should be from the last 3 years — signals you are writing at the cutting edge, especially in spatial omics, AI pathology, and modern ICB trials!).
- **Core recent window (`≤ 5` years old)**: **`46.5%`** (nearly half of all citations!).
- **Enduring classics (`≥ 10` years old)**: **`28.2%`** (original biological discoveries, foundational algorithms, seminal statistical tests).
- **Red Flag**: If `< 25%` of your references are within the past 5 years (or `> 50%` are ≥ 10 years old), reviewers immediately perceive the framing as outdated.
