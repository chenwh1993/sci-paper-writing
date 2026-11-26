# CNS Prose Realism, Statistical Restraint, Median-Bullseye Calibration & Cross-Rule Harmonization (`n = 1,436` Published 2025–2026 High-IF Papers)

> **Purpose**: Eliminate the exact "AI-generated manuscript" signatures that separate rigid LLM drafts from effortless, human-authored *Nature / Nature Cell Biology / Cell / Cancer Cell / Science* prose — **calibrating every stylistic metric toward the real human CNS MEDIAN (never merely hugging the redline ceiling!)** while explicitly resolving every potential conflict between competing writing rules.
>
> **Anti-Boundary-Hugging Principle**: LLMs habitually stop editing the instant a metric crosses a "safe ceiling" (e.g., leaving `3.7 P/1kw` against a `4.0` ceiling when the *Nat Cell Biol* median is `0.4`, or stopping at `CV = 0.36` when the human CNS median is `0.49`). Every table below therefore specifies **TWO tiers**:
> 1. **`Human CNS Median Bullseye`** — the active drafting & polishing target (`Median` / tight `IQR` core) you MUST aim for.
> 2. **`Hard Redline Ceiling`** — the outer boundary that triggers an automatic `[WARN]` / `[FAIL]` in `audit_manuscript.py`.

> **Corpus-First Principle (Retrieve Positive CNS Corpus FIRST — Never Whack-a-Mole Free Generation!)**: Blocking a few AI words without supplying rich positive exemplars merely pushes LLMs to coin *new* non-CNS words (`erodes`, `collars/cuffs`, `plasticity-reversing`, `biomarker-agnostic`), stack acronyms in Title/Abstract/Intro, repeat `We next / To [verb]` across 70% of Results paragraphs, or repeat `First/Second/Third` in 3 Discussion paragraphs! **ALWAYS retrieve verified verbs, prepositional 3/4-gram connectors, paragraph transitions, and sentence skeletons from [`08-comprehensive-phrasebank-and-collocations.md` Part 5 (Scenarios 19–25)](./08-comprehensive-phrasebank-and-collocations.md) FIRST** before drafting or polishing!

---

## Part 1 — The Prose vs. Figure Statistical Division of Labor (`n = 1,436` Papers)

### 1.1 Empirical `P/q`-Value Density in Published 2025–2026 High-IF Journals

Across **`1,436` published 2025–2026 high-IF oncology manuscripts**, real CNS authors **NEVER** turn Results prose into an automated statistical printout! Exact `P`/`q` values belong **on the figure plots, in Figure Captions, and in Source Data** — NOT after every clause in the main text:

| Journal (`2025–2026`) | `n` | Total `P/q` in Results — Med (IQR) | `P/q` per 1,000w — **Med** (`P90`) | **Abstract Raw `P` (%)** | **Median Bullseye Target** (`P/q` / 1kw) | Hard Redline Ceiling |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cell** | 46 | **`0.0`** (`0–4`) | **`0.0`** (`3.3`) | **`0.0%`** | **`0.0–1.0 / 1kw`** (`0–4` total) | `> 3.5 / 1kw` |
| **Immunity / Sci Immunol** | 36 | **`0.0`** (`0–1`) | **`0.0`** (`1.0`) | **`0.0%`** | **`0.0–0.8 / 1kw`** (`0–3` total) | `> 2.5 / 1kw` |
| **Cancer Cell** | 75 | **`1.0`** (`0–5`) | **`0.3`** (`6.3`) | **`0.0%`** | **`0.0–1.5 / 1kw`** (`0–6` total) | `> 6.0 / 1kw` |
| **Nat Cell Biol** | 23 | **`2.0`** (`0–7`) | **`0.4`** (`3.6`) | **`0.0%`** | **`0.0–1.5 / 1kw`** (`0–6` total) | `> 4.0 / 1kw` |
| **Nature** | 119 | **`4.0`** (`0–11`) | **`1.0`** (`5.5`) | **`0.8%`** | **`0.3–2.0 / 1kw`** (`1–8` total) | `> 5.5 / 1kw` |
| **Nat Cancer / Nat Genet** | 117 | **`5.0–6.5`** (`0–17`) | **`1.1–1.7`** (`8.4–11.2`) | `0.0–1.6%` | **`0.8–2.8 / 1kw`** (`3–11` total) | `> 8.0 / 1kw` |
| **Nat Med** *(clinical trials)* | 39 | **`10.0`** (`2–22`) | **`2.8`** (`8.6`) | `0.0%` *(trial HR/CI ok)* | **`1.5–4.5 / 1kw`** (`6–18` total) | `> 9.0 / 1kw` |
| **Sci Transl Med** | 25 | **`18.0`** (`8–31`) | **`4.7`** (`14.3`) | `0.0%` | **`3.0–6.5 / 1kw`** | `> 12.0 / 1kw` |
| **All 1,436 Papers Overall** | **1,436** | **`2.0`** (`0–8`, `P90 = 22`) | **`0.6`** (`P90 = 5.9`, `P95 = 8.6`) | **`0.3%`** | **`0.0–2.0 / 1kw`** | **HARD FAIL: `> 10 / 1kw`** |

### 1.2 Exact Division of Labor & Flexible All-Metric Restraint (`n`, `ρ`, `AUC`, `HR`, `OR`, `log2FC`, `NES` — `n = 1,436` Papers + `775` Abstracts!)

Reducing `P/q` alone is NOT enough if Results prose still prints `n = ...`, `ρ = ...`, `AUC = ...`, `HR = ...`, `OR = ...`, `C-index = ...`, `NES = ...`, and `log2FC = ...` after every clause (`26–30` inline stat equations per 1,000 words!) or if the Abstract crams 8–12 numbers into 6 sentences! Across **`1,436` published 2025–2026 Results** and **`775` published Abstracts**:

| Metric Density Category (`2025–2026` Published Norms) | *Cell / Immunity* Med (`P90`) | *Cancer Cell* Med (`P90`) | *Nat Commun / Nature / NCB* Med (`P90`) | *Nat Cancer / Nat Med* Med (`P90`) | **Flexible Target (By Paper Type)** |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Results Non-`P` Stat Eq (`n=`, `ρ/r=`, `AUC=`, `HR=`, `OR=`, `NES=`, `log2FC=`) `/1kw`** | **`0.0`** (`2.1–4.2`) | **`0.6`** (`4.5`) | **`2.4–3.1`** (`6.5–9.5`) | **`2.8–4.7`** (`8.8–12.5`) | Mechanistic: **`≤ 5–8/1kw`** · Multi-cohort/Clinical/AI: **`≤ 8–14/1kw`** (Warn **`> 15/1kw`**) |
| **Results `n =` inline tags `/1kw`** | **`0.0`** (`1.5–1.9`) | **`0.4`** (`4.2`) | **`1.7–3.1`** (`6.2–9.5`) | **`2.2–3.9`** (`8.8–9.6`) | State cohort size naturally **once** per module (`across 24 patients`); NEVER repeat `(n = 24)` 5×! |
| **Results `ρ/r/AUC/HR/OR/log2FC =` `/1kw`** | **`0.0`** (`0.3–0.7`) | **`0.0`** (`0.8`) | **`0.0`** (`0.0–0.9`) | **`0.0`** (`2.3–3.1`) | Keep **1 headline effect size** per major claim; move secondary `ρ/log2FC/NES/sub-AUC` lists onto figures! |
| **Abstract Quantitative Numbers (total)** | **`0.0`** (`Q75 1`, `P90 2`) | **`0.0`** (`Q75 1`, `P90 2`) | **`0.0`** (`Q75 1–2`, `P90 5–7`) | **`1.0`** (`Q75 3`, `P90 4–9`) | Mechanistic: **`0–3`** · Clinical/Atlas/AI: **`2–5`** (Warn **`≥ 7`** crammed numbers!) |
| **Abstract Stat Equations (`ρ=`, `r=`, `AUC=`, `HR=`, `n=`, `P=`)** | **`0.0`** (`100%` zero!) | **`0.0`** (`98.2%` zero!) | **`0.0`** (`99.2–100%` zero!) | **`0.0`** (`100%` zero!) | **`0`** (`≤ 1` headline `AUC`/`HR` only in clinical/AI papers; NEVER `ρ = −0.58` + `AUC = 0.90` + `P = ...`!) |

- **In the Abstract (Narrative First, Restrained Numbers!)**: Let the Abstract read as a crisp biological story, NOT a statistical table. Use **`0–3` concise scale/effect anchors** in mechanistic papers (up to **`2–5`** in multi-cohort/clinical/AI papers), with **ZERO inline correlation/P equations (`ρ =`, `P =`)** (`98.2–100%` of real CNS Abstracts contain zero stat equations; reserve Abstract `P`/HR strictly for randomized clinical-trial primary endpoints in *Nat Med / Clin Cancer Res*).
- **In Results Prose (Flexible Restraint — Not Mechanical Deletion!)**:
  1. **State direction + biology first, plus ONLY 1 headline number where it genuinely changes clinical/biological meaning** (primary clinical `AUC`, primary multivariable `HR`, decisive *in vivo* `%` regression).
  2. **Avoid `(n = 24)` / `(n = 39)` tag spam**: write `"across 24 baseline patients"` once when introducing the cohort; do not repeat `(n = 24)` on every subsequent correlation in the same subsection!
  3. **Offload secondary `ρ`, `log2FC`, `NES`, `ARI`, and per-subgroup `AUC` arrays onto Figure panels & Captions** — write *"inversely correlated with malignant ERBB2 across all three external bulk cohorts (Fig. 1i)"* rather than listing four `ρ =` values inline!
  4. **Reserve inline `P` values ONLY for the top `2–6` decisive claims** (primary survival / multivariable Cox / biomarker × treatment interaction / decisive *in vivo* synergy).
- **In Figure Panels, Captions & Source Data**: Put **100% of exact two-sided `P`/`q` values, `n`, `ρ`/`r`, `AUC`, `HR (95% CI)`, test names, and Source Data tables** here — complete statistical rigor with effortless human-grade prose!

### 1.3 Per-Journal Section Length (Raw vs Paren-Stripped Pure Prose), Parenthesis Budget & Default `~6,000`-Word Standard (`n = 1,436` Papers)

**The Parenthesis Hollow-Out Trap**: When LLM drafts cram 150–200 stat-heavy parentheses into Results, **`22%–28%` of the entire Results word count sits inside `(...)`** (vs only **`10.1%–16.8%`** in real published CNS papers!). Once bloated inline stats are moved to figures and captions, an apparently "3,300-word" Results section collapses to only `~2,450` words of pure narrative prose — far below published high-IF norms! Always calibrate **BOTH raw word count AND parenthesis-stripped pure-prose word count**, strictly **by target journal** (or default to **`general` = `~6,000` words Main Text** when no target journal is set!):

