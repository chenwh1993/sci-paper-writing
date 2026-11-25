# Methods & STAR★METHODS — CNS Schemas, Past-Passive Grammar & Reproducibility Corpus

> Empirically distilled from 307 complete CNS & high-impact Methods / STAR★METHODS sections. Enforces 9.89:1 past-passive dominance, exact reagent/software version traceability, IRB/IACUC/STR compliance, and permanent data/code availability disclosures.


---

## Part 1 — CNS Methods Architectures: Nature Online Methods, Cell STAR Methods & Science

Empirically calibrated from 307 complete CNS Methods sections (`135` Nature family, `106` Cell family, `56` Science family) plus official *Nature Portfolio*, *Cell Press*, and *Science/AAAS* instructions to authors.

---

### 1. Nature Portfolio Online Methods (`median 3,634 words`, `15 subheadings`)

*Nature*, *Nature Medicine*, *Nature Genetics*, *Nature Cancer*, *Nature Immunology*, *Nature Biotechnology*, *Nature Methods*, *Nature Communications*.

#### Canonical Section Order
```markdown
### Methods

#### Human participants and sample collection        # IRB, Helsinki, consent, clinical criteria, sex/age
#### Animal models and in vivo treatments          # IACUC, strain, sex/age, SPF housing, randomization, endpoint
#### Cell lines and culture conditions             # Source, media, STR authentication, mycoplasma screening
#### Tissue dissociation and flow cytometry        # Digestion, strainer, staining, gating, FlowJo
#### Single-cell RNA-seq and TCR-seq library prep  # 10x Genomics Chromium, sequencing platform, read length
#### Spatial transcriptomics / Multiplex IF / IHC  # FFPE sectioning, Visium/Xenium/mIF panels, scanning
#### Functional wet-lab assays                     # CRISPR, Western blot, RT-qPCR, ELISA, co-culture
#### Sequencing alignment and quality control      # Cell Ranger / STAR / BWA, ambient RNA, doublet removal
#### Integration, clustering and cell annotation   # Seurat/Scanpy, Harmony/scVI, Leiden, marker genes
#### Differential expression and pathway analysis  # Pseudobulk DESeq2, GSEA/fgsea, MSigDB, AUCell
#### Trajectory, cell–cell interaction and CNV     # Monocle3/scVelo, CellChat/CellPhoneDB, InferCNV
#### Spatial deconvolution and niche analysis      # RCTD/Cell2location, QuPath/HALO, proximity permutation
#### Survival analysis and predictive modelling    # Kaplan–Meier, Cox PH, LASSO/XGBoost, cross-validation
#### Statistics and reproducibility                # Sample size, blinding, normality, two-sided tests, FDR

#### Reporting summary                             # Standard Nature Portfolio link sentence
#### Data availability                             # Accession codes + controlled-access terms + Source Data
#### Code availability                             # GitHub URL + Zenodo DOI + custom script statement
```

> **Nature Spelling & Formatting**: Flagship *Nature* copyedits to British spelling (`tumour`, `analyse`, `modelling`, `normalised`, `centre`, `s.d.`, `s.e.m.`) and prefers concise subheadings without numbered prefixes. *Nature Communications* accepts consistent American or British spelling.

---

### 2. Cell Press STAR★METHODS (`median 4,928 words`, `21 subheadings`)

*Cell*, *Cancer Cell*, *Immunity*, *Cell Metabolism*, *Cell Stem Cell*, *Molecular Cell*, *Cell Genomics*, *Cell Reports*.

#### Mandatory 5-Block Schema (Exact Uppercase Major Headings)
```markdown
### STAR★METHODS

#### KEY RESOURCES TABLE
| REAGENT or RESOURCE | SOURCE | IDENTIFIER |
| :--- | :--- | :--- |
| **Antibodies** | | |
| Anti-human CD8α (clone C8/144B) | Agilent Dako | Cat# M7103; RRID: AB_2075537 |
| **Biological samples** | | |
| Human [cancer type] FFPE / fresh biopsies | [Hospital Name] | This paper (Table S1) |
| **Chemicals, peptides, and recombinant proteins** | | |
| Collagenase IV | Worthington | Cat# LS004188 |
| **Critical commercial assays** | | |
| Chromium Next GEM Single Cell 5' Kit v2 | 10x Genomics | Cat# PN-1000263 |
| **Deposited data** | | |
| Raw and processed scRNA-seq data | GEO / GSA-Human | GSEXXXXXX / HRAXXXXXX |
| **Experimental models: Cell lines** | | |
| Human: HEK293T | ATCC | Cat# CRL-3216; RRID: CVCL_0063 |
| **Experimental models: Organisms/strains** | | |
| Mouse: C57BL/6J | The Jackson Laboratory | Strain# 000664; RRID: IMSR_JAX:000664 |
| **Oligonucleotides** | | |
| sgRNA targeting [GENE]: 5'-...-3' | Integrated DNA Technologies | N/A |
| **Software and algorithms** | | |
| Seurat (v4.3.0) | Hao et al. | https://satijalab.org/seurat/; RRID: SCR_016341 |
| Analysis code for this study | This paper | https://github.com/[ORG]/[REPO] (Zenodo DOI) |

#### RESOURCE AVAILABILITY
#### Lead contact
Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, [Full Name] ([email@institution.edu]).

#### Materials availability
This study did not generate new unique reagents.
(OR: Plasmids / cell lines generated in this study are available from the lead contact with a completed materials transfer agreement.)

#### Data and code availability
- [Raw/processed sequencing data] have been deposited at [GEO / GSA-Human / EGA] under accession number [ID] and are publicly available [or: available under controlled access] as of the date of publication.
- All original code has been deposited at [GitHub / Zenodo] and is publicly available at [URL / DOI] as of the date of publication.
- Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request.

#### EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS
#### Human participants           # Updated 2023+ heading (replaced "Subject Details"); sex, age, ancestry/race, IRB
#### Mice                         # Strain, source, sex, age, SPF housing, IACUC
#### Cell lines                   # Origin, sex of cell line, culture conditions, STR & mycoplasma

#### METHOD DETAILS
#### [Assay / Computational Subsections in chronological order of Results]

#### QUANTIFICATION AND STATISTICAL ANALYSIS
## Part 1 — Exact n definitions, dispersion measures (mean ± SD/SEM), statistical tests, software, significance thresholds
```

