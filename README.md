# re-text-difficulty

Replication package for the paper *"Evaluating the Impact of Input Text Properties on LLM-Based Requirements Extraction"* (RE@Next! 2026).

This repository contains the text analysis framework and dataset used to characterize input document difficulty along five dimensions: entity coherence, readability, document structure, requirements formality, and professional vocabulary. The framework computes 19 metrics per document and provides statistical and machine-learning analyses to validate that these metrics produce distinguishable document profiles.

## Repository Structure

```
re-text-difficulty/
├── src/
│   ├── master_analyzer.py          # Runs all 5 analyzers on input documents
│   └── analyzers/
│       ├── entity_coherence_analyzer.py   # TRUNAJOD Entity Grid (Barzilay & Lapata 2008)
│       ├── readability_analyzer.py        # 6 readability formulas + consensus grade
│       ├── structure_analyzer.py          # Heading/list density and hierarchy
│       ├── requirements_readiness_analyzer.py  # SMAO, vague words, anaphora, sentence CV
│       └── cpre_glossary_analyzer.py      # 198 IREB CPRE terms
├── scripts/
│   ├── analyze_results.py          # ANOVA, Random Forest, correlation, figures
│   ├── metric_redundancy.py        # PCA, hierarchical clustering, redundancy analysis
│   ├── skope_rules_experiment.py   # Per-category interpretable decision rules
│   └── generate_rule_heatmap.py    # Feature importance heatmap for paper
├── data/
│   └── results.csv                 # Pre-computed metrics for 376 documents
├── requirements.txt
├── LICENSE
└── README.md
```

## Dataset

`data/results.csv` contains pre-computed metrics for 376 documents across five categories:

| Category | n | Description |
|----------|---|-------------|
| Small PRD | 225 | Short product requirements documents from GitHub |
| PURE | 76 | Requirements from the PURE dataset (Napolitano et al., 2021) |
| GitHub Articles | 51 | Non-requirements GitHub README files |
| Wikipedia | 13 | Wikipedia articles (negative control) |
| Long PRD | 11 | Large multi-section product requirements documents |

Each row includes 28 raw metrics, a human-readable category label, and a `Source` column with a link to the original document (GitHub URL or dataset reference). The original documents are not redistributed; the `Source` column allows retrieval.

### Metrics (19 used in statistical analysis)

After excluding 2 composite scores and 6 redundant readability formulas (see paper Section 5), 19 metrics are retained:

**Entity Coherence (8):** PW score, PU score, PACC uniform, PACC weighted, avg entities/sentence, total entities, sentences analyzed, entity persistence ratio

**Readability (1):** Consensus grade level

**Structure (4):** Headings count, headings/sentence, list items count, lists/sentence

**Requirements (5):** SMAO count, SMAO %, vague words/sentence, anaphora/sentence, sentence CV

**CPRE (1):** CPRE terms/sentence

## Quick Start

### Installation

```bash
git clone https://github.com/anonymous/re-text-difficulty.git
cd re-text-difficulty
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Reproduce the paper's statistical analysis

```bash
# From the repo root:
python scripts/analyze_results.py data/results.csv
```

This produces:
- `analysis_output/analysis_report.txt` — ANOVA results, classification report, feature importance
- `analysis_output/confusion_matrix.png` — Cross-validated confusion matrix (Fig. 2 in paper)
- `analysis_output/feature_importance.png` — Random Forest feature importance
- `analysis_output/subfolder_radar.png` — Radar chart of category profiles

### Reproduce the redundancy analysis

```bash
python scripts/metric_redundancy.py data/results.csv
```

Outputs PCA scree plot, hierarchical clustering, and correlated pairs.

### Reproduce the interpretable rule extraction

```bash
python scripts/skope_rules_experiment.py data/results.csv
python scripts/generate_rule_heatmap.py data/results.csv analysis_output/rule_importance_heatmap.png
```

### Analyze your own documents

```bash
# Place documents in input/
mkdir -p input
cp your_document.md input/

# Run the analysis pipeline
cd src
python master_analyzer.py

# Results appear in results/ (per-document JSONs) and results/results.csv
```

## Key Results (Stage 1)

- All 19 metrics significantly discriminate between document categories (Welch's ANOVA, BH-corrected p < 0.05)
- Random Forest achieves 93.09% cross-validated accuracy (macro F1 = 0.865, weighted F1 = 0.928)
- Removing length-proxy metrics (sentences_analyzed, total_entities) improves Small PRD F1 from 0.931 to 0.957, confirming content metrics carry discriminative signal independently of document size
- PCA shows 19 metrics span ~10 independent axes; substantial within-dimension redundancy exists (e.g., PW Score and PACC Uniform at rho = 0.96)
- Each category is characterized by a distinct metric subset (see Fig. 1 in paper)

## Citation

```bibtex
@inproceedings{anonymous2026textdifficulty,
  title     = {Evaluating the Impact of Input Text Properties on LLM-Based Requirements Extraction},
  author    = {Anonymous},
  booktitle = {Proceedings of the 34th IEEE International Requirements Engineering Conference (RE@Next! Track)},
  year      = {2026}
}
```

## License

MIT. See [LICENSE](LICENSE).