| Target Journal (`audit --journal`) | Main Text Raw Target (**Pure-Prose Floor**) | Abstract Cap | Intro Med (Pure) | Results Med → **Pure Prose** (`%` in `()`) | Disc Med (Pure) | Results `()` `/1kw` (Med / Warn) | Non-Fig Num `()` `/1kw` (Med / Warn) | `≥3` Parens/Sent (Med / Warn) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`general`** *(no target journal — default!)* | **`~6,000w`** (`5,200–6,800`; **Pure `≥4,600w`**) | **`≤150w`** | **`620w`** (`~600`) | **`4,200w → 3,650w`** (`13.2%`) | **`1,100w`** (`~1,060`) | `37.4 / 48` | `4.0 / 12` | `7.5% / 16%` |
| **`nature`** (`n = 119`) | **`~5,430w`** (`4,500–6,200`; **Pure `≥3,950w`**) | `~200w` (`≤215`) | `401w` (`388`) | `4,293w → 3,581w` (`16.8%`) | `645w` (`634`) | `40.3 / 50` | `3.5 / 10` | `8.8% / 16%` |
| **`nat_cell_biol`** (`n = 23`) | **`~5,710w`** (`4,700–6,600`; **Pure `≥4,150w`**) | **`≤150w`** | `511w` (`506`) | `4,278w → 3,471w` (`14.5%`) | `930w` (`905`) | `40.9 / 52` | `4.1 / 11` | `7.9% / 16%` |
| **`nat_commun`** (`n = 180`) | **`~6,110w`** (`5,100–7,300`; **Pure `≥4,550w`**) | **`≤150w`** | **`723w`** (`706`) | **`4,299w → 3,698w`** (`12.4%`) | **`1,283w`** (`1,240`) | `35.8 / 46` | `4.2 / 12` | `7.1% / 16%` |
| **`nat_cancer`** (`n = 55`) | **`~5,610w`** (`4,600–6,600`; **Pure `≥4,000w`**) | **`≤150w`** | `516w` (`471`) | `4,152w → 3,483w` (`15.2%`) | `943w` (`919`) | `39.6 / 52` | `5.6 / 16` | `8.8% / 18%` |
| **`nat_med`** (`n = 39`, clinical) | **`~5,260w`** (`4,100–6,400`; **Pure `≥3,550w`**) | `~200w` (`≤225`) | `475w` (`377`) | `3,523w → 2,820w` (`19.5%`) | `1,255w` (`1,209`) | `47.1 / 56` | `11.8 / 22` | `14.9% / 22%` |
| **`nat_methods`** (`n = 42`) | **`~5,280w`** (`4,300–6,300`; **Pure `≥4,000w`**) | **`≤150w`** | `656w` (`645`) | `3,752w → 3,340w` (`11.0%`) | `590w` (`587`) | `31.0 / 42` | `2.2 / 8` | `4.8% / 12%` |
| **`cell`** (`n = 46`) | **`~5,400w`** (`4,500–6,400`; **Pure `≥4,150w`**) | **`≤150w`** | `533w` (`524`) | `3,852w → 3,420w` (`11.9%`) | `984w` (`970`) | `39.2 / 48` | `1.8 / 7` | `8.5% / 17%` |
| **`cancer_cell`** (`n = 75`) | **`~4,950w`** (`4,100–5,900`; **Pure `≥3,850w`**) | **`≤150w`** | `458w` (`446`) | `3,627w → 3,160w` (`12.3%`) | `866w` (`857`) | `40.1 / 50` | `2.7 / 9` | `10.3% / 17%` |
| **`immunity`** (`n = 20`) | **`~5,020w`** (`4,200–6,000`; **Pure `≥3,950w`**) | **`≤150w`** | `494w` (`472`) | `3,724w → 3,224w` (`10.1%`) | `943w` (`932`) | `36.4 / 48` | `1.6 / 7` | `6.9% / 17%` |
| **`science`** (`n = 9`) | **`~6,090w`** (`4,700–6,900`; **Pure `≥4,500w`**) | **`≤125w`** | `456w` (`425`) | `4,874w → 4,322w` (`12.6%`) | `786w` (`743`) | `37.6 / 50` | `1.9 / 7` | `6.3% / 14%` |

- **Empirical Parenthesis Composition Law (`n = 1,436` Papers)**: In published high-IF Results, **`~48%` of non-figure parentheses are brief acronym definitions** (e.g., `(TME)`, `(CAFs)`), `~16%` are concise clarifications/examples (`(such as ...)`), and **only `1.6–5.6/1kw`** (except clinical *Nat Med* `11.8/1kw`) are standalone numeric/stat blocks! Never invert this ratio into `15–30/1kw` stacked stat parentheses, and never pack `≥ 3` parenthetical blocks into `> 15%` of Results sentences!
- **Per-Subheading Citation Hygiene**: In `85.3%` of published CNS Results subheadings, every `≥ 250w` subsection anchors `≥ 1` inline reference (named tools, published signatures, external cohorts, assay models, or prior concordance) — never leave an entire Results subsection with `0` citations!

---

## Part 2 — Sentence Rhythm, Burstiness & Anti-AI Punctuation Median Bullseyes (`n = 1,350` Papers)

LLMs either pack 3–5 clauses into suffocating 60–140 word walls OR over-correct into robotic "metronome prose" where every sentence is 26–30 words (`CV ≈ 0.32`). Aim directly for the **Human CNS Median Bullseye**:

| Stylistic / Structural Metric | Published 2025–2026 **Median** (IQR) | **Median Bullseye Target** | Hard Ceiling / Floor | Concrete Fix When Off-Median |
| :--- | :---: | :---: | :---: | :--- |
| **Results mean sentence length** | **`27.7`w** (`25.2–30.0`) | **`25–29` words** | `22–34`w | Split compound chains into `1 claim + 1 figure/ref` |
| **Sentence-length Burstiness (`CV = SD/Mean`)** | **`0.49`** (`0.41–0.55`) | **`0.44–0.55`** | **`≥ 0.40`** (Warn `< 0.36`) | Interleave `1` crisp `10–17w` sentence every `3–4` sentences (see [`08` Scenario 13](./08-comprehensive-phrasebank-and-collocations.md)) |
| **Short crisp sentences (`≤ 18` words)** | **`23.1%`** (`18–29%`) | **`20–28%`** | `≥ 18%` | Turn topic pivots, null controls & single readouts into punchy `10–17w` sentences |
| **Monster sentences (`> 40` words)** | **`12.2%`** (`8.1–18.0%`) | **`8–15%`** | `≤ 20%` | Break at semicolons, `whereas`, `while`, `and` |
| **Ultra-monster sentences (`> 55` words)** | **`2.7%`** (`1.1–4.9%`) | **`0–3%`** | `≤ 5%` (ZERO `> 75`w) | Never stack 3 cohorts/assays into one sentence |
| **Results median paragraph length** | **`139`w** (`108–177`) | **`120–165` words** | `100–190`w | Split 230w+ walls into 2 clean logical paragraphs |
| **Discussion total word count** | **`999`w** (`745–1,280`; *NCB* `913`) | **`880–1,150`w** (*Nature* `700–850`) | `≥ 720`w (*Nature* `≥ 550`) | Balance conceptual model, literature comparison & concise caveats |
| **Em-dashes (`—`) per 1,000w** | **`0.0`** (`0.0–0.4`) | **`0.0–0.3 / 1kw`** (`0–1` total!) | `≤ 1.0 / 1kw` | Replace `—...—` pairs with commas or a crisp period |
| **Prose semicolons (`;`) OUTSIDE `(...)` / 1kw** | **`2.4`** (`1.1–4.9`) | **`1.0–4.0 / 1kw`** | `≤ 6.0 / 1kw` | Keep `1–3` crisp contrasts/1kw; **ALWAYS keep `;` inside `(n = 39; Fig. 3f)` in *Nature***! |
| **Colons (`:`) in prose per 1,000w** | **`0.7`** (`0.3–1.5`) | **`0.3–1.2 / 1kw`** | `≤ 2.0 / 1kw` | Avoid dramatic `colon: list` reveals in prose |
| **Nested brackets `[...]` inside `(...)`** | **`0.0`** (`0.0–0.4`) | **`0`** | `≤ 1` | Move nested subgroup counts to tables or separate clauses |
| **Parentheticals `(...)` in Results / 1kw** | **`37.5`** (`32.2–43.2`) | **`32–42 / 1kw`** | `≤ 48 / 1kw` | Move inline stat parentheses onto figures |
| **Subheading `Together/Collectively` close** | **`48.6%`** of subheadings | **`45–55%`** | `35–65%` | Half explicit synthesis close, half crisp empirical readout |
| **Editorializing / AI-drama adverbs** | **`3.8 / 1kw`** (`2.6–5.4`) | **`≤ 1×` per word** | Max `2×` per paper | Delete `crucially/critically/strikingly/parsimonious/remarkably` bloat |

---

## Part 3 — Banning Notebook/Code Jargon, Defensive Audit Logs & Alien Lexicon (`Median = 0.0`)

Across `1,350` published 2025–2026 high-IF papers, **internal code/sample IDs, defensive Kaggle-style QC logs, invented 3-part hyphen stacks, and tech-blog metaphors ALL have a published median of `0.0` (`P90 = 0.0`) in Main Results!**

### 3.1 Internal Pipeline / Sample-ID Jargon Translation Table

| NEVER Write in Main Results Prose (Notebook Leak!) | Write This in Clean CNS Biological Prose Instead | Where Internal Detail Actually Belongs |
| :--- | :--- | :--- |
| `PipeV2_DropAll phenotyping framework` | `a stringent single-cell phenotyping framework` | **Methods** (full parameters & thresholds) |
| `c02_Fib_POSTN`, `c04_Fib_COL14A1`, `m01_Macro_SPP1` | `*POSTN*+` and `*COL14A1*+` fibroblasts and `*SPP1*+` macrophages | **Supplementary Table** / Extended Data heatmap |
| `Primary40`, `ValSet15`, `CohortB28`, `v2 slides` | `the discovery cohort (n = 40)`, `the independent validation cohort (n = 15)` | **Methods** & Supplementary Table 1 |
| `pt12`, `pt34`, `S08-pre`, `P19-post` | `a representative responder`, `a non-responder` *(keep sample IDs in caption/Source Data only!)* | **Figure Captions** & Supplementary Table 1 |
| `MalignantGate`, `Model_L2`, `Ensemble-5`, `Feat1 + Feat2`, `mIHC Panel B` | `copy-number-gated malignant spots`, `calibrated histological features`, `the two-feature spatial score` | **Methods** & Figure legends *(synced 1:1 with Main Text!)* |

### 3.2 Separating Biological Specificity (`P4`) From Defensive QC / Audit Prose
- **NEVER write defensive rebuttal-log phrases in Main Results**: ban *"without outcome-label leakage"*, *"outcome-blind"*, *"zero-outcome-peeking"*, *"strictly quarantined"*, *"adversarial removal of top-contributing patients"*, *"fragile antibodies excluded"*, *"guarding against technical batch structure (P = 0.614)"*, *"bidirectional rescue disabled"*, *"honest optical blind spot"*, *"zero negative penalty"*.
- **DO write 1 clean biological specificity sentence in Results** (preserving full `P4` rigor without sounding defensive!):
  - *Before (Defensive + Jargon + Stat Dump, 94w)*: `"To define higher-order tissue architecture without outcome-label leakage, we conducted an unsupervised stability sweep across 81 physical radius and cluster combinations (r = 20–150 μm × K = 5–13)... exhaustive 40-patient LOPO resampling and adversarial removal of top-contributing patients. Only K = 8 satisfied all six stability gates (ARI = 0.96 ± 0.01, LOPO ARI = 0.99, cosine ≥ 0.995)..."`
  - *After (Effortless Nat Cell Biol Prose, 33w)*: `"Unsupervised spatial neighbourhood analysis across all baseline tissues resolved eight reproducible cellular neighbourhoods (CN1–CN8) at a 40-μm radius, separating tumour, vascular, stromal, lymphoid and myeloid niches (Fig. 2h; Extended Data Fig. 3b–d)."` *(All parameter sweeps, ARI values, and leave-one-out stability checks live cleanly in **Methods** + **Extended Data Fig. 3b–d**!)*