#### Critical KRT Rules
1. **Cross-reporting**: Every single reagent, model, dataset, and software tool listed in the KRT **must** appear in `METHOD DETAILS` (and vice versa).
2. **Exclude routine consumables**: Do *not* list PBS, ethanol, standard media components, pipette tips, or basic buffers.
3. **Identifier precision**: Include catalog numbers (`Cat# ...`), RRIDs (`RRID: AB_...`, `CVCL_...`, `SCR_...`), exact software versions, and DOI/accession numbers.

---

### 3. Science / AAAS Materials and Methods (`median 2,631 words`, `15 subheadings`)

*Science*, *Science Translational Medicine*, *Science Immunology*, *Science Advances*.

#### Structural Rules
- **Flagship *Science***: Keep main-text methods to a 1–2 sentence conceptual overview inside Results; place the complete **Materials and Methods** inside the Supplementary Materials PDF (with a concise `Data and materials availability` block in the main text Acknowledgments).
- ***Science Advances* / *Sci. Transl. Med.* / *Sci. Immunol.***: Full `Materials and Methods` section included inline in the main article, opening with **`Study design`** (required by *Sci. Transl. Med.* and *Sci. Immunol.*: explicit objectives, sample size rationale, inclusion/exclusion rules, stopping criteria, randomization, and blinding!), followed by experimental & computational subsections and **`Statistical analysis`**.
- **MDAR Compliance**: Explicitly cover Materials, Design, Analysis, and Reporting (ethics, sex as a biological variable, randomization, blinding, replicates, code/data deposition).

---

## Part 2 — CNS Methods Grammar, Voice, Connectors & Academic Vocabulary Bank

Empirically distilled from **307 complete CNS & high-impact Methods / STAR Methods sections** (`35,152` past-passive verbs, `3,556` active `we` verbs, and top 4-gram idioms). Use this handbook to write natural, crisp, publication-grade Methods prose.

---

### 1. Tense & Voice Rules (`9.89 : 1` Past-Passive Rule)

| Rhetorical Context | Grammatical Tense & Voice | Empirical Basis | Authentic CNS Example |
| :--- | :--- | :--- | :--- |
| **Experimental & computational actions performed** | **Simple Past Passive** (`was/were + V-ed`) | **9.89 : 1** over active `we` (`35,152` vs `3,556`) | `Single-cell suspensions were washed twice with PBS and filtered through a 70-μm cell strainer.` |
| **Bespoke algorithmic / modeling decisions (sparingly)** | **Simple Past Active** (`we + V-ed`) | Used ~9% of the time for clear analytical rationale | `To account for inter-patient batch effects, we integrated all samples using Harmony (v1.2.0).` |
| **Mathematical definitions, cutoffs, tool defaults** | **Simple Present** (`is defined as`, `calculates`, `represents`) | States timeless mathematical/software truths | `Here, R_o/e is defined as the ratio of observed to expected cell counts.` |
| **Data & code repository archiving** | **Present Perfect** (`have been deposited`) + **Simple Present** (`are publicly available`) | Standard across *Nature* & *Cell STAR* | `Raw sequencing data have been deposited in GEO (GSEXXXXXX) and are publicly available as of publication.` |
| **Lead contact & future requests** (*Cell STAR*) | **Modal Passive** (`should be directed to and will be fulfilled by`) | Exact mandatory Cell Press phrasing (`79` hits) | `Further information and requests for resources should be directed to and will be fulfilled by the lead contact.` |

---

### 2. Top 50 Empirically Ranked Past-Passive Academic Verbs (by Workflow Stage)

Use precise domain verbs instead of repeating `used`, `did`, or `made`:

| Workflow Stage | Authentic CNS Past-Passive Verbs (`was/were + ...`) |
| :--- | :--- |
| **Cohort, Ethics & Sourcing** | `approved`, `enrolled`, `recruited`, `obtained`, `collected`, `harvested`, `archived`, `purchased`, `acquired`, `confirmed`, `staged`, `classified`, `matched`, `assigned`, `randomized` |
| **Sample Prep & Wet-Lab** | `minced`, `digested`, `dissociated`, `filtered`, `lysed`, `centrifuged`, `washed`, `resuspended`, `diluted`, `incubated`, `stained`, `fixed`, `permeabilized`, `blocked`, `mounted`, `seeded`, `cultured`, `maintained`, `treated`, `stimulated`, `transduced`, `transfected`, `sorted`, `purified`, `extracted`, `eluted`, `quantified`, `prepared`, `stored`, `injected`, `implanted`, `monitored`, `euthanized` |
| **Sequencing & Preprocessing** | `constructed`, `encapsulated`, `amplified`, `sequenced`, `demultiplexed`, `trimmed`, `aligned`, `mapped`, `counted`, `retained`, `excluded`, `removed`, `discarded`, `corrected`, `decontaminated`, `normalized`, `log-transformed`, `scaled`, `integrated` |
| **Bioinformatics & Modeling** | `selected`, `reduced`, `projected`, `clustered`, `annotated`, `identified`, `inferred`, `scored`, `deconvolved`, `imputed`, `estimated`, `predicted`, `trained`, `validated`, `benchmarked`, `evaluated`, `ranked`, `visualized` |
| **Statistics & Reporting** | `performed`, `conducted`, `carried out`, `calculated`, `computed`, `determined`, `assessed`, `compared`, `tested`, `adjusted`, `controlled`, `stratified`, `modeled`, `defined`, `considered`, `summarized`, `deposited`, `archived` |

---

### 3. High-Frequency Procedural Connectors & CNS Academic Idioms

Empirically ranked by document prevalence across 307 CNS Methods sections:

