#!/usr/bin/env python3
"""
audit_manuscript.py — Unified Zero-Dependency CNS Scientific Manuscript Linter & Scaffolder.

Covers ALL 9 manuscript components:
  title | abstract | intro | results | subheadings | discussion | cover_letter | caption | methods | all

Usage:
  python audit_manuscript.py audit --section abstract --journal nature --file draft.txt
  python audit_manuscript.py audit --section all --journal cell --file full_manuscript.md
  python audit_manuscript.py scaffold --archetype mechanistic --journal cancer_cell
"""
import argparse
import re
import sys
from pathlib import Path

JOURNAL_SPECS = {
    "nature": {
        "title_max_w": 12, "title_colon_ok": False,
        "abs_min_w": 130, "abs_max_w": 250,
        "intro_max_w": 550, "sub_max_w": 9,
        "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK",
    },
    "nature_sister": {
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 110, "abs_max_w": 165,
        "intro_max_w": 750, "sub_max_w": 13,
        "disc_lim_mandatory": False, "cap_max_w": 350, "spelling": "UK",
    },
    "nat_med": {
        "title_max_w": 18, "title_colon_ok": True,
        "abs_min_w": 140, "abs_max_w": 240,
        "intro_max_w": 650, "sub_max_w": 13,
        "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
    },
    "cell": {
        "title_max_w": 15, "title_colon_ok": True,
        "abs_min_w": 100, "abs_max_w": 160,
        "intro_max_w": 700, "sub_max_w": 16,
        "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
    },
    "cancer_cell": {
        "title_max_w": 16, "title_colon_ok": True,
        "abs_min_w": 100, "abs_max_w": 160,
        "intro_max_w": 700, "sub_max_w": 16,
        "disc_lim_mandatory": True, "cap_max_w": 350, "spelling": "US",
    },
    "science": {
        "title_max_w": 13, "title_colon_ok": False,
        "abs_min_w": 85, "abs_max_w": 140,
        "intro_max_w": 650, "sub_max_w": 14,
        "disc_lim_mandatory": False, "cap_max_w": 300, "spelling": "US",
    },
}

CHINGLISH_PATTERNS = [
    (r"\bwith the rapid development of\b", "Macro-era throat-clearing cliché ('with the rapid development of'); open directly with the biological or clinical phenomenon."),
    (r"\bfew studies have (investigated|explored|studied|focused on)\b", "Weak 'few studies' gap (only 1.1% in 2025-2026 CNS); replace with a mechanistic, spatial, clinical, or technical contradiction."),
    (r"\blittle attention has been paid\b", "Weak 'little attention' gap; state the concrete scientific barrier instead."),
    (r"\bmore and more\b", "Informal ('more and more'); replace with 'increasingly' or 'a growing number of'."),
    (r"\bobviously\b|\bvery significantly\b|\bremarkably significant\b", "Subjective/redundant intensifier ('obviously' / 'very significantly'); use 'markedly' or report exact fold change and P value."),
    (r"\bin order to\b", "Wordy ('in order to'); tighten to concise 'To [verb]...'."),
    (r"\bas can be seen from (fig|figure)\b", "Chinglish figure reference ('As can be seen from Fig.'); state the biological result as subject and cite '(Fig. Xa)' parenthetically."),
    (r"\bproved that\b|\bproves that\b", "Overclaiming verb ('proved'); biological data rarely 'prove'—use 'demonstrated', 'established', or 'indicated' per the 4-tier certainty ladder."),
    (r"\bplay(s)? a very important role\b|\bhas (great|important) clinical significance\b", "Empty significance cliché; name the concrete biological function or translational utility."),
    (r"\bnovel\b.*\bfirst\b|\bfor the first time\b", "Editorial red flag ('for the first time' / 'novel...first'); let specific findings convey novelty without self-praise."),
]


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def split_sents(text: str):
    t = re.sub(r"\b(Fig|Figs|vs|et al|e\.g|i\.e|Dr|Prof|No)\.", r"\1<D>", text)
    t = re.sub(r"(\d)\.(\d)", r"\1<P>\2", t)
    return [s.replace("<D>", ".").replace("<P>", ".").strip() for s in re.split(r"(?<=[.!?])\s+", t.strip()) if len(s.split()) >= 4]


def scan_chinglish(text: str, findings: list):
    for pat, msg in CHINGLISH_PATTERNS:
        if re.search(pat, text, re.I):
            findings.append(("WARN", f"Style/Chinglish: {msg}"))


