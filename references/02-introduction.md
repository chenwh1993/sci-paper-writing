# Introduction Writing Rules, Funnel Architecture & Idiomatic Corpus

Empirically distilled from **1,395** 2025–2026 published biomedical & oncology CNS Introductions (real published literature is the single ground truth; engineering/social-science blog conventions such as macro market-size openers or separate Literature Review roadmaps do NOT apply to biomedical CNS articles).

---

## 1. Journal Word & Paragraph Budgets (`n = 1,395`)

| Target Journal | Median Words | Target Paragraphs | Final-Paragraph Preview (`Here, we...`) | Editorial Pace |
| :--- | :---: | :---: | :---: | :--- |
| **Nature** | **386w** | **3** | 41.7% | Ultra-tight; unheaded directly after Abstract; zero throat-clearing |
| **Nat Med** | **465w** | **2–3** | ~45% | Straight to clinical unmet need → trial/biomarker rationale |
| **Cancer Cell / Nat Cancer** | **469–498w** | **4** | **52.7–58.0%** | Crisp 4-paragraph funnel ending with 1 full summary paragraph |
| **Cell / Immunity / Sci Transl Med** | **509–530w** | **4** | **54.3%** (*Cell*) | Balanced biological context + explicit final preview |
| **Nat Genet / Nat Immunol / Cancer Discov** | **520–560w** | **4** | 40–44% | Sharp domain funnel |
| **Nat Methods / Nat Biotechnol / Nat Commun** | **613–723w** | **4–5** | 43–49% | Needs 1 focused paragraph diagnosing existing technical/spatial trade-offs |

---

## 2. The 4-Paragraph CNS Funnel Architecture (Reverse-Engineered from Results)

Remember the empirical **Results → Introduction Back-Propagation Law** (`n = 932`):
`P1` introduces only `10%` of Results entities → `P2–P3` surges to `36.8%` → `Final P` locks in `28.4%` (`52.6%` cumulative). **Never dump textbook knowledge that does not pay off in Results.**

| Paragraph | Move & Role | Word Share | Exact Job |
| :--- | :--- | :---: | :--- |
| **P1** | **Broad Known Stakes (Macro Hook)** | ~20–25% | Establish clinical burden OR fundamental biological importance in 3–5 concise sentences. Cite 2–3 landmark reviews/stats. |
| **P2** | **Narrow Focus to the 2–3 Core Entities** | ~25–30% | Synthesize what IS known about the exact cell state, pathway, spatial niche, or modality your Results study — grouped **by theme/concept**, NEVER author-by-author (`"Wang et al. found... Li et al. found..."`). |
| **P3** | **The Sharp Gap → Scientific Question** | ~20–25% | Pivot cleanly (`However, ...` / `Yet ...` / `Despite ...`) into 1 of the **5 Strong Gap Types** below, then frame the exact testable question or hypothesis **BEFORE** introducing your method. |
| **P4** | **Approach + Core Findings Preview + Significance** | ~25% | `Here, we addressed this gap by...` / `In this study, we integrated...` State the experimental/omics strategy concisely (no Methods parameters!), preview the 2–3 flagship findings, and close with 1 grounded sentence of conceptual or clinical value. |

- **Acronym, Code & P4 Restraint in Introduction (`n = 1,441` Published Papers)**: Keep ALL-CAPS acronyms/gene symbols to **`≤ 6–7 / 100w`** (*Nature* median `3.5`, *Nat Commun* `4.6`, *Cancer Cell* `5.9`; warn `> 8.5 / 100w`). Define ONLY acronyms reused `≥ 3×` in Main Text; **NEVER leak Results-only internal codes** (`MP4/MP9`, `CN1–10`, `Model A/B`, `Ensemble-5`) or exact sub-figure micrometer measurements into Introduction, and avoid bolting on unrelated secondary goals with `"Addressing these questions also requires..."` at the end of P3 (weave clinical deployability organically into the clinical biomarker bottleneck!).

---

## 3. Five Strong Gap Archetypes vs Banned Weak Gaps

In 2025–2026 CNS/high-IF papers (`n = 1,395`), the weak `"few studies have investigated"` gap appears in only **`1.1%`** of articles. Always anchor your Gap in one (or a stacked pair) of these **5 High-Impact Gap Types**:

| Gap Type | Empirical Rate | Authentic CNS Gap Templates |
| :--- | :---: | :--- |
| **1. Mechanistic / Causal Black Box** | **67.1%** | `However, the molecular mechanisms by which [X] drives [Y] remain poorly understood.`<br>`Yet whether [X] actively instructs [phenotype] or merely reflects [bystander effect] remains unclear.` |
| **2. Spatial / Single-Cell / Niche Blindspot** | **60.1%** | `Although bulk sequencing has catalogued [alterations], it lacks the spatial resolution required to resolve cellular neighbourhoods and in situ ligand–receptor interactions.`<br>`Consequently, the multicellular organization and phenotypic plasticity of [niche] remain largely unexplored.` |
| **3. Clinical Resistance / Biomarker Failure** | **53.1%** | `Despite durable responses in a subset of patients, primary and acquired resistance limits clinical benefit in the majority of [cancer] cases.`<br>`Moreover, existing biomarkers such as PD-L1 expression fail to reliably stratify responders from non-responders.` |
| **4. Technical / Scalability Bottleneck** | **22.3%** (`52.8%` in Methods papers) | `Existing computational approaches face an inherent trade-off between [resolution/accuracy] and [scalability/cost], hindering application to large clinical cohorts.`<br>`However, current methods rely on [limiting assumption] and cannot jointly model [modality A] and [modality B].` |
| **5. Paradox / Contradictory Prior Evidence** | **1.8%** *(ultra-high prestige!)* | `Paradoxically, while [X] has been linked to [pro-tumor effect] in [context A], other studies report [anti-tumor effect] in [context B], raising the question of what dictates its context-dependent function.` |