| Function | Authentic CNS Phrasing (`Document %`) | Usage Example |
| :--- | :--- | :--- |
| **Paired/parallel values** | `..., respectively` (`71.0%`) | `Cells with < 500 or > 6,000 detected genes were excluded, respectively.` |
| **Opening with purpose (Best transition!)** | `To [assess / evaluate / determine / identify / quantify / validate] ...,` (`66.1%`) | `To evaluate the prognostic value of the signature, multivariable Cox regression was performed.` |
| **Mitigating confounders / QC** | `To [account for / minimize / eliminate / correct for / remove] ...,` (`34.2%`) | `To minimize ambient RNA contamination, raw count matrices were processed with SoupX (v1.6.2).` |
| **Condensing a known protocol** | `Briefly,` (`55.4%`) / `In brief,` (`26.1%`) | `Briefly, fresh tumour tissues were minced into ~1-mm³ fragments and enzymatically digested.` |
| **Commercial kit adherence** | `according to the manufacturer's instructions` (`49.8%`) / `protocol` / `with minor modifications` (`5.9%`) | `Libraries were constructed using the Chromium Next GEM 5' Kit v2 according to the manufacturer's instructions.` |
| **Sequential chaining** | `Following [noun],` (`45.3%`) · `Subsequently,` (`33.9%`) · `Next,` (`45.6%`) · `Finally,` (`45.9%`) · `Prior to [noun],` (`15.0%`) | `Following red blood cell lysis, cells were resuspended in FACS buffer. Prior to sorting, DAPI was added.` |
| **Pipeline handoff** | `retained for downstream analysis` (`41.0%`) | `A total of 118,420 high-quality cells were retained for downstream analysis.` |
| **Citing established protocol** | `as previously described` (`38.8%`) / `as described above` | `Organoid establishment was performed as previously described (ref. X) with minor modifications.` |
| **Compliance / ethics** | `in accordance with` (`34.9%`) / `approved by the` | `All procedures were conducted in accordance with the Declaration of Helsinki and approved by the IRB.` |
| **Software parameters** | `with default parameters` (`29.6%`) / `unless otherwise specified/indicated` (`10.1%`) | `DESeq2 (v1.42.0) was executed with default parameters unless otherwise specified.` |
| **Precision specifier** | `Specifically,` (`25.1%`) · `Where indicated,` (`10.1%`) · `on the basis of` (`24.8%`) | `Specifically, genes expressed in fewer than 10 cells were removed on the basis of sparsity.` |

---

### 4. Scientific Units, Reagents & Software Citation Syntax

1. **Centrifugation**: Always use relative centrifugal force (`g`, italic or upright consistently, **never `rpm`** without rotor radius): `centrifuged at 300g for 5 min at 4 °C` (or `500 × g for 5 min`).
2. **Temperature & Time**: `incubated at 37 °C for 30 min`, `overnight at 4 °C`, `at room temperature for 15 min`, `stored at −80 °C` (true minus `−`, space before `°C`, abbreviated `s`, `min`, `h`, `d`).
3. **Concentrations & Dimensions**: `10% (v/v) FBS`, `1 mg ml⁻¹` or `1 mg/mL` (keep consistent throughout paper), `70-μm cell strainer`, `5-μm-thick FFPE sections`, `~1-mm³ fragments` (hyphenate compound adjectival units before a noun: `5-μm sections`, `12-h light/dark cycle`, `150-bp paired-end reads`).
4. **Reagents / Kits / Antibodies**: `anti-CD8α antibody (Abcam, cat. no. ab237709; 1:500 dilution; RRID: AB_2892677)`.
5. **Software & Packages**: `Seurat (v4.3.0)`, `Scanpy (v1.9.8)`, `Cell Ranger (v7.1.0)`, `R (v4.3.2)`, `Python (v3.10.12)`, `GraphPad Prism (v10.1.2)`. Always cite original tool publications!

---

### 5. Common Chinglish / Non-Idiomatic Methods Pitfalls → Authentic CNS Fixes