### 3.3 Empirical CNS Phraseological Grounding & Anti-Alien-Lexicon Law (`n = 1,312` Reference Papers vs `30` Held-Out Human CNS Papers)

Even when 30 real published *Nature / Cell / Cancer Cell / Nat Cell Biol / Immunity* papers investigate completely different cancers and molecules, their **de-lexicalized sentence skeletons, academic phrasing frames, and vocabulary** remain remarkably consistent across the genre:

| Idiomaticity Benchmark (vs `1,312` Published 2025–2026 CNS Papers) | Real Human CNS **Median** (`IQR`) `[Min–Max]` | **Median Bullseye Target** | Hard Floor |
| :--- | :---: | :---: | :---: |
| **De-lexicalized 2-gram Phraseological Grounding** (`df ≥ 3`) | **`76.0%`** (`71.4–78.4%`) `[54.0–81.2%]` | **`72–78%`** | `≥ 65%` |
| **De-lexicalized 3-gram Phraseological Grounding** (`df ≥ 2`) | **`46.5%`** (`39.8–51.0%`) `[19.2–53.5%]` | **`42–50%`** | `≥ 35%` |
| **Sentence 2-Word Opener Grammar Grounded** (`df ≥ 3`) | **`73.8%`** (`68.0–78.8%`) `[38.6–82.0%]` | **`70–78%`** | `≥ 65%` |
| **100% Pure-CNS-Vocabulary Sentences (`0` rare/alien words)** | **`52.0%`** (`37.9–60.7%`) `[25.0–86.5%]` | **`48–60%`** | `≥ 40%` |

**The Three Linguistic Habits That Separate `50%` AI Grounding From the `76%` Human CNS Median**:
1. **Unpack Invented 3-Part AND AI-Tell 2-Part Compound Modifier Stacks (`0.00%` in `1,312` CNS papers!)**:
   - LLMs compress clauses into compound stacks like *"marker-stability-tiered spatial features"*, *"copy-number-confirmed"*, *"outcome-blind tile-level"*, *"out-of-fold"*, *"two-feature composite"*, *"same-section"*, *"single-marker"*, *"batch-matched"*, *"multi-compartment"*, *"macro-architectural"*, *"within-batch"*, *"per-slide"*.
   - **CNS Fix**: Unpack into plain prepositional English (`of`, `by`, `for`, `across`, `within` — full 22-row unpacking dictionary in [`08-comprehensive-phrasebank-and-collocations.md` §18.2](./08-comprehensive-phrasebank-and-collocations.md)).
2. **Replace Non-CNS Tech-Blog / Editorializing / Metaphor Lexicon (`< 0.5%` in `1,312` CNS papers!) With Plain CNS Equivalents**:

| Non-CNS / LLM-Register Word (`< 0.5%` of `1,312` Papers) | Authentic High-Frequency CNS Replacement |
| :--- | :--- |
| `audit` / `audited` / `rigorous audit` (`0.0%`) | `analysis` / `evaluated` / `assessed` / `examined` |
| `quarantined` (cohort, `0.0%`) | `held-out` / `independent validation` |
| `obliterates` (`0.0%`) | `disrupts` / `eliminates` / `abolishes` |
| `crosswalk against` (`0.0%`) | `comparison with` / `mapping onto` |
| `capitalising on` / `division of labour` (`0.0%`) | `combining` / `integrating` / `complementary roles` |
| `honest blind spot` / `over-optimistic assumption` (`0.0%`) | `limited ability to distinguish` / `prevailing assumption` |
| `upgraded clinical stratification` (`0.0%`) | `improved clinical stratification` / `enhanced risk stratification` |
| `locked atlas` / `phase cliff` (`0.0%`) | `consensus atlas` / `sharp decline` |
| `parsimonious` (`< 0.4%`) | `compact` / `minimal` / `two-feature` |
| `habitats` / `portals` / `descriptors` / `triage cascade` (`0.15–0.46%`) | `niches` / `compartments` / `features` / `two-step stratification` |
| `cleanly` (`0.38%`) / `decodes` (`< 0.5%`) | `distinctly` or `clearly` / `predicts` or `infers` |
| `out-of-fold` (`< 0.1%`) / `zero-shot` (`< 0.2%`) | `cross-validated` / `pretrained` (specify zero-shot once in Methods) |

3. **Flexible Sentence-Opener Discipline & Anti-Consecutive Bare-NP-Subject Rule**:
   - **Be flexible on domain terminology**: NEVER strip authentic study-specific terms (`protease sleeve`, `snFFPE-seq`, `urothelial`, drug/assay names) merely to chase a blind corpus 2-gram score!
   - **DO eliminate the real unnatural AI syntax habit — consecutive bare article-less noun-phrase openings**: LLMs compress Results into 5–8 consecutive executive headlines lacking human subjects or articles (*"Serial clinical pelvic MRI illustrated... Pretreatment covariates were... Routine IHC failed... Copy-number inference identified... Unbiased consensus NMF recovered... Continuous plasticity tracked..."*).
   - **Human CNS Fix**: Across every Results module, open **`20–40%`** of sentences with active human voice (`We next...`, `Using [Tool], we identified...`, `To determine whether..., we...`), mix in natural article/bridge openings (`The...`, `Consistent with...`, `In contrast to...`, `These findings suggest...`), **never chain `≥ 4–5` consecutive bare nominalized noun-phrase openings**, and split `> 55w` paragraph-opening wall sentences (`≤ 3% > 55w`, median `2.7%`) into crisp 2-sentence pairs (`Method/cohort` → `Key finding`)! See [`08-comprehensive-phrasebank-and-collocations.md` §Part 2 & §18.1](./08-comprehensive-phrasebank-and-collocations.md).