---

## 4. Strict Three-Tense Discipline in Introduction

Empirical tense split across `1,395` 2025–2026 Introductions: **Present `54.6%`** | **Past `30.9%`** | **Present Perfect `14.5%`**.

| Tense | Mandatory Use Cases | Authentic Examples |
| :--- | :--- | :--- |
| **Simple Present (`54.6%`)** | Established scientific consensus, disease epidemiology, general biological functions, stating the current Gap, and stating enduring aims/conclusions | `PDAC is one of the most lethal malignancies...`<br>`The tumour microenvironment plays a pivotal role in...`<br>`However, the precise role of astrocytes in GBM remains unknown.` |
| **Present Perfect (`14.5%`)** | Accumulating research trends up to the present, ongoing controversies, and negative knowledge gaps | `Single-cell technologies have revealed extensive heterogeneity...`<br>`Immune checkpoint inhibitors have transformed the treatment of...`<br>`It has not yet been determined whether...` |
| **Simple Past (`30.9%`)** | Specific prior experimental findings (especially author-as-subject), refuted hypotheses, and **your own completed experimental/analytical actions** in the final paragraph | `Previous studies showed that loss of X sensitized...`<br>`Here, we integrated scRNA-seq and spatial profiling of 114 tumours and identified...` |

---

## 5. High-Frequency Introduction Cohesion & Transition Corpus

| Function | Ranked Authentic CNS Stems (`n = 1,395`) |
| :--- | :--- |
| **Macro → Micro Transition** | `Within this ecosystem, ...` / `Among these subsets, ...` / `In particular, ...` / `Beyond tumour-cell-intrinsic factors, ...` / `A defining feature of [disease] is ...` |
| **Gap Pivot (Top Ranked)** | `However,` (`888`), `Although ...` (`263`), `Despite ...` (`220`), `Nevertheless,` (`54`), `Yet ...` (`37`), `Whereas ...` (`27`), `Unfortunately,` (`22`), `Nonetheless,` (`18`) |
| **Gap Predicate (Top Ranked)** | `remains unclear` (`157`), `remain(s) poorly understood` (`91`), `remains unknown` (`65`), `remains limited` (`60`), `remain(s) elusive` (`50`), `remains challenging` (`36`), `little is known about` (`29`), `not well understood` (`22`), `poorly characterized` (`16`), `remains to be elucidated/determined` (`19`) |
| **Approach & Preview Opener** | `Here, we show/report/present/identify/demonstrate...` (#1 in *Nature/Cell*)<br>`In this study, we developed/integrated/investigated/profiled...`<br>`To address this gap / challenge, we leveraged...`<br>`To elucidate how [X] governs [Y], we combined...` |
| **Closing Grounded Value** | `Together, these insights provide a mechanistic rationale for targeting [X] in [cancer].`<br>`This atlas serves as a foundational resource for dissecting [process] and guiding patient stratification.` |

---

## 6. Five High-Frequency Introduction Traps & 10-Point Audit Checklist

### Traps to Eliminate Immediately
1. ❌ **Macro-era throat-clearing**: `"With the rapid development of high-throughput sequencing technology in the 21st century..."` → Start directly with the biological/clinical entity!
2. ❌ **Author-by-author laundry list**: `"Smith et al. (2021) found A. Jones et al. (2022) reported B. Wang et al. (2023) observed C."` → Group by mechanism/theme and put citations at sentence end (`"Recent studies have linked TAMs to immune exclusion through metabolic competition and ECM remodeling¹⁻³."`).
3. ❌ **Citation stuffing**: Avoid dumping `[1–15]` behind one trivial truism; select 2–4 seminal, targeted references per claim.
4. ❌ **Method before Question**: Never introduce `"We performed scRNA-seq on 30 samples"` before clearly stating the Gap and Scientific Question!
5. ❌ **Fake "Few Studies" Gap**: Replace `"Few studies have investigated gene X in HCC"` with a causal/spatial/clinical contradiction.

### 10-Point Pre-Submission Introduction Check
- [ ] Word count matches journal target (`Nature` ~350–450w; `Cell/Cancer Cell` ~450–600w)?
- [ ] First sentence hooks a broad biomedical reader without niche acronyms?
- [ ] Every biological concept introduced in P2–P3 directly pays off in Results (zero orphan background)?
- [ ] Literature synthesized thematically (not author-by-author)?
- [ ] Gap is concrete (mechanistic / spatial / clinical / technical / paradoxical) — zero `"few studies"`?
- [ ] Scientific question / hypothesis appears **before** experimental approach?
- [ ] Final paragraph uses active `We` (`Here, we...` / `In this study, we...`)?
- [ ] Zero Methods-level experimental details (reagents, buffer molarities, R package versions)?
- [ ] Three-tense rules obeyed (Present for consensus/gap, Present Perfect for accumulated trends, Past for specific prior experiments & our completed workflow)?
- [ ] Closing sentence grounds significance in a specific biological/clinical outcome (not empty `"advances the field"`)?