| # | ❌ Avoid (Chinglish / Informal / Imprecise) | ✅ Authentic CNS Replacement | Why |
| :---: | :--- | :--- | :--- |
| 1 | `We used Seurat to do clustering of single cells.` | `Unsupervised clustering was performed using Seurat (v4.3.0) via the Leiden algorithm (resolution = 0.6).` | Past passive, exact version, algorithm, and resolution parameter. |
| 2 | `Then we deleted low quality cells whose MT > 20%.` | `Low-quality cells with > 20% mitochondrial transcripts were excluded from downstream analysis.` | `excluded` / `filtered out` (not `deleted`); full biological term (`mitochondrial transcripts`). |
| 3 | `According to the kit instruction, RNA was extracted.` | `Total RNA was extracted using the RNeasy Mini Kit (Qiagen, cat. no. 74104) according to the manufacturer's instructions.` | Idiomatic singular possessive `manufacturer's instructions` + exact kit/vendor/cat. no. |
| 4 | `Samples were spun at 1500 rpm for 5 minutes.` | `Cell suspensions were centrifuged at 300g for 5 min at 4 °C.` | `centrifuged` (not `spun`), `g` (reproducible across rotors), temperature stated. |
| 5 | `Cells were put in 37°C incubator with 5% CO2.` | `Cells were maintained at 37 °C in a humidified atmosphere containing 5% CO₂.` | Standard cell culture register (`maintained`, `humidified atmosphere`). |
| 6 | `We got 45 cancer patients from our hospital.` | `A total of 45 patients with histologically confirmed [cancer type] were enrolled at [Hospital Name] between [Month Year] and [Month Year].` | Clinical precision (`histologically confirmed`, `enrolled`, enrollment window). |
| 7 | `The study got ethical approval and patients signed consent.` | `The study protocol was approved by the Institutional Review Board of [Institution] (protocol no. [XXXX]), and written informed consent was obtained from all participants in accordance with the Declaration of Helsinki.` | Mandatory CNS human ethics disclosure. |
| 8 | `Mice were killed when tumors became too big.` | `Mice were euthanized when tumour volume reached the humane endpoint of 1,500 mm³ (or when ulceration occurred).` | `euthanized` (never `killed`), quantitative humane endpoint. |
| 9 | `Cell lines were checked for mycoplasma.` | `All cell lines were authenticated by short tandem repeat (STR) profiling and routinely tested negative for mycoplasma contamination using [MycoAlert / PCR] prior to experiments.` | Explicitly confirms both STR authentication and negative status. |
| 10 | `Reads were mapped to human genome hg38.` | `Raw sequencing reads were aligned against the human reference genome (GRCh38; GENCODE v43) using STAR (v2.7.10b).` | Exact assembly + annotation release + aligner version. |
| 11 | `Batch effect was removed by Harmony.` | `Inter-patient batch effects were mitigated using Harmony (v1.2.0) on the top 30 principal components.` | `mitigated` / `corrected` (never claim complete "removal") + exact input (`top 30 PCs`). |
| 12 | `DEGs were found by FindMarkers.` | `Differentially expressed genes (DEGs) were identified using the two-sided Wilcoxon rank-sum test in Seurat (`FindMarkers`; min.pct = 0.1, logfc.threshold = 0.25), with P values adjusted via the Benjamini–Hochberg procedure.` | Exact test, thresholds, and multiple-testing correction. |
| 13 | `GSEA was done using Hallmark gene sets.` | `Gene set enrichment analysis (GSEA) was performed using `fgsea` (v1.28.0) against the MSigDB Hallmark gene set collection (v2023.2.Hs), with 10,000 permutations.` | Exact tool, database version, and permutation count. |
| 14 | `Cell-cell communication was analyzed by CellChat.` | `Intercellular ligand–receptor communication networks were inferred using CellChat (v1.6.1) with the curated human CellChatDB; interactions with permutation P < 0.01 were retained.` | Domain verb (`inferred`), database version, and significance cutoff. |
| 15 | `Survival difference was tested by KM curve.` | `Kaplan–Meier survival curves were generated using the R package `survival` (v3.5-7), and survival differences between groups were compared using the two-sided log-rank test.` | Separates curve estimation (`Kaplan–Meier`) from hypothesis test (`two-sided log-rank`). |
| 16 | `Statistical analysis was done by R software. P < 0.05 means significant.` | `All statistical analyses were performed in R (v4.3.2). Unless otherwise specified, all statistical tests were two-sided, and Benjamini–Hochberg-adjusted P < 0.05 was considered statistically significant.` | Exact version, two-sided default, FDR adjustment, authentic closing phrase. |
| 17 | `We didn't calculate sample size before experiment.` | `No statistical methods were used to predetermine sample sizes, but our sample sizes are similar to those reported in previous publications.` | Verbatim Nature Reporting Summary standard phrasing. |
| 18 | `Data can be asked from the corresponding author.` | `Raw human sequencing data have been deposited in [GSA-Human / EGA] under accession [ID] and are available under controlled access upon reasonable request to the Data Access Committee in compliance with patient privacy regulations.` | Compliant controlled-access human genomics wording. |
| 19 | `Code is uploaded to GitHub.` | `All custom scripts used for data processing and figure generation are publicly available on GitHub (https://github.com/[ORG]/[REPO]) and archived on Zenodo (https://doi.org/10.5281/zenodo.[XXXX]).` | Permanent reproducibility citation (GitHub + Zenodo DOI). |
| 20 | `First, ... Second, ... Third, ... Then, ... After that, ...` | `Briefly, ... Following [step], ... Subsequently, ... Finally, ...` | Eliminates repetitive elementary sequence adverbs. |

---

## Part 3 — Reusable CNS Experimental & Clinical Methods Corpus

Empirically distilled modular templates from 307 CNS Methods / STAR Methods sections. Replace bracketed `[SLOTS]` with study-specific parameters; switch British (`tumour`, `analyse`) vs American (`tumor`, `analyze`) spelling per target journal.

---

### 1. Human Participants, Clinical Cohorts & Ethics (`50.8%` of corpus)

> **Human samples and study cohorts**
> A total of `[N]` patients with histologically confirmed `[cancer type / disease]` were enrolled at `[Hospital / Institution Name]` between `[Month Year]` and `[Month Year]`. All clinical specimens—comprising `[fresh tumour biopsies, adjacent normal tissues, and matched peripheral blood]`—were collected prior to `[or during]` `[treatment regimen]`. This study was approved by the Institutional Review Board (IRB) of `[Institution Name]` (protocol no. `[XXXX]`) and conducted in accordance with the Declaration of Helsinki. Written informed consent was obtained from all participants prior to sample collection. Clinical tumour staging was determined according to the `[8th edition AJCC TNM classification]`, and treatment responses were evaluated according to Response Evaluation Criteria in Solid Tumours (`RECIST v1.1`) as complete response (CR), partial response (PR), stable disease (SD), or progressive disease (PD). Detailed clinicopathological characteristics, including age, sex, and treatment history, are summarized in `[Supplementary Table 1 / Table S1]`.

---

### 2. Animal Models & In Vivo Experiments (`45.0%` of corpus)

> **Animal models and in vivo treatments**
> Six- to eight-week-old `[female/male]` `[C57BL/6J / BALB/c / NSG]` mice were purchased from `[The Jackson Laboratory / Charles River / GemPharmatech]` and housed under specific-pathogen-free (SPF) conditions at `18–23 °C` and `40–60%` relative humidity under a `12-h` light/dark cycle, with food and water provided *ad libitum*. All animal experiments were approved by the Institutional Animal Care and Use Committee (IACUC) of `[Institution Name]` (protocol no. `[XXXX]`) and performed in accordance with institutional animal welfare guidelines.
>
> To establish `[subcutaneous / orthotopic]` tumour models, `[5 × 10⁵]` `[cell line name]` cells suspended in `[100 μl]` of `[PBS / 1:1 PBS:Matrigel]` were injected `[subcutaneously into the right flank / orthotopically into the ...]` of recipient mice. Once tumours reached an average volume of `[~80–100 mm³]`, mice were randomly assigned to `[treatment arms]` (`n = [8]` mice per group) and administered `[anti-PD-1 (clone RMP1-14, Bio X Cell, cat. no. BE0146; 200 μg per mouse)]` or isotype control (`clone 2A3`) intraperitoneally every `[3 days]` for `[four doses]`. Tumour dimensions were measured every `[2–3 days]` using digital calipers by investigators blinded to group allocation, and tumour volume was calculated as `V = (length × width²) / 2`. Mice were euthanized when tumour volume reached the humane endpoint of `[1,500 mm³]` or upon signs of ulceration or distress.

---

### 3. Cell Lines, Primary Culture & Organoids (`74.6%` of corpus)