def audit_title(text: str, spec: dict, journal: str):
    findings = []
    t = " ".join(text.strip().splitlines()).strip().rstrip(".")
    wc = count_words(t)
    cc = len(t)
    findings.append(("INFO", f"Title length: {wc} words, {cc} chars (target for {journal}: <={spec['title_max_w']} words)."))
    if wc > spec["title_max_w"]:
        findings.append(("WARN", f"Title exceeds {journal} empirical norm ({wc} > {spec['title_max_w']} words); tighten by removing filler nouns."))
    if ":" in t and not spec["title_colon_ok"]:
        findings.append(("FAIL", f"Colon ':' detected in title — {journal} publishes 0% colon titles in 2025-2026; remove colon."))
    if re.match(r"^(a study on|study of|investigation of|analysis of|the role of|comprehensive analysis of)\b", t, re.I):
        findings.append(("FAIL", "Deadwood opener ('A study on / Analysis of / The role of'); promote the active biological entity or discovery to subject."))
    if re.search(r"\b(novel|first|new)\b", t, re.I):
        findings.append(("WARN", "Avoid empty novelty adjectives ('novel', 'first', 'new') in CNS titles."))
    if journal == "nat_med" and re.search(r"\b(drives|controls|governs|orchestrates|fuels|licenses)\b", t, re.I):
        findings.append(("WARN", "Nat Med rarely uses strong causal title verbs (2.4%); consider conservative clinical descriptive + colon trial/cohort design."))
    # Check Title Case overuse
    cap_words = sum(1 for w in t.split()[1:] if len(w) > 3 and w[0].isupper() and not w.isupper())
    if cap_words >= max(4, wc // 2):
        findings.append(("WARN", "Title appears to be in Title Case; CNS journals mandate Sentence case."))
    return findings


def audit_abstract(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    sents = split_sents(text)
    findings.append(("INFO", f"Abstract: {wc} words, {len(sents)} sentences (target for {journal}: {spec['abs_min_w']}-{spec['abs_max_w']}w)."))
    if wc > spec["abs_max_w"]:
        findings.append(("FAIL", f"Word count ({wc}w) exceeds {journal} ceiling ({spec['abs_max_w']}w). Trim background/methods immediately."))
    elif wc < spec["abs_min_w"]:
        findings.append(("WARN", f"Word count ({wc}w) is below typical {journal} density ({spec['abs_min_w']}w); ensure quantitative findings and implication are present."))
    if not re.search(r"\b(however|yet|despite|nevertheless|remains? (unclear|unknown|poorly understood|elusive|challenging|limited)|little is known|paradox|unmet|challenge|question of whether)\b", text, re.I):
        findings.append(("WARN", "No explicit Gap/Problem pivot detected ('However, ... remains poorly understood')."))
    if not re.search(r"\b(here,?\s+we|in this study,?\s+we|we here|we show|we identify|we demonstrate|we present|we develop|we report)\b", text, re.I):
        findings.append(("WARN", "No clear main-result pivot ('Here, we show/identify/present...')."))
    if not re.search(r"\b(\d{2,}|\d+\.\d+%?|n\s*=\s*\d+|fold|auc|hr\s*=|p\s*[<=>])\b", text, re.I):
        findings.append(("WARN", "No quantitative anchors (cohort n, cell counts, fold changes, AUC/HR) detected; 55.7-76% of top abstracts include concrete numbers."))
    # Methods-bloat detector
    method_sents = sum(1 for s in sents if re.search(r"\b(seurat|harmony|cellchat|gsea|10x genomics|filtered|normalized|clustered|western blot|qpcr|pcr|flow cytometry|kit|software|pipeline|we collected|we performed|we analyzed)\b", s, re.I))
    if method_sents >= 3 or (len(sents) >= 3 and method_sents / len(sents) >= 0.45):
        findings.append(("FAIL", f"Methods bloat detected ({method_sents}/{len(sents)} method-heavy sentences); compress methodology to <=1 sentence and allocate ~50% to concrete findings."))
    if re.search(r"\[\d+\]|\(\w+ et al\., \d{4}\)", text):
        findings.append(("FAIL", "Citations detected inside Abstract; remove all references from Abstract."))
    scan_chinglish(text, findings)
    return findings


def audit_intro(text: str, spec: dict, journal: str):
    findings = []
    paras = [p.strip() for p in re.split(r"\n{2,}", text.strip()) if len(p.split()) >= 15]
    wc = count_words(text)
    findings.append(("INFO", f"Introduction: {wc} words across {len(paras)} paragraphs (target for {journal}: <={spec['intro_max_w']}w, 3-4 paras)."))
    if wc > spec["intro_max_w"] + 150:
        findings.append(("WARN", f"Introduction is lengthy ({wc}w vs {journal} norm <={spec['intro_max_w']}w); prune textbook background that does not pay off in Results."))
    if len(paras) < 2 or len(paras) > 6:
        findings.append(("WARN", f"Paragraph count ({len(paras)}) outside optimal 3-4 paragraph CNS funnel."))
    if not re.search(r"\b(however|yet|despite|nevertheless|remains? (unclear|unknown|poorly understood|elusive|limited|challenging)|little is known|poorly characterized)\b", text, re.I):
        findings.append(("FAIL", "No clear Gap/Unknown statement detected in Introduction."))
    if paras and not re.search(r"\b(here,?\s+we|in this study,?\s+we|to address|to investigate|to elucidate|to overcome|we here)\b", paras[-1], re.I):
        findings.append(("WARN", "Final Introduction paragraph lacks an active 'Here, we...' / 'In this study, we...' approach-and-findings preview."))
    if re.search(r"\[\s*\d+\s*[-–,]\s*\d+(?:\s*,\s*\d+){4,}\s*\]", text):
        findings.append(("WARN", "Heavy citation stuffing (6+ refs clustered together); 95.1% of CNS citations use 1-3 targeted refs per claim (only 2.5% use 5+)."))
    # Also check range stuffing like [1-8] or (1-8)
    for m in re.finditer(r"[\[\(]\s*(\d{1,3})\s*[-–]\s*(\d{1,3})\s*[\]\)]", text):
        if int(m.group(2)) - int(m.group(1)) >= 4:
            findings.append(("WARN", f"Citation range stuffing '{m.group(0)}' ({int(m.group(2))-int(m.group(1))+1} refs in one cluster); split into specific claims with 1-3 refs each."))
            break
    scan_chinglish(text, findings)
    return findings


def audit_subheadings(text: str, spec: dict, journal: str):
    findings = []
    lines = [re.sub(r"^#+\s*|^\d+[\.\)]\s*|^[-*]\s*", "", ln).strip() for ln in text.strip().splitlines() if ln.strip()]
    findings.append(("INFO", f"Results subheadings: {len(lines)} modules (CNS median: 6-7 modules)."))
    if len(lines) < 4 or len(lines) > 10:
        findings.append(("WARN", f"Module count ({len(lines)}) differs from CNS standard (5-8 modules matching main figures)."))
    long_sh = [ln for ln in lines if count_words(ln) > spec["sub_max_w"]]
    if long_sh:
        findings.append(("WARN", f"{len(long_sh)} subheading(s) exceed {journal} length norm ({spec['sub_max_w']}w), e.g.: '{long_sh[0][:75]}'"))
    if journal in ("cell", "cancer_cell"):
        finite_n = sum(1 for ln in lines if re.search(r"\b(is|are|was|were|drives?|promotes?|reveals?|enhances?|induces?|suppresses?|inhibits?|controls?|regulates?|mediates?|predicts?|identifies?|improves?|reprograms?|requires?|exhibits?|impairs?|attenuates?|potentiates?|increases?|reduces?|correlates?|restores?|localizes?|colocalizes?|organizes?|shapes?|remodels?|rescues?|abolishes?|synergizes?|sensitizes?|reverses?|prevents?|triggers?|orchestrates?|defines?|determines?|links?|uncovers?|establishes?|activates?|limits?|alters?|enables?|boosts?|fuels?|licenses?|governs?)\b", ln, re.I))
        if lines and finite_n / len(lines) < 0.45:
            findings.append(("WARN", f"Cell Press prefers declarative biological-takeaway subheadings (~52%+); only {finite_n}/{len(lines)} contain an active verb."))
    return findings


def audit_results(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    inline_fig = len(re.findall(r"\((?:Extended Data |Supplementary )?(?:Fig(?:s)?\.|Figure(?:s)?)\s*[S]?\d+[a-zA-Z0-9,\s–\-]*\)", text))
    subj_fig = len(re.findall(r"(?:^|[.!?]\s+)(?:Extended Data |Supplementary )?(?:Fig(?:s)?\.|Figure(?:s)?)\s*[S]?\d+[a-zA-Z]?\s+(?:shows?|demonstrates?|illustrates?|depicts?|reveals?|presents?|displays?)", text, re.M))
    findings.append(("INFO", f"Results prose: {wc} words | Figure citations: {inline_fig} inline parenthetical vs {subj_fig} subject-style ('Fig. X shows')."))
    if subj_fig > 0:
        findings.append(("FAIL", f"Detected {subj_fig} subject-style figure citation(s) ('Fig. X shows...'); CNS ratio is 765:1 inline parenthetical '(Fig. 1a)'."))
    if inline_fig == 0 and wc > 120:
        findings.append(("WARN", "No parenthetical figure citations '(Fig. 1a)' detected in Results prose."))
    past_c = len(re.findall(r"\b(was|were|showed|revealed|demonstrated|identified|observed|found|exhibited|increased|reduced|induced|promoted|suppressed|inhibited|performed|analyzed|confirmed|established)\b", text, re.I))
    pres_c = len(re.findall(r"\b(is|are|shows|reveals|demonstrates|identifies|exhibits|increases|reduces|induces|promotes|suppresses|inhibits|confirms|establishes)\b", text, re.I))
    if pres_c > past_c and wc > 100:
        findings.append(("WARN", f"Present tense ({pres_c}) outweighs Past tense ({past_c}) in Results; CNS Results maintain ~4.9:1 Past:Present for empirical observations."))
    if re.search(r"\bdata not shown\b", text, re.I):
        findings.append(("WARN", "'data not shown' detected (only 2.9% of 2025-2026 CNS papers); consider moving to Extended Data / Supplementary Figures."))
    # Overclaiming on computational inference
    if re.search(r"\b(cellchat|nichenet|pseudotime|monocle|trajectory|correlation|kaplan|cox|tcga|bioinformatic)[^\.]{0,80}\b(proved|demonstrated causality|caused|drove)\b", text, re.I):
        findings.append(("FAIL", "Certainty Verb Ladder violation: strong causal verb ('proved/caused/drove') paired with correlative/computational analysis; downgrade to Tier 3/4 ('predicted/indicated/associated with')."))
    scan_chinglish(text, findings)
    return findings


def audit_discussion(text: str, spec: dict, journal: str):
    findings = []
    paras = [p.strip() for p in re.split(r"\n{2,}", text.strip()) if len(p.split()) >= 15]
    wc = count_words(text)
    findings.append(("INFO", f"Discussion: {wc} words across {len(paras)} paragraphs."))
    if paras:
        p1 = paras[0]
        if re.search(r"\b(p\s*[<=>]\s*0\.\d+|hr\s*=\s*\d|auc\s*=\s*0\.\d+|\d+\.\d+%)\b", p1, re.I):
            findings.append(("FAIL", "Discussion P1 repeats raw statistics (P/HR/AUC/%); 99.6% of top Discussions open with a conceptual synthesis without raw stat dumps."))
    if not re.search(r"\b(consistent with|in line with|in contrast to|unlike previous|previous studies|prior studies|prior work|in agreement with|whereas)\b", text, re.I):
        findings.append(("WARN", "No explicit literature comparison/triangulation stems detected ('Consistent with...', 'In contrast to...')."))
    has_lim = bool(re.search(r"\b(limitation|limitations of|several limitations|caveat|cannot rule out)\b", text, re.I))
    if spec["disc_lim_mandatory"] and not has_lim:
        findings.append(("FAIL", f"{journal} mandates explicit Limitations (Cell Press requires a dedicated 'Limitations of the study' subheading; Nat Med ~70%)."))
    elif not has_lim:
        findings.append(("WARN", "No explicit scope limitation or caveat detected; consider weaving a constructive 3-part limitation + next-step sentence."))
    if journal in ("cell", "cancer_cell") and not re.search(r"limitations of the study", text, re.I):
        findings.append(("WARN", "Cell Press expects the exact subheading 'Limitations of the study'."))
    if not re.search(r"\b(therapeutic|clinical|trial|patient stratification|biomarker|target|future studies|prospective|translation)\b", text, re.I):
        findings.append(("WARN", "No forward-looking clinical/translational or future-extension statement detected (present in 76.8% of oncology Discussions)."))
    scan_chinglish(text, findings)
    return findings


def audit_cover_letter(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"Cover Letter: {wc} words (target: 300-500 words, <=1 page)."))
    if wc > 550:
        findings.append(("FAIL", f"Cover Letter exceeds 1-page ceiling ({wc}w > 550w); editors triage in 30-60s—cut to 350-480w."))
    elif wc < 200:
        findings.append(("WARN", f"Cover Letter is very short ({wc}w); ensure core advance, journal fit, and all 4 compliance declarations are included."))
    if re.search(r"\b(dear sir|dear madam|to whom it may concern)\b", text, re.I):
        findings.append(("FAIL", "Generic salutation ('Dear Sir/Madam' / 'To Whom It May Concern'); address the specific Editor or 'Dear Editors of [Journal],'"))
    if re.search(r"\b(groundbreaking|paradigm-shifting|revolutionary|first ever|unprecedented|world-leading|extremely significant)\b", text, re.I):
        findings.append(("FAIL", "Empty hype superlative detected ('groundbreaking/revolutionary/first ever'); replace with restrained, evidence-anchored significance."))
    # 4 mandatory compliance statements
    if not re.search(r"\b(original|not been published|not under consideration|unpublished)\b", text, re.I):
        findings.append(("FAIL", "Missing Compliance #1: Originality & exclusivity statement ('not published elsewhere and not under consideration...')."))
    if not re.search(r"\b(all authors|approved)\b", text, re.I):
        findings.append(("WARN", "Missing Compliance #2: All-authors approval statement."))
    if not re.search(r"\b(competing\s+(?:financial\s+|non-financial\s+)?interests?|conflicts?\s+of\s+interest|financial\s+interests?)\b", text, re.I):
        findings.append(("FAIL", "Missing Compliance #3: Competing / conflict of interest declaration."))
    if not re.search(r"\b(ethics|irb|iacuc|helsinki|informed consent|approved by)\b", text, re.I):
        findings.append(("WARN", "Missing Compliance #4 (if human/animal data): IRB/IACUC ethics & informed consent note."))
    if not re.search(r"\b(readership|scope|recent|published in|et al\.,?\s*202\d)\b", text, re.I):
        findings.append(("WARN", "Missing explicit journal-scope fit / citation of 1-2 recent papers from the target journal."))
    return findings


def audit_caption(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"Figure Caption: {wc} words (target for {journal}: <={spec['cap_max_w']}w)."))
    if wc > spec["cap_max_w"]:
        findings.append(("WARN", f"Caption length ({wc}w) exceeds {journal} guideline ({spec['cap_max_w']}w); consolidate repeated stats into a closing sentence."))
    if re.search(r"\b(this figure shows|the figure illustrates|as shown in this figure)\b", text, re.I):
        findings.append(("FAIL", "Avoid 'This figure shows...'; use telegraphic participial syntax ('UMAP projection showing...', 'Box plots comparing...')."))
    if re.search(r"\b(box ?plot|violin|bar ?plot|scatter|kaplan|survival|quantification|comparison)\b", text, re.I):
        if not re.search(r"\bn\s*=\s*\d+|\b\d+\s+(patients|mice|samples|replicates|tumou?rs)\b", text, re.I):
            findings.append(("FAIL", "Quantitative plot detected without explicit sample size 'n' and biological unit."))
        if re.search(r"\bbox ?plot\b", text, re.I) and not re.search(r"\b(median|interquartile|iqr|whisker|quartile)\b", text, re.I):
            findings.append(("FAIL", "Box plot mentioned without defining center line (median), box bounds (IQR/quartiles), and whiskers."))
        if re.search(r"\b(error bar|mean|bar ?plot)\b", text, re.I) and not re.search(r"\b(s\.d\.|s\.e\.m\.|sd|sem|standard deviation|standard error|95%\s*ci)\b", text, re.I):
            findings.append(("WARN", "Error bars / means mentioned without defining dispersion metric (mean +/- s.d. or s.e.m.)."))
        if re.search(r"\bp\s*[<=>]|mann|wilcoxon|t-?test|anova|kruskal|log-?rank|fisher\b", text, re.I) and not re.search(r"\b(two-sided|two-tailed|one-sided|one-tailed)\b", text, re.I):
            findings.append(("WARN", "Statistical test cited without specifying sidedness ('two-sided' / 'two-tailed')."))
    if re.search(r"\b(immunofluorescence|mif|ihc|h&e|microscop|codex|imaging|histolog|spatial)\b", text, re.I) and not re.search(r"\bscale bar\b", text, re.I):
        findings.append(("FAIL", "Microscopy / tissue imaging panel detected without 'Scale bar, XX um' disclosure."))
    return findings


def audit_highlights(text: str, spec: dict, journal: str):
    findings = []
    bullets = [re.sub(r"^[-*•\d\.\)]\s*", "", ln).strip() for ln in text.strip().splitlines() if ln.strip()]
    findings.append(("INFO", f"Highlights: {len(bullets)} bullet(s) (Cell Press standard: 3-4 bullets, <=85 chars each)."))
    if len(bullets) < 3 or len(bullets) > 4:
        findings.append(("WARN", f"Bullet count ({len(bullets)}) outside Cell Press standard (3-4 bullets)."))
    over = [(i + 1, len(b), b) for i, b in enumerate(bullets) if len(b) > 85]
    for idx, ch, b in over:
        findings.append(("FAIL", f"Highlight #{idx} exceeds 85-character Cell Press hard limit ({ch} chars): '{b[:60]}...'"))
    return findings


def audit_in_brief(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    findings.append(("INFO", f"In brief / eTOC blurb: {wc} words (Cell Press hard limit: <=50 words, 3rd-person present tense)."))
    if wc > 55:
        findings.append(("FAIL", f"In brief exceeds 50-word Cell Press ceiling ({wc}w)."))
    if re.search(r"\b(we |our )\b", text, re.I):
        findings.append(("FAIL", "First-person ('we/our') detected in In brief; Cell Press requires 3rd-person ('Author et al. reveal that...')."))
    if not re.search(r"\b(et al\.|and colleagues)\b", text, re.I):
        findings.append(("WARN", "Standard Cell Press In brief opens with '[FirstAuthor] et al. [present verb]...' or '[FirstAuthor] and colleagues...'"))
    return findings


def audit_methods(text: str, spec: dict, journal: str):
    findings = []
    wc = count_words(text)
    passive = len(re.findall(r"\b(was|were)\s+[a-z]+(ed|en|wn|pt|lt)\b", text, re.I))
    active_we = len(re.findall(r"\bwe\s+[a-z]+(ed|d)\b", text, re.I))
    findings.append(("INFO", f"Methods: {wc} words | Past-passive ({passive}) vs Active 'we' ({active_we})."))
    if active_we > 0 and passive / max(1, active_we) < 2.0 and wc > 200:
        findings.append(("WARN", f"Active 'we' ratio is high ({passive}:{active_we}); CNS Methods average 9.89:1 past-passive dominance."))
    if re.search(r"\b(patient|human|biopsy|clinical|cohort|tumor specimen)\b", text, re.I) and not re.search(r"\b(irb|institutional review board|ethics committee|helsinki|informed consent)\b", text, re.I):
        findings.append(("FAIL", "Human specimens mentioned without IRB/ethics approval and written informed consent disclosure."))
    if re.search(r"\b(mouse|mice|murine|xenograft|pdx)\b", text, re.I) and not re.search(r"\b(iacuc|animal care|ethics committee|institutional animal)\b", text, re.I):
        findings.append(("FAIL", "Animal experiments mentioned without IACUC / institutional animal ethics approval."))
    if re.search(r"\b(cell line|hepg2|hela|a549|mcf7|hek293|cultured in dmem|rpmi)\b", text, re.I) and not re.search(r"\b(mycoplasma|str profiling|authenticated)\b", text, re.I):
        findings.append(("WARN", "Cell lines mentioned without STR authentication and routine mycoplasma testing disclosures."))
    if re.search(r"\b(seurat|scanpy|cell ranger|deseq2|harmony|star|bwa|gatk|cellchat|python|r\b)\b", text, re.I) and not re.search(r"\bv?\d+\.\d+(?:\.\d+)?\b", text):
        findings.append(("FAIL", "Bioinformatics software cited without exact version numbers (e.g., Seurat v4.3.0, R v4.3.2)."))
    if wc > 400 and not re.search(r"\b(data availability|code availability|github|zenodo|gse\d+|hra\d+|egas\d+|prjna\d+)\b", text, re.I):
        findings.append(("WARN", "No Data/Code Availability statement or repository accession (GEO/GSA/EGA/GitHub/Zenodo) detected."))
    if journal in ("cell", "cancer_cell") and wc > 500 and not re.search(r"key resources table|resource availability|quantification and statistical analysis", text, re.I):
        findings.append(("WARN", "Cell Press STAR Methods requires 'KEY RESOURCES TABLE', 'RESOURCE AVAILABILITY', and 'QUANTIFICATION AND STATISTICAL ANALYSIS'."))
    return findings


def split_full_manuscript(text: str):
    """Split a Markdown/plain manuscript by top-level section headers for --section all."""
    sec_map = {
        "title": "title", "abstract": "abstract", "summary": "abstract",
        "highlights": "highlights", "in brief": "in_brief", "etoc": "in_brief",
        "introduction": "intro", "results": "results", "subheadings": "subheadings",
        "discussion": "discussion", "cover letter": "cover_letter",
        "figure caption": "caption", "figure captions": "caption", "figure legend": "caption",
        "methods": "methods", "star methods": "methods", "materials and methods": "methods",
    }
    sections = {}
    cur = None
    buf = []
    for ln in text.splitlines():
        m = re.match(r"^#{1,2}\s+(.+)$", ln.strip())
        if m:
            hdr = m.group(1).strip().lower().rstrip(":")
            matched = next((v for k, v in sec_map.items() if hdr == k or hdr.startswith(k)), None)
            if matched:
                if cur and buf:
                    sections[cur] = "\n".join(buf).strip()
                cur = matched
                buf = []
                continue
        if cur:
            buf.append(ln)
    if cur and buf:
        sections[cur] = "\n".join(buf).strip()
    # Extract Results H3 subheadings automatically if present
    if "results" in sections and "subheadings" not in sections:
        shs = re.findall(r"^###\s+(.+)$", sections["results"], re.M)
        if shs:
            sections["subheadings"] = "\n".join(shs)
    return sections


SCAFFOLDS = {
    "mechanistic": """# Manuscript Strategic Scaffold — Mechanistic Axis + Perturbation ({journal})

## Title (Target: {title_w}w | Declarative Causal Clause — 84.3% CNS norm)
- Option 1 (Causal): [Driver/Metabolite/Axis] drives/reprograms [phenotype] via [pathway] in [cancer]
- Option 2 (Therapeutic): Targeting [axis] overcomes [resistance] by restoring [immune/cell state]

## Abstract (Target: {abs_w}w | Hook: Fundamental Biology Paradox — 68.5%)
- [S1-S2 Background + Gap] Broad biological premise -> However, how [X] drives [Y] remains poorly understood.
- [S3 Pivot + <=1s Method] Here, combining [single-cell/spatial profiling] with [in vivo genetic perturbation], we show that [main finding].
- [S4-S6 Quantitative Escalation (~50%)] (1) Cell-state/niche discovery (n = ...); (2) Mechanistic axis; (3) In vivo KO/rescue + human cohort validation.
- [S7 Implication] Together, these findings establish [X-Y axis] and nominate [target] for [cancer] therapy.

## Introduction (Target: 3-4 paras, ~450-530w | Reverse-Engineered from Results!)
- P1 (Broad Stakes — <=10% Results entities): Clinical/biological importance of [cancer/process].
- P2 (Focused Entities — ~37% Results entities): Known biology of ONLY the 2-3 core entities in Results.
- P3 (Strong Mechanistic Gap — 78.7%): However, the causal mechanism linking [A] to [B] remains elusive -> Question/Hypothesis.
- P4 (Approach & Preview): Here, we integrated [...] and demonstrate that [...].

## Results Subheadings (6-7 Domino Modules)
- H1: [Unbiased discovery / human cohort phenotype]
- H2: [Spatial localization / key cellular niche]
- H3: [Transcriptional / metabolic / signaling signature]
- H4: [Upstream driver / molecular interaction]
- H5: [In vivo genetic KO/depletion establishes causal necessity]
- H6: [Pharmacological blockade synergizes with standard therapy / anti-PD-1]
- H7: [Human clinical cohort validation & prognostic relevance]

## Discussion (MIT/Harvard 5-Block Elevation — ZERO raw P values in P1!)
- P1: Unified conceptual model answering Introduction's big question.
- P2: Literature triangulation & paradox reconciliation ('Whereas prior studies..., our data...').
- P3: Mechanistic implications & open upstream/downstream questions.
- P4: Actionable translational roadmap (delivery, combination regimen, patient selection).
- P5 / Limitations of the study: 3-Part Constructive Limitations (Boundary -> Mitigation -> Next step) + Forward-looking close.

## Cover Letter (350-450w, 1 page)
- P1: Targeted Editor salutation + Title + Article type.
- P2: Core paradox resolved + flagship causal evidence (NOT mini-abstract).
- P3: Target journal scope fit + cite 1-2 recent papers in {journal}.
- P4: 4 Compliance statements (Originality, Authorship approval, COI, IRB/IACUC).
""",
    "clinical": """# Manuscript Strategic Scaffold — Clinical Biomarker / Immunotherapy ({journal})

## Title (Target: {title_w}w | Nat Med: Conservative + Colon Trial/Cohort Design; Cancer Cell: Declarative)
- Option 1 (Clinical): [Biomarker / Regimen] in [patient population]: [a phase 1/2 trial / multi-cohort study]
- Option 2 (Translational): [Spatial/Cellular signature] predicts/shapes response and resistance to [therapy] in [cancer]

## Abstract (Target: {abs_w}w | Hook: Clinical Burden / Treatment Resistance — 66.1%)
- [S1-S2] High mortality / low durable response to [standard of care]; predictive biomarkers or resistance mechanisms remain unclear.
- [S3] Here, we profiled [n patients, pre/on-treatment] using [modalities] across [discovery + external validation cohorts].
- [S4-S6] (1) Responder vs non-responder cellular/spatial hallmark (with n, AUC/HR, P); (2) Mechanistic correlate; (3) Independent validation & clinical utility.
- [S7] These findings inform patient stratification and rational combination strategies for [cancer].

## Introduction (3-4 paras | Gap: Clinical Resistance / Biomarker Failure — 71.0%)
- P1: Clinical standard of care & durability/response bottleneck.
- P2: Limitations of existing biomarkers (e.g., PD-L1/TMB) and prior bulk cohorts.
- P3: Sharp clinical/mechanistic gap -> study objective.
- P4: Cohort design + top-line predictive & biological discoveries.

## Results Subheadings (6-7 Clinical -> Mechanistic -> Validation Modules)
- H1: Cohort design, clinical characteristics, and primary outcomes
- H2: Baseline TME / cellular states associated with treatment response
- H3: On-treatment longitudinal remodeling in responders vs non-responders
- H4: Spatial architecture / immune niches distinguishing durable benefit
- H5: Development and external multi-center validation of predictive signature
- H6: Preclinical / mechanistic validation of resistance target

## Discussion (Primary Gravity: Clinical Translation 34.4% + Cohort Limitations 10.2%)
- P1: Conceptual clinical synthesis (zero raw stat dumps).
- P2: Comparison with landmark clinical trials & prior biomarkers.
- P3: Clinical deployment pathway (FFPE/H&E/cfDNA feasibility, adaptive trial design).
- P4 / Limitations of the study: Cohort size/heterogeneity/retrospective caveats -> External validation mitigation -> Prospective trial roadmap.
""",
    "atlas": """# Manuscript Strategic Scaffold — Single-Cell / Spatial Atlas Resource ({journal})

## Title (Target: {title_w}w | Atlas/Landscape NP or Atlas + Verb Hybrid)
- Option 1 (Hybrid): Single-cell and spatial atlas of [cancer] reveals [key ecotype/vulnerability]
- Option 2 (Pure Resource): Pan-cancer human [organ/stage] atlas at single-cell and spatial resolution

## Abstract (Target: {abs_w}w | Hook: TME Architecture 64.5% + Resolution Blindspot 12.8%)
- [S1-S2] TME heterogeneity governs [cancer] progression, yet limited cohort scale and lack of spatial context have hindered systematic mapping.
- [S3] Here, we integrate [N cells, M samples, spatial + scRNA-seq] across [stages/lineages].
- [S4-S6] (1) Recurrent malignant metaprograms; (2) Distinct multicellular ecotypes/niches; (3) Clinical prognosis & therapeutic vulnerability validated orthogonally.
- [S7] This atlas defines shared hallmarks of [disease] and provides a foundational resource for precision oncology.

## Results Subheadings (6-7 Multi-Scale Modules)
- H1: Construction of a multi-omic single-cell and spatial atlas of [disease]
- H2: Recurrent malignant cell states and transcriptional metaprograms
- H3: Remodeling of myeloid and lymphoid immune compartments
- H4: Spatial multicellular neighborhoods and tumor-stroma boundary niches
- H5: Ligand-receptor crosstalk hubs driving immunosuppression
- H6: Distinct TME ecotypes stratify patient survival and therapy response
- H7: Orthogonal mIF / functional validation of lead niche target

## Discussion (Resource Generality 14.7% — 2x higher than Mechanistic!)
- P1: Overarching spatial/ecological organizing principles uncovered by the atlas.
- P2-P3: Cross-cancer generality & reconciliation with prior bulk/small single-cell studies.
- P4: Community utility of the open portal & translational targeting opportunities.
- P5 / Limitations of the study: Treatment-naive balance, panel gene coverage, unmatched longitudinal sampling -> Mitigation & next-gen whole-transcriptome spatial roadmap.
""",
    "evolution": """# Manuscript Strategic Scaffold — Clonal Evolution / Metastasis / Plasticity ({journal})

## Title (Target: {title_w}w | Topic NP 45% or Declarative 44% or Gerund 'Tracking...')
- Option 1 (Gerund): Tracking clonal evolution from precancer to metastasis in [cancer] using [modality]
- Option 2 (Causal): [Metabolic/Niche cue] drives clonal selection and metastatic plasticity in [cancer]

## Abstract (Target: {abs_w}w | Hook: Evolutionary Principle 61.2% + Relapse/Interception 37.5%)
- Focus on pre-existing vs de novo selection, longitudinal trajectory across stages (normal -> precancer -> invasive -> metastasis/recurrence), and early interception window.

## Results Subheadings (6-7 Temporal / Lineage Arc)
- H1: Longitudinal cohort / lineage-tracing architecture
- H2: Genomic & clonal phylogeny across disease stages
- H3: Non-genetic transcriptional plasticity & state transitions
- H4: Microenvironmental co-evolution along the progression trajectory
- H5: Stage-specific driver / resistance clone selection under therapy
- H6: Preclinical interception or adaptive targeting at the vulnerable window

## Discussion (Evolutionary Dynamics 44.9% + Literature Paradigm Contrast 18.0%)
- Contrast linear vs branched/punctuated evolution; reconcile genetic vs epigenetic plasticity; propose evolution-informed adaptive trials or precancer interception.
""",
    "method": """# Manuscript Strategic Scaffold — Computational Tool / AI Foundation Model / Assay ({journal})

## Title (Target: {title_w}w | Nat Methods: Colon Tool Brand 37.5%)
- Option 1 (Brand): [ToolName]: [capability] bridging [modality A] and [modality B]
- Option 2 (Functional NP): A [visual-omics / foundation] model to [solve bottleneck] at single-cell resolution

## Abstract (Target: {abs_w}w | Hook: Technical/Omics Bottleneck — 36.4%, 36x Mechanistic!)
- [S1-S2] Concrete trade-off (resolution vs cost/scalability/modality gap).
- [S3] Here, we present [ToolName], a [architecture/assay] trained/engineered on [scale].
- [S4-S6] (1) Benchmark superiority across X datasets & Y baselines; (2) Distinct modular capabilities; (3) Novel biological/clinical discovery enabled by [ToolName].
- [S7] Open-source availability and broad applicability across tissues and diseases.

## Results Subheadings (6-7 Modular Benchmark + Discovery Chain)
- H1: Overview of [ToolName] architecture and representation learning
- H2: Benchmark 1 — [ToolName] outperforms existing methods in [core task A]
- H3: Benchmark 2 — [ToolName] generalizes across platforms/cohorts in [task B]
- H4: Scalability, runtime, and robustness under noise/dropout
- H5: Biological discovery 1 — applying [ToolName] to [clinical cancer cohort]
- H6: Biological discovery 2 — orthogonal experimental/clinical validation

## Discussion (Method Generality 30.6% + Rigorous Technical Limitations 12.4%)
- Highlight extensibility to new modalities, computational efficiency, failure modes/boundary conditions (batch shift, rare cell types, training bias), and open-source ecosystem roadmap.
""",
}


def run_audit(section: str, journal: str, text: str) -> int:
    spec = JOURNAL_SPECS[journal]
    dispatch = {
        "title": audit_title,
        "abstract": audit_abstract,
        "highlights": audit_highlights,
        "in_brief": audit_in_brief,
        "intro": audit_intro,
        "subheadings": audit_subheadings,
        "results": audit_results,
        "discussion": audit_discussion,
        "cover_letter": audit_cover_letter,
        "caption": audit_caption,
        "methods": audit_methods,
    }
    total_fail = 0
    total_warn = 0

    if section == "all":
        parts = split_full_manuscript(text)
        if not parts:
            print("[ERROR] Could not detect markdown '# Section' headers (e.g., '# Title', '# Abstract', '# Introduction', '# Results', '# Discussion', '# Cover Letter', '# Figure Captions', '# Methods').")
            return 2
        to_check = [(k, v) for k, v in parts.items() if k in dispatch]
    else:
        to_check = [(section, text)]

    print(f"=== CNS Manuscript Audit | Journal: {journal} | Sections: {', '.join(k for k,_ in to_check)} ===")
    for sec_name, sec_txt in to_check:
        res = dispatch[sec_name](sec_txt, spec, journal)
        print(f"\n[{sec_name.upper()}]")
        for level, msg in res:
            print(f"  [{level:4s}] {msg}")
            if level == "FAIL":
                total_fail += 1
            elif level == "WARN":
                total_warn += 1

    print(f"\n--- SUMMARY: {total_fail} FAIL(s), {total_warn} WARN(s) ---")
    return 1 if total_fail > 0 else 0


def main():
    p = argparse.ArgumentParser(description="CNS Scientific Manuscript Auditor & Storyline Scaffolder")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("audit", help="Audit a manuscript section or full markdown manuscript")
    pa.add_argument("--section", required=True, choices=["title", "abstract", "highlights", "in_brief", "intro", "results", "subheadings", "discussion", "cover_letter", "caption", "methods", "all"])
    pa.add_argument("--journal", default="nature", choices=list(JOURNAL_SPECS.keys()))
    pa.add_argument("--file", required=True, help="Path to draft text/markdown file")

    ps = sub.add_parser("scaffold", help="Generate a strategic narrative scaffold by study archetype")
    ps.add_argument("--archetype", required=True, choices=list(SCAFFOLDS.keys()))
    ps.add_argument("--journal", default="cancer_cell", choices=list(JOURNAL_SPECS.keys()))

    args = p.parse_args()
    if args.cmd == "scaffold":
        spec = JOURNAL_SPECS[args.journal]
        print(SCAFFOLDS[args.archetype].format(
            journal=args.journal,
            title_w=spec["title_max_w"],
            abs_w=spec["abs_max_w"],
        ))
        return 0
    else:
        txt = Path(args.file).read_text(encoding="utf-8")
        return run_audit(args.section, args.journal, txt)


if __name__ == "__main__":
    sys.exit(main())