### 3.4 Zone-by-Zone Concrete Before (AI-Tell) → After (Human CNS Median) Rewrite Gallery

Use these verified side-by-side transformations (paired with the `550`-paper verbatim corpus in [`08-comprehensive-phrasebank-and-collocations.md` §Part 4](./08-comprehensive-phrasebank-and-collocations.md)) whenever polishing drafts from "safe zone" up to the **real human CNS median**:

#### Zone 1 — Discussion & Introduction Rhetoric (Lifting Opener Grounding `36% → 74%`)
- **Before (AI-Tell — nominalized opener + metaphors + em-dash)**: `"Capitalising on this complementary division of labour—where macro-architectural histology decodes stromal exclusion while multiplex spatial profiling resolves target habitats—our study establishes a parsimonious triage cascade that obliterates the over-optimistic assumption of single-metric scoring."`
- **After (Human CNS Median — crisp 2-sentence burstiness + plain CNS verbs)**: `"In this study, we show that routine H&E histology and multiplex spatial profiling capture complementary determinants of treatment response. Whereas histology reflects macroscopic stromal architecture, spatial profiling resolves cellular niches that cannot be distinguished by conventional single-marker scoring alone."` *(16w + 22w; 0 alien words; 0 em-dashes; 100% CNS opener grounding!)*

#### Zone 2 — Results Spatial & Computational Pathology Blocks (Eliminating Hyphen Stacks + Defensive QC)
- **Before (AI-Tell — 3-part hyphen stacks + Kaggle audit prose)**: `"To perform an outcome-blind crosswalk without outcome-label leakage, we evaluated zero-shot foundation-model embeddings on same-section H&E slides and observed an honest optical blind spot when distinguishing marker-stability-tiered target-to-vascular geometry across batch-matched discovery and strictly quarantined validation cohorts (AUC = 0.89, P = 0.0004, Fig. 4b)."`
- **After (Human CNS Median — short-long rhythm + plain prepositional English + Nature `;`)**: `"We next evaluated whether pretrained pathology foundation models applied to matched H&E slides could predict treatment response. Although histology alone stratified stromal architecture across discovery and independent validation cohorts (AUC = 0.89; Fig. 4b), H&E morphology was not sufficient to resolve spatial proximity between target-expressing cells and vessels (Extended Data Fig. 6a)."` *(18w + 35w -> natural `CV`; 0 defensive logs; 0 hyphen stacks; exact `;` before `Fig. 4b`!)*

#### Zone 3 — Results Statistical Restraint & Burstiness (Pulling `P/q` From `3.7/1kw` → `0.5–1.5/1kw` & `CV` From `0.32` → `0.49`)
- **Before (AI-Tell — metronome 27w sentences + routine inline `P` values + comma before `Fig.`)**: `"Malignant cell abundance did not differ significantly between complete responders and non-responders across the baseline cohort (P = 0.642, Fig. 1d). Baseline clinical covariates including age (P = 0.991), tumour stage (P = 0.257) and histological grade (P = 0.443) similarly showed no association with pathological response (Extended Data Fig. 1b). Conversely, baseline effector T-cell density was markedly elevated in responding tumours compared with non-responding tumours (2.4-fold, P = 0.004, Fig. 1e)."`
- **After (Human CNS Median — `13w + 15w + 26w` burstiness + `0` routine inline `P` + Nature `;`)**: `"Baseline malignant cell abundance did not differ between responders and non-responders (Fig. 1d). Clinical covariates, including age, stage and grade, were similarly balanced between groups (Extended Data Fig. 1b). By contrast, effector T cell infiltration was 2.4-fold higher in responding tumours and independently predicted prolonged disease-free survival in multivariable Cox analysis (HR = 0.26, P = 0.004; Fig. 1e,f)."` *(Only the single decisive multivariable Cox `P` stays in prose; all routine `P`/`n`/tests sit cleanly on the panels and captions!)*

#### Zone 4 — Methods & Legend Format Purity (*Nature* vs *Cell Press*)
- **Before (AI-Tell — format cross-contamination + vague scale bar + broken Markdown)**: `"Primary antibodies are listed in the Key Resources Table [Supplier, Cat#]. Representative H&E and mIF images (white scale bar embedded at lower right); **q* < 0.01."`
- **After (Clean *Nature* Portfolio Standard)**: `"Primary antibodies, dilutions and RRIDs are provided in Supplementary Table 2. Representative H&E and multiplex immunofluorescence images (n = 3 independent tumours per group; scale bars, 100 µm); two-sided Wilcoxon rank-sum test with Benjamini–Hochberg correction (q < 0.01)."`

---

## Part 4 — Citation Hygiene, Sequential Order, Methods Citations & Format Purity