> **Cell lines and culture conditions**
> Human `[cell line A]` and `[cell line B]` cells were obtained from `[ATCC / DSMZ]` and maintained in `[DMEM / RPMI-1640]` (Gibco) supplemented with `10% (v/v)` heat-inactivated fetal bovine serum (FBS; Gibco) and `1%` penicillin–streptomycin (`100 U ml⁻¹` penicillin, `100 μg ml⁻¹` streptomycin) at `37 °C` in a humidified atmosphere containing `5% CO₂`. All cell lines were authenticated by short tandem repeat (STR) profiling within `[6 months]` of use and routinely tested negative for mycoplasma contamination using the `[MycoAlert Mycoplasma Detection Kit (Lonza) / PCR-based screening]`.

---

### 4. Tissue Dissociation, PBMC Isolation & Flow Cytometry (`55.4%` of corpus)

> **Tissue dissociation and single-cell suspension preparation**
> Fresh surgical specimens were transported on ice in `[MACS Tissue Storage Solution (Miltenyi Biotec)]` and processed within `[2 h]` of resection. Briefly, tissues were washed twice with ice-cold PBS, minced into `~1-mm³` fragments, and enzymatically digested in `[RPMI-1640]` containing `[1 mg ml⁻¹ collagenase IV (Worthington) and 0.1 mg ml⁻¹ DNase I (Sigma-Aldrich)]` at `37 °C` for `[30 min]` with gentle agitation. Following digestion, cell suspensions were passed through a `70-μm` cell strainer, centrifuged at `300g` for `5 min` at `4 °C`, and treated with `ACK lysing buffer` (Gibco) for `3 min` on ice to remove erythrocytes. Cells were subsequently washed and resuspended in ice-cold PBS containing `0.04% (w/v)` BSA, and cell viability (`> 85%`) was assessed using trypan blue exclusion on a `[Countess II Automated Cell Counter (Thermo Fisher Scientific)]`.

> **Flow cytometry and fluorescence-activated cell sorting (FACS)**
> Single-cell suspensions were first incubated with `[Human TruStain FcX / anti-mouse CD16/32 (BioLegend)]` for `10 min` at `4 °C` to block nonspecific Fc receptor binding, followed by staining with `[Fixable Viability Dye eFluor 780 (Thermo Fisher Scientific)]` and fluorophore-conjugated surface antibodies (`[Supplementary Table X]`) for `30 min` at `4 °C` in the dark. For intracellular cytokine staining, cells were stimulated ex vivo with `[PMA (50 ng ml⁻¹) and ionomycin (1 μg ml⁻¹)]` in the presence of `[Brefeldin A]` for `4 h` at `37 °C`, fixed and permeabilized using the `[Foxp3/Transcription Factor Staining Buffer Set (eBioscience)]` according to the manufacturer's instructions, and stained overnight at `4 °C`. Data were acquired on a `[BD LSRFortessa / Cytek Aurora]` cytometer and analyzed using `FlowJo (v10.9.0)`. Cell sorting was performed on a `[BD FACSAria III]` equipped with a `[100-μm]` nozzle.

---

### 5. Single-Cell & Spatial Sequencing Library Preparation (`61.6%` of corpus)

> **Single-cell RNA-seq and TCR-seq library preparation and sequencing**
> Single-cell suspensions were loaded onto a `[Chromium Controller / Chromium X]` (10x Genomics) targeting a recovery of `[8,000–10,000]` cells per sample. Gene expression (`5'` or `3'`) and paired V(D)J TCR libraries were constructed using the `[Chromium Next GEM Single Cell 5' Reagent Kit v2 (10x Genomics, cat. no. PN-1000263)]` strictly according to the manufacturer's instructions. Library quality and fragment size distribution were verified using an `[Agilent 4200 TapeStation]`, and libraries were quantified by Qubit dsDNA HS Assay (Thermo Fisher Scientific). Pooled libraries were sequenced on an `[Illumina NovaSeq 6000]` platform using `150-bp` paired-end reads to a minimum depth of `[50,000]` reads per cell for gene expression and `[5,000]` reads per cell for V(D)J libraries.

> **Spatial transcriptomics (10x Visium / Xenium)**
> Formalin-fixed, paraffin-embedded (FFPE) tumour blocks passing RNA quality control (`DV200 > 50%`) were sectioned at `5-μm` thickness and mounted onto `[Visium CytAssist Spatial Gene Expression slides (10x Genomics)]`. Deparaffinization, H&E staining, whole-slide brightfield imaging (`20×` magnification), probe hybridization, ligation, and library construction were performed according to the manufacturer's protocol. Libraries were sequenced on an `[Illumina NovaSeq 6000]` targeting `[≥ 25,000]` read pairs per tissue-covered spot.

---

### 6. Histology, IHC & Multiplex Immunofluorescence (mIF / CODEX) (`57.0%` of corpus)

> **Multiplex immunofluorescence (mIF) staining and image acquisition**
> Serial `4-μm`-thick FFPE tissue sections were baked at `60 °C` for `1 h`, deparaffinized in xylene, and rehydrated through a graded ethanol series. Heat-induced epitope retrieval was performed in `[Tris-EDTA buffer (pH 9.0) / citrate buffer (pH 6.0)]` for `15 min` using a microwave/pressure cooker. Endogenous peroxidase activity was quenched with `3% H₂O₂` for `10 min`, and sections were blocked with `[5% normal goat serum / Akoya Antibody Diluent]` at room temperature for `30 min`. Sequential rounds of primary antibody incubation (overnight at `4 °C` or `1 h` at room temperature), HRP-conjugated secondary polymer incubation, and tyramide signal amplification using the `[Opal 7-Color Manual IHC Kit (Akoya Biosciences)]` were performed (`[antibodies and dilutions listed in Supplementary Table X]`). Nuclei were counterstained with `DAPI`, and slides were mounted with `[ProLong Diamond Antifade Mountant]`. Whole-slide multispectral images were acquired on a `[PhenoImager HT / Vectra Polaris (Akoya Biosciences)]` at `20×` magnification (`0.5 μm pixel⁻¹`).

---

### 7. Core Molecular & Functional Assays (CRISPR, Western Blot, RT-qPCR)

> **CRISPR–Cas9 gene knockout**
> Single-guide RNAs (sgRNAs) targeting `[GENE]` or a non-targeting control (NTC) (`[sequences in Supplementary Table X]`) were cloned into the `[lentiCRISPRv2 (Addgene, #52961)]` vector. Lentiviral particles were packaged in HEK293T cells co-transfected with `psPAX2` and `pMD2.G` using `[Lipofectamine 3000]` and harvested at `48 h` and `72 h` post-transfection. Target cells were transduced in the presence of `8 μg ml⁻¹` polybrene, selected with `[2 μg ml⁻¹ puromycin]` for `[7 days]`, and knockout efficiency was confirmed by immunoblotting and Sanger sequencing.

> **Immunoblotting (Western blot)**
> Cells were lysed on ice for `30 min` in `RIPA buffer` supplemented with protease and phosphatase inhibitor cocktails (`Thermo Fisher Scientific`). Lysates were cleared by centrifugation at `14,000g` for `15 min` at `4 °C`, and protein concentrations were quantified using a `BCA Protein Assay Kit`. Equal amounts of protein (`20–30 μg`) were resolved by `SDS–PAGE`, transferred onto `PVDF` membranes (`Millipore`), blocked in `5% (w/v)` non-fat milk in `TBST` for `1 h` at room temperature, and probed overnight at `4 °C` with primary antibodies followed by HRP-conjugated secondary antibodies for `1 h` at room temperature. Signals were visualized by enhanced chemiluminescence (`ECL`) on a `[ChemiDoc Imaging System (Bio-Rad)]`.

---

## Part 4 — Reusable CNS Computational, Bioinformatics & ML Methods Corpus

Empirically distilled modular templates from 307 CNS Methods / STAR Methods sections. Replace bracketed `[SLOTS]` with exact tool versions, thresholds, and reference builds from your actual pipeline.

---

### 1. Bulk RNA-seq, WES & WGS Preprocessing (`58.3%` of corpus)

> **Bulk RNA-seq alignment and quantification**
> Raw paired-end FASTQ reads were assessed for quality using `FastQC (v0.12.1)` and trimmed for adapter sequences and low-quality bases using `fastp (v0.23.4)` with default parameters. Clean reads were aligned to the human reference genome (`GRCh38`; `GENCODE v43`) using `STAR (v2.7.10b)` in two-pass mode. Gene-level raw counts were quantified using `featureCounts (Subread v2.0.6)` [or `Salmon (v1.10.1)`], and normalized expression values were computed as transcripts per million (TPM) or variance-stabilized counts (`vst`) for downstream analysis.

> **Whole-exome sequencing (WES) and somatic variant calling**
> Trimmed reads were mapped to `GRCh38` using `BWA-MEM (v0.7.17)`. Duplicate reads were marked and base quality scores were recalibrated following the `GATK (v4.4.0)` Best Practices workflow. Somatic single-nucleotide variants (SNVs) and small insertions/deletions (indels) were called from matched tumour–normal pairs using `Mutect2` and filtered with `FilterMutectCalls` and a panel of normals. High-confidence somatic variants (`sequencing depth ≥ 20×`, `variant allele frequency ≥ 5%`, `≥ 4 supporting reads`) were annotated using `ANNOVAR` / `Ensembl VEP (v110)`.

---

### 2. scRNA-seq Alignment, Ambient RNA & Doublet Removal (`60.6%` of corpus)

> **Single-cell RNA-seq preprocessing and quality control**
> Raw sequencing reads were demultiplexed, aligned to the human reference genome (`GRCh38-2020-A`), and quantified into gene-by-barcode UMI count matrices using `Cell Ranger (v7.1.0; 10x Genomics)` with default parameters. To minimize ambient RNA contamination, raw count matrices were corrected using `SoupX (v1.6.2)` [or `CellBender (v0.3.0)`]. Putative doublets were identified and removed on a per-sample basis using `scDblFinder (v1.16.0)` [or `DoubletFinder (v2.0.4)` / `Scrublet (v0.2.3)`]. Subsequently, low-quality cells were filtered out according to the following criteria: `< [300]` or `> [6,000]` detected genes, `< [500]` UMIs, or `> [15%]` mitochondrial transcript fraction. Genes expressed in fewer than `[10]` cells across the entire dataset were excluded. In total, `[N]` high-quality single cells from `[M]` samples were retained for downstream analysis.

---

### 3. Normalization, Batch Integration, Clustering & Annotation (`60.6%` of corpus)

> **Normalization, dimensionality reduction, integration and cell-type annotation**
> Downstream single-cell analyses were performed using `Seurat (v4.3.0)` in `R (v4.3.2)` [or `Scanpy (v1.9.8)` in `Python (v3.10.12)`]. UMI counts were log-normalized (`NormalizeData`, scale factor `10,000`), and the top `[2,000]` highly variable genes (HVGs) were selected using variance-stabilizing transformation (`FindVariableFeatures`), excluding mitochondrial, ribosomal, immunoglobulin, and T-cell receptor genes prior to principal component analysis (PCA) to avoid technical or clonal confounding. To mitigate inter-patient batch effects while preserving biological variation, samples were integrated using `Harmony (v1.2.0)` [or `scVI (v1.1.0)`] on the top `[30]` principal components. A shared nearest-neighbor (SNN) graph was constructed on the Harmony-corrected embedding (`FindNeighbors`), and unsupervised clustering was performed using the `Leiden` [or `Louvain`] algorithm (`resolution = [0.6]`). Two-dimensional visualization was generated via Uniform Manifold Approximation and Projection (`UMAP`). Major cell lineages and fine-grained subclusters were annotated on the basis of canonical lineage markers and cluster-specific differentially expressed genes (`[Supplementary Table X]`).

---

### 4. Differential Expression, Pseudobulk & Pathway / GSEA (`62.2%` of corpus)