1. **Strict Sequential Citation Numbering (`1, 2, 3, ..., N`)**: In numbered-reference journals (*Nature* Portfolio, *Science*), citations MUST appear in **strict sequential order of first appearance** across `Introduction → Results → Discussion`, followed by `Methods`-only references (`N+1..M`). NEVER jump from ref `19` to ref `43`!
2. **Zero Orphan References (`listed − cited = 0`) & Zero Missing Citations (`cited − listed = 0`)**: Every single entry in `# References` MUST be cited in the manuscript body, and every citation number in the body MUST appear in `# References`.
3. **Every Named External Dataset, Clinical Trial, Signature & Tool in Results AND Methods Must Be Cited**: Never name public datasets or tools (`TCGA`, `GEO`, `DepMap`, `PRISM`, `GDSC2`, `Seurat`, `Scanpy`, `Harmony`, `UCell`, `edgeR`, `RCTD`, `CellChat`, `UNI`, `CONCH`) without an inline reference. In *Nature* Portfolio papers, **`32.4%` of all citations (`~15–27` refs)** belong inside **Methods** (citing every software package, genome/database, and assay protocol) — NEVER submit a 4,000-word *Nature* Methods section with only 1 citation!
4. **Zero Journal-Format Cross-Contamination & Strict Main-Text ↔ Figure ↔ Legend Sync**:
   - **Never mix Cell Press `STAR Key Resources Table` into *Nature* Portfolio Methods** (in *Nature / NCB / Nat Cancer*, use the **Nature Portfolio Reporting Summary** and put antibody RRIDs & primer sequences in a **Supplementary Table**, never referencing `"listed in the Key Resources Table"`!).
   - **Never scrub a model/cohort label out of Main Text while leaving it on Figure Legends & Axes** (e.g., calling it `"the two-feature spatial score"` in Results while Fig. 3i and its Legend say `Model_V1` and `Feat_A + Feat_B`!). Either clean internal code names across **ALL THREE** (`Main Text + Legends + Figures`), OR define clean human shorthand once on first mention in Main Text (`"a two-feature spatial score (Model A; Fig. 3i)"`).
   - **Exact Physical Scale Bars Everywhere (Zero Phantom Claims!) & 100% Plot-Axis / Schematic ↔ Text/Legend Cross-Check**: Every MRI, H&E, IHC, and mIF legend MUST state an exact numeric scale bar (`Scale bar, 100 µm` or `Scale bar, 1 cm`) **ONLY WHEN that calibrated scale bar is physically drawn and visibly verified on the image** (if raw MRI lacks a drawn bar, either stamp a calibrated vector bar or report exact FOV dimensions — NEVER claim a phantom scale bar!). Cross-verify **100%** of (a) numerical metrics (`µm`, `AUC`, `HR`, `P`, `n`, gene/cell labels) printed inside schematics against data panels, AND (b) **statistical metric types (`Spearman ρ` vs group difference `Δ` vs `OR`/`HR` vs `AUC`) and sample sizes `n`** printed on EVERY rendered Main & Supplementary plot axis against both the Results prose and Figure Legends (preventing plot-vs-legend drift after figure revisions!). Avoid Markdown star collisions (`**q* < 0.01` breaks rendering; escape `\*` or write `q < 0.01`).

---

## Part 5 — Master Cross-Skill Conflict-Resolution Matrix (17 Pairs — Zero Rule Collisions!)

Whenever two writing rules appear to pull in opposite directions, ALWAYS apply these exact precedence resolutions:

| Rule A | Potential Tension With Rule B | **Exact Conflict-Free Resolution** |
| :--- | :--- | :--- |
| **1. Abstract quantitative anchors** (`01`) | **Abstract numeric & stat-equation restraint (`98.2%` zero stat equations!)** (`14`) | Keep **`0–3` crisp scale/effect numbers** in mechanistic Abstracts (up to **`2–5`** in clinical/AI Abstracts) and **ZERO inline `ρ = / r = / P =` equations** (`≤ 1` headline `AUC`/`HR` only in clinical/AI papers; reserve `P` for *Nat Med* trial primary endpoints). |
| **2. Statistical rigor (`P`, `n`, FDR, two-sided)** (`06`, `07`) | **Median-bullseye Results `P/q` (`0.0–2.0/1kw`)** (`14`) | Put **100% of exact `P/q`, `n`, test names, and CIs** on Figures, Captions, and Source Data; reserve prose `P` strictly for the top `2–6` decisive primary survival, multivariable Cox/interaction, and *in vivo* efficacy endpoints. |
| **3. `P4` Specificity & alternative-hypothesis disproof** (`13`) | **No defensive QC/audit/leakage prose in Results** (`14`) | State the **biological specificity conclusion** in 1 crisp Results sentence (`remained predictive after adjusting for stage and PD-L1`); place all parameter sweeps, batch checks, patient exclusions, and thresholds in **Methods + Extended Data**. |
| **4. `55–68` Main-Text unique refs + `3–5`/subheading** (`09`) | **Concise `25–29w` sentences & `1–3` anti-stuffing** (`09`, `14`) | Cite each named tool, signature, cohort, or trial inline (`1–2` refs) inside short 1-claim sentences across `3–4` crisp `120–165w` paragraphs per subheading — zero stuffing, zero monster sentences! |
| **5. `51.4%` subheading synthesis closures** (`03`) | **Avoid robotic LLM template repetition** (`14`) | Close **`45–55%`** of Results subheadings (3–4 of 7) with varied synthesis stems (`Together`, `Thus`, `Collectively`, `These observations`); end the remaining subheadings directly on a strong empirical finding or forward pivot. |
| **6. Tight Discussion (`~880–1,150w`, zero raw stats in P1)** (`04`) | **4-Layer Elevation + `+11–15` NEW refs + Limitations** (`04`, `09`) | Target **`880–1,150` words** (`5–6` balanced paragraphs; *Nature* `700–850w`); keep P1 stat-free, devote 2–3 paragraphs to comparative literature & translation (`+11–15` new refs), and focus Limitations on the **2–3 highest-level scope boundaries** (never a defensive 5-point laundry list). |
| **7. Strict `1-Panel = 1-Unique-Letter` (`90.4%`)** (`10`, `sci-plot`) | **Track-B high-density chart consolidation** (`11`, `sci-plot`) | Track-B helpers (`plot_multi_cluster_volcano`, `plot_split_violin`, `plot_roe_bubble_heatmap`) unify homogeneous data into **ONE single plot** (= 1 unique letter); never bundle two different chart types under one letter. |
| **8. Journal Main-Figure page caps (`5–7` Figs)** (`10`, `11`) | **Real visual Hero Space (`35–55%` of plate area)** (`10`, `sci-plot`) | Protect `1–2` flagship real-image panels per relevant Main Fig at Tier-1 priority (`93`) with generous `115–174 mm` Hero zones, and cleanly offload QC, extra patient slides, single-channel splits, and secondary cohorts to paired `ED Fig. / Fig. S`! |
| **9. Memorable biological concept naming & domain terms** (`00`, `13`) | **Flexible CNS phraseological grounding & anti-bare-NP openers** (`14`) | Preserve authentic biological/domain terms (`protease sleeve`, `snFFPE-seq`, drug names) freely without gaming n-grams; fix the real AI habit by keeping **`20–40%` active `"We..."` / `"Using..., we..."` openers**, zero `≥5` bare-NP streaks, and zero tech-blog metaphors! |
| **10. Splitting long sentences (`25–29w` mean, `≤3% >55w`)** (`14`) | **Human-median cadence burstiness (`CV 0.44–0.55`, `20–28% <= 18w`)** (`14`) | Do NOT flatten every sentence to 26–30w like a metronome! Mix punchy `10–17w` topic/finding/negative-control sentences (`20–28%`) with richer `30–40w` mechanistic sentences (splitting `>55w` paragraph-opening wall sentences into 2 crisp sentences). |
| **11. Banning notebook jargon in Main Text** (`14`) | **1:1 Text ↔ Figure ↔ Legend terminology sync** (`06`, `11`) | Never delete an abbreviation from Main Text while leaving it on Figure axes or Legends! Clean internal pipeline IDs (`PipeV2_DropAll`, `CohortA_39`, `Feat1`) across ALL deliverables, and introduce any clean human shorthand (`Model A`, `CN1–CN8`) once in Main Text on first reference. |
| **12. Median-Bullseye prose restraint (`0–2 P/1kw`, `0` em-dashes)** (`14`) | **Journal-specific clinical reporting & valid scientific compounds** (`03`, `07`, `15`) | Match the **journal-specific** Median Bullseye (*Cell/NCB* `0.0–1.5 P/1kw`, *Nature/Cancer Cell* `0.3–2.0`, *Nat Med* clinical trials `1.5–4.5`); never delete genuinely decisive survival/Cox/`in vivo` stats just to hit `0.0`, and never break established biomedical compounds (`anti-PD-1`, `non-small-cell`, `single-cell`). |
| **13. Anti-Sparse Main Plates (`≤76%` white, `KM+Risk`) vs Relaxed Supp/ED (`≤88%` white)** (`10`, `sci-plot`) | **Minimal-Text Plot Policy & Anti-Padding (`≥5 pt`, zero gridlines/fake contours)** (`sci-plot`) | Achieve Main-Figure visual substance via **real imaging anchors and genuine multi-dimensional encodings (KM + CI + Risk Table, OncoPrint, clustered heatmaps)** — NEVER by adding narrative prose boxes, background gridlines, shrinking fonts below `5 pt`, or **slapping decorative 2D KDE contour lines onto small-`n` (`<300`) scatter plots just to fill whitespace**! Keep Supplementary / Extended Data figures relaxed, clean, and unadorned (`≤88%` white, `≥50%` height OK). |
| **14. Flexible Non-`P` Metric Restraint (`n=`, `ρ=`, `AUC=`, `HR=`, `log2FC=`)** (`14`) | **Multi-cohort / clinical / AI quantitative transparency** (`03`, `09`) | State each cohort's `n` naturally **once** per module (`across 24 patients`) rather than repeating `(n = 24)`; retain ONLY 1 headline effect size (`AUC`, `HR`, `%` regression) per major claim and offload secondary `ρ`, `log2FC`, `NES`, `ARI` lists to Figure panels & Captions (target **`≤ 8–14/1kw`** in multi-cohort/AI papers, **`≤ 5–8/1kw`** in mechanistic papers). |
| **15. Multi-Figure Experimental / Mouse / Spatial Schematics (`≥2–3` Main Figs)** (`10`, `sci-plot`) | **Full-Page Millimeter Height Caps (`215–220 mm`) & Zero LLM Image Generation** (`11`, `sci-plot`) | Use **compact `22–34 mm` horizontal timeline/assay strips** (`mouse_timeline_schematic`, `cell_assay_schematic`, `spatial_workflow_schematic`) built strictly via **programmatic editable vector SVG / R `grid` / Illustrator / BioRender** (**NEVER** direct LLM/diffusion image generation for any chart, plate assembly, or schematic!) — giving instant reader comprehension while preserving full height and 100% scientific integrity! |
| **16. Trimming inline parenthetical stat dumps (`−500` to `−800w`)** (`14`) | **Meeting Target-Journal / `~6,000w` Narrative Substance (`pure-prose floor`)** (`14`, `15`) | NEVER pad deleted parenthetical stats with vague filler! Reinvest the freed word budget into authentic CNS **mechanistic explanation, biological specificity contrasts (`P4`), cohesive experimental transitions, and comparative literature triangulation (`+21–32` Results / `+11–15` Discussion refs)** so paren-stripped pure prose matches the target journal's published median (or **`~6,000w` raw / `≥4,600w` pure** under the `general` default when no journal is chosen)! |
| **17. Active human `"We"` voice (`20–40%`) & structured multi-point Discussion** (`03`, `04`, `14`) | **Avoiding `We next/then` / `To [verb]` paragraph monotony, triple `First/Second/Third` lists & front-matter alphabet soup** (`08` Part 5, `14`) | **Retrieve from the positive CNS corpus FIRST (`08` Scenarios 19–25)**: keep Title (`0–1` acronym), Abstract (`≤5–7` acr/100w, `0` internal codes like `MP4/Model A`), and Intro (`≤6–7` acr/100w) clean; in Results, rotate all **8 natural paragraph-opening families** (`We next/then ≤ 15%`, `To [verb] ≤ 25%`, raw `GSE` IDs offloaded to figures/Methods) and use natural `11–17w` sentences instead of 4-word telegraph punchlines; in Discussion, use `First/Second` in **at most ONE paragraph** and include **1–2 paragraphs of genuine epistemic mechanistic speculation (`6–10/1kw`)**! |