> **Differential gene expression and pathway enrichment analysis**
> To identify cluster-specific marker genes, differential expression was assessed using the two-sided Wilcoxon rank-sum test implemented in `Seurat::FindMarkers` (`min.pct = 0.1`, `logfc.threshold = 0.25`), with *P* values adjusted via the Benjamini–Hochberg procedure. To compare gene expression between clinical groups (e.g., responders versus non-responders) without single-cell pseudoreplication, raw UMI counts were aggregated by patient and cell type into pseudobulk profiles, and differential expression was modeled using `DESeq2 (v1.42.0)` adjusting for `[batch / sex / tissue site]`. Genes with `|log₂(fold change)| > [1]` and Benjamini–Hochberg-adjusted `P < [0.05]` were defined as significantly differentially expressed.
>
> Gene set enrichment analysis (GSEA) was performed using `fgsea (v1.28.0)` (`10,000` permutations) against the `MSigDB` Hallmark and Gene Ontology Biological Process collections (`v2023.2.Hs`). Single-cell pathway activity scores were calculated using `AUCell (v1.24.0)` [or `Seurat::AddModuleScore` / `UCell (v2.6.0)`].

---

### 5. Trajectory, RNA Velocity, Cell–Cell Interaction & CNV (`28.3%` of corpus)

> **Pseudotime trajectory and RNA velocity analysis**
> Transcriptional differentiation trajectories within `[CD8⁺ T cells]` were inferred using `Monocle 3 (v1.3.4)` [or `Slingshot (v2.10.0)`], rooting the trajectory at `[naive CCR7⁺ T cells]` on the basis of biological prior knowledge and `CytoTRACE (v0.3.3)` stemness scores. To orthogonally validate directional state transitions, spliced and unspliced transcript counts were quantified with `velocyto (v0.17.17)` and modeled using the dynamical mode of `scVelo (v0.3.1)`.

> **Cell–cell communication analysis**
> Intercellular ligand–receptor signaling networks were inferred using `CellChat (v1.6.1)` [or `CellPhoneDB (v4.1.0)` / `NicheNet (v2.0.4)`] based on the curated human ligand–receptor database. Communication probabilities were computed with default parameters (`1,000` permutations), and ligand–receptor pairs with permutation `P < 0.01` were retained as statistically significant.

> **Copy-number variation (CNV) inference**
> To distinguish malignant epithelial cells from non-malignant epithelial cells, chromosomal CNVs were inferred from scRNA-seq expression profiles using `inferCNV (v1.18.1)` [or `CopyKAT (v1.1.0)`] with `[T cells and myeloid cells]` as diploid reference populations (`cutoff = 0.1`, `denoise = TRUE`, `HMM = TRUE`).

> **TCR repertoire analysis**
> Paired αβ TCR sequences were assembled using `Cell Ranger vdj (v7.1.0)`. Productive clonotypes were defined by identical paired CDR3 amino acid sequences, and clonal expansion, diversity (Shannon entropy), and cross-compartment sharing were quantified using `scRepertoire (v2.0.0)` [or `STARTRAC`].

---

### 6. Spatial Transcriptomics & mIF Spatial Neighborhood Analysis (`57.0%` of corpus)

> **Spatial deconvolution and niche identification**
> Visium spatial sequencing reads were processed with `Space Ranger (v2.1.1)` (`GRCh38`). Spot-level cell-type proportions were deconvolved using `RCTD (spacexr v2.2.1)` [or `Cell2location (v0.1.3)`] referencing our matched scRNA-seq atlas (`doublet_mode = 'full'`). Spatial niches were identified by unsupervised `[k-means / Leiden]` clustering of spot-level cell-type composition vectors across integrated tissue sections.

> **Multiplex IF image quantification and spatial proximity analysis**
> Multispectral whole-slide images were spectrally unmixed in `inForm (v2.6.0)` and imported into `QuPath (v0.5.0)` [or `HALO (v3.6)`] for nuclear segmentation (`StarDist`), intensity-thresholded cell phenotyping, and tissue-compartment classification (tumour core versus stroma), reviewed independently by a board-certified pathologist blinded to clinical outcomes. Spatial co-localization between cell phenotypes `A` and `B` was quantified within a `[30-μm]` radius and compared against a null distribution generated by `1,000` random label permutations within each tissue compartment (`squidpy v1.4.1` / `spatstat`).

---

### 7. Survival Analysis, Cox Regression & Machine Learning (`42.0%` of corpus)

> **Survival and clinical association analysis**
> Overall survival (OS) and progression-free survival (PFS) were analyzed using the R packages `survival (v3.5-7)` and `survminer (v0.4.9)`. Patients were stratified into high- and low-expression groups based on `[the cohort median / optimal cutpoint determined by maximally selected rank statistics (maxstat)]`. Survival curves were estimated using the Kaplan–Meier method and compared with the two-sided log-rank test. Univariable and multivariable Cox proportional hazards models were fitted adjusting for `[age, sex, tumour stage, and treatment line]`; the proportional hazards assumption was verified using Schoenfeld residuals (`cox.zph`).

> **Predictive modelling and validation**
> To build a predictive classifier for `[immunotherapy response]`, features were standardized (`z-score`) strictly within each training fold to prevent data leakage. Models (`[LASSO logistic regression / Random Forest / XGBoost]`) were trained in `scikit-learn (v1.4.0)` using stratified `[5-fold cross-validation]` (`10` repeats) for hyperparameter tuning, and evaluated on independent external validation cohorts (`[Cohort A, n = X; Cohort B, n = Y]`). Discrimination was assessed via area under the receiver operating characteristic curve (`AUROC`) with `95%` confidence intervals computed by `1,000` stratified bootstrap replicates; model interpretability was evaluated using TreeSHAP (`shap v0.45.0`).

---

## Part 5 — Statistics, Reproducibility, Resource, Data & Code Availability Corpus

Empirically distilled mandatory closing sections across *Nature Portfolio*, *Cell Press STAR Methods*, and *Science / AAAS* (`79.8%` data availability, `79.2%` statistics, `67.4%` code availability across 307 audited CNS Methods).

---

### 1. Quantification & Statistical Analysis (Drop-In Master Block)

#### 1.1 Nature Portfolio Style (`Statistics and reproducibility`)
> **Statistics and reproducibility**
> All statistical analyses were performed in `R (v4.3.2)`, `Python (v3.10.12)`, or `GraphPad Prism (v10.1.2)`. No statistical methods were used to predetermine sample sizes, but our sample sizes are similar to those reported in previous publications. For animal experiments, mice were randomly allocated to experimental groups, and investigators were blinded to group allocation during tumour measurement and histological evaluation. Data distribution was assessed for normality using the Shapiro–Wilk test. Unless otherwise specified, all statistical tests were two-sided. Comparisons between two independent groups were performed using the two-sided Wilcoxon rank-sum test (non-parametric) or two-sided unpaired Student's *t*-test / Welch's *t*-test (parametric); paired comparisons were assessed using the two-sided Wilcoxon signed-rank test or paired *t*-test. Comparisons across three or more groups were evaluated by Kruskal–Wallis test with Dunn's post hoc test or one-way/two-way ANOVA with Tukey's or Šídák's multiple comparisons test. Correlations were quantified using Spearman's rank correlation coefficient (`ρ`) or Pearson's correlation coefficient (`r`). Categorical variables were compared using two-sided Fisher's exact test or Pearson's χ² test. Where multiple hypotheses were tested simultaneously, *P* values were adjusted using the Benjamini–Hochberg false discovery rate (FDR) method, and adjusted `P < 0.05` was considered statistically significant. All in vitro experiments were performed with at least three independent biological replicates unless otherwise indicated in the figure legends.

#### 1.2 Cell Press STAR Methods Style (`QUANTIFICATION AND STATISTICAL ANALYSIS`)
> **QUANTIFICATION AND STATISTICAL ANALYSIS**
> All statistical analyses were conducted using `R (v4.3.2)` and `GraphPad Prism (v10.1.2)`. Statistical details of individual experiments—including the exact value of *n*, what *n* represents (e.g., number of patients, mice, or biological replicates), definition of center and dispersion measures (mean ± SD, mean ± SEM, or median with IQR), and the exact statistical tests used—are provided in the figure legends and Results. Normality was evaluated using the Shapiro–Wilk test. Two-group comparisons were assessed using two-tailed unpaired or paired Student's *t*-tests (parametric) or two-sided Mann–Whitney *U* / Wilcoxon signed-rank tests (non-parametric). Multiple-group comparisons were performed using one-way or two-way ANOVA with Tukey's/Šídák's correction or the Kruskal–Wallis test with Dunn's post hoc test. For high-dimensional omics comparisons, *P* values were adjusted for multiple testing using the Benjamini–Hochberg procedure. Survival differences were evaluated by the two-sided log-rank test. Significance thresholds are defined as `*p < 0.05, **p < 0.01, ***p < 0.001, ****p < 0.0001; ns, not significant`.

---

### 2. Nature Portfolio Reporting Summary Statement

> **Reporting summary**
> Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

---

### 3. Cell Press STAR Methods: `RESOURCE AVAILABILITY` (Mandatory Verbatim Schema)

> **RESOURCE AVAILABILITY**
>
> **Lead contact**
> Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, `[Full Name]` (`[email@institution.edu]`).
>
> **Materials availability**
> `[Option A]` This study did not generate new unique reagents.
> `[Option B]` All unique reagents, plasmids, and cell lines generated in this study are available from the lead contact upon reasonable request with a completed materials transfer agreement (MTA).
>
> **Data and code availability**
> - Raw and processed `[scRNA-seq / spatial transcriptomics / WES]` data generated in this study have been deposited in `[GEO / GSA-Human / EGA]` under accession number `[GSEXXXXXX / HRAXXXXXX / EGASXXXXXXXXXXX]` and are `[publicly available / available under controlled access]` as of the date of publication.
> - Publicly available datasets reanalyzed in this study are accessible under accession numbers `[GSEYYYYYY, TCGA-XXXX]` (listed in the Key Resources Table).
> - All original analysis code has been deposited on GitHub (`https://github.com/[ORG]/[REPO]`) and archived on Zenodo (`https://doi.org/10.5281/zenodo.[XXXXXXX]`), and is publicly available as of the date of publication.
> - Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request.

---

### 4. Nature & Science Data and Code Availability Templates

#### 4.1 Open-Access Animal / Cell-Line Omics Data (GEO / SRA)
> **Data availability**
> Raw and processed `[scRNA-seq / bulk RNA-seq / Visium]` data generated in this study have been deposited in the Gene Expression Omnibus (GEO) under accession code `[GSEXXXXXX]` (or NCBI Sequence Read Archive under BioProject `[PRJNAXXXXXX]`). Processed Seurat/AnnData objects and spatial imaging matrices are available via Zenodo (`https://doi.org/10.5281/zenodo.[XXXXXXX]`). Source data are provided with this paper.

#### 4.2 Controlled-Access Human Clinical Genomic Data (GSA-Human / EGA / dbGaP)
> **Data availability**
> Raw sequencing data from human participants have been deposited in the Genome Sequence Archive for Human (`GSA-Human`, National Genomics Data Center) under accession number `[HRAXXXXXX]` [or European Genome-phenome Archive (`EGA`), accession `[EGASXXXXXXXXXXX]`]. To protect participant privacy in compliance with institutional ethical approvals and national human genetic resource regulations, raw sequencing files are available under controlled access. Qualified academic researchers may request access through the `[GSA-Human / EGA]` Data Access Committee (`[DAC email or portal URL]`); requests will be reviewed within `[30 days]` and granted upon execution of a Data Access Agreement for non-commercial research use. De-identified processed expression count matrices and cell metadata are publicly available at `[GEO GSEXXXXXX / Zenodo DOI]`.

#### 4.3 Code Availability
> **Code availability**
> All custom scripts and notebooks used for data preprocessing, statistical analysis, and figure generation are publicly available on GitHub (`https://github.com/[ORG]/[REPO]`) and permanently archived on Zenodo (`https://doi.org/10.5281/zenodo.[XXXXXXX]`) under the `[MIT]` license.

#### 4.4 Science / AAAS `Data and materials availability`
> **Data and materials availability**
> All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Raw sequencing data have been deposited in `[GEO / GSA-Human]` under accession `[ID]`. Custom analysis code is archived on Zenodo (`https://doi.org/10.5281/zenodo.[XXXXXXX]`). `[Reagent/material]` can be provided by `[Institution]` pending scientific review and a completed material transfer agreement.
