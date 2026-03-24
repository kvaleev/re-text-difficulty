#!/usr/bin/env python3
"""
Interpretable rule extraction experiment: extract per-category decision rules
from the 19-metric feature space.

Instead of the unmaintained skope-rules package, this uses sklearn's
DecisionTreeClassifier (shallow, one-vs-rest) to produce interpretable rules.
Each tree is constrained to max_depth=3, giving at most 8 leaf nodes —
shallow enough to read as IF-THEN rules.

For each category (one-vs-rest):
  1. Fit a shallow decision tree
  2. Extract all paths that predict the positive class
  3. Report precision/recall of each path on training data
  4. Compare rules with and without length-proxy metrics

Usage:
    python skope_rules_experiment.py [path/to/results.csv]
"""

import sys
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import precision_recall_fscore_support, accuracy_score


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
EXCLUDED_METRICS = [
    'Structure score 0-100 (Structure)',
    'Readiness score 0-100 (Requirements)',
    'Flesch Reading Ease 0-100 (Readability)',
    'Flesch-Kincaid grade level (Readability)',
    'ARI grade level (Readability)',
    'Gunning Fog grade level (Readability)',
    'SMOG grade level (Readability)',
    'Coleman-Liau grade level (Readability)',
]

CATEGORY_NAMES = {
    'small_prd_files': 'Small PRD',
    'prd_files': 'Long PRD',
    'pure_raw_markdown': 'PURE',
    'non_related_github': 'GitHub Articles',
    'non_related_wikipedia_samples': 'Wikipedia',
}

SHORT_METRIC = {
    'Entity persistence ratio (Entity Coherence)': 'entity_persist',
    'PU score (Entity Coherence)': 'pu_score',
    'PW score (Entity Coherence)': 'pw_score',
    'PACC uniform (Entity Coherence)': 'pacc_uniform',
    'PACC weighted (Entity Coherence)': 'pacc_weighted',
    'Avg entities/sentence (Entity Coherence)': 'entities_per_sent',
    'Total entities (Entity Coherence)': 'total_entities',
    'Sentences analyzed (Entity Coherence)': 'sentences_analyzed',
    'Consensus grade level (Readability)': 'grade_level',
    'Headings per sentence (Structure)': 'headings_per_sent',
    'Headings count (Structure)': 'heading_count',
    'Lists per sentence (Structure)': 'lists_per_sent',
    'List items count (Structure)': 'list_items',
    'SMAO sentences count (Requirements)': 'smao_count',
    'SMAO sentences % (Requirements)': 'smao_pct',
    'Vague words per sentence (Requirements)': 'vague_per_sent',
    'Anaphora per sentence (Requirements)': 'anaphora_per_sent',
    'Sentence CV (Requirements)': 'sentence_cv',
    'CPRE terms per sentence (CPRE)': 'cpre_per_sent',
}

LENGTH_PROXIES = {
    'Sentences analyzed (Entity Coherence)',
    'Total entities (Entity Coherence)',
}


def display_name(internal: str) -> str:
    return CATEGORY_NAMES.get(internal, internal)


def short_name(metric: str) -> str:
    return SHORT_METRIC.get(metric, metric.split('(')[0].strip())


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_data(path: str) -> tuple:
    df = pd.read_csv(path)
    df['Subfolder'] = df['Subfolder'].fillna('(root)').replace('', '(root)')

    numeric_cols = []
    for col in df.columns:
        if col in ('Subfolder', 'File', 'Interpretation (Readability)'):
            continue
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if not df[col].isna().all() and col not in EXCLUDED_METRICS:
            numeric_cols.append(col)

    print(f"Loaded {len(df)} documents, {len(numeric_cols)} metrics, "
          f"{df['Subfolder'].nunique()} categories\n")
    return df, numeric_cols


# ---------------------------------------------------------------------------
# Rule extraction from a decision tree
# ---------------------------------------------------------------------------
def extract_rules(tree, feature_names: list[str], class_label: str) -> list[dict]:
    """
    Walk all root-to-leaf paths in a fitted DecisionTreeClassifier.
    Return paths where the predicted class is 1 (positive).
    With class_weight='balanced', value stores weighted counts —
    so we use the tree's own predicted class instead.
    """
    tree_ = tree.tree_
    rules = []

    def recurse(node, conditions):
        # Leaf node
        if tree_.children_left[node] == tree_.children_right[node]:
            predicted_class = np.argmax(tree_.value[node][0])
            n_samples = int(tree_.n_node_samples[node])
            weighted_vals = tree_.value[node][0]
            # confidence = proportion of weighted votes for predicted class
            confidence = weighted_vals[predicted_class] / weighted_vals.sum()
            if predicted_class == 1 and n_samples >= 2:
                rules.append({
                    'conditions': list(conditions),
                    'rule': ' AND '.join(conditions),
                    'confidence': float(confidence),
                    'n_samples': n_samples,
                })
            return

        feat = feature_names[tree_.feature[node]]
        thresh = tree_.threshold[node]

        # Left child: feature <= threshold
        conditions.append(f"{feat} <= {thresh:.3f}")
        recurse(tree_.children_left[node], conditions)
        conditions.pop()

        # Right child: feature > threshold
        conditions.append(f"{feat} > {thresh:.3f}")
        recurse(tree_.children_right[node], conditions)
        conditions.pop()

    recurse(0, [])
    return sorted(rules, key=lambda r: (-r['confidence'], -r['n_samples']))


# ---------------------------------------------------------------------------
# One-vs-rest rule extraction with cross-validated evaluation
# ---------------------------------------------------------------------------
def run_rules_for_category(df, feature_cols, short_cols, X, y_binary,
                           cat_name, max_depth=3):
    """Fit tree, extract rules, cross-validate, print results."""
    n_pos = y_binary.sum()
    n_neg = len(y_binary) - n_pos

    print(f"{'='*70}")
    print(f"Category: {cat_name}  (n_pos={n_pos}, n_neg={n_neg})")
    print(f"{'='*70}")

    # Fit on full data for rule extraction
    dt = DecisionTreeClassifier(
        max_depth=max_depth,
        min_samples_leaf=max(3, int(0.02 * len(y_binary))),
        class_weight='balanced',
        random_state=42,
    )
    dt.fit(X.values, y_binary.values)

    # Cross-validated performance of the tree
    n_splits = min(5, min(n_pos, n_neg))
    if n_splits >= 2:
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
        y_pred_cv = cross_val_predict(dt, X.values, y_binary.values, cv=skf)
        prec_cv, rec_cv, f1_cv, _ = precision_recall_fscore_support(
            y_binary.values, y_pred_cv, pos_label=1, average='binary',
            zero_division=0
        )
        acc_cv = accuracy_score(y_binary.values, y_pred_cv)
        print(f"  CV Performance: Acc={acc_cv:.3f}  P={prec_cv:.3f}  "
              f"R={rec_cv:.3f}  F1={f1_cv:.3f}")
    else:
        print(f"  (too few samples for cross-validation)")

    # Print tree structure
    tree_text = export_text(dt, feature_names=short_cols, decimals=2)
    print(f"\n  Decision tree:\n")
    for line in tree_text.strip().split('\n'):
        print(f"    {line}")

    # Extract readable rules
    rules = extract_rules(dt, short_cols, cat_name)
    print(f"\n  Extracted rules (positive-class paths):")
    if not rules:
        print("    (no rules predicting this category)")
    for i, r in enumerate(rules):
        print(f"    Rule {i+1}: IF {r['rule']}")
        print(f"      → Confidence={r['confidence']:.3f}  "
              f"({r['n_samples']} samples)")

    # Feature importance from tree
    importances = pd.Series(dt.feature_importances_, index=short_cols)
    importances = importances[importances > 0].sort_values(ascending=False)
    print(f"\n  Feature importance (tree splits):")
    for feat, imp in importances.items():
        print(f"    {feat:25s}  {imp:.3f}")

    print()
    return rules


def run_experiment(df, feature_cols, label: str, max_depth=3):
    """Run one-vs-rest rule extraction for all categories."""
    X = df[feature_cols].copy()
    for col in X.columns:
        X[col] = X[col].fillna(X[col].median())

    rename_map = {col: short_name(col) for col in feature_cols}
    X_short = X.rename(columns=rename_map)
    short_cols = list(X_short.columns)

    categories = sorted(df['Subfolder'].unique())
    all_results = {}

    print(f"\n{'#'*70}")
    print(f"  {label}")
    print(f"  {len(feature_cols)} features, max_depth={max_depth}")
    print(f"{'#'*70}\n")

    for cat in categories:
        y_binary = (df['Subfolder'] == cat).astype(int)
        rules = run_rules_for_category(
            df, feature_cols, short_cols, X_short, y_binary,
            display_name(cat), max_depth=max_depth
        )
        all_results[cat] = rules

    return all_results


# ---------------------------------------------------------------------------
# Composition analysis
# ---------------------------------------------------------------------------
def analyze_composition(all_results: dict, feature_cols: list[str]):
    print(f"\n{'='*70}")
    print("RULE COMPOSITION SUMMARY")
    print(f"{'='*70}\n")

    metric_counts = {}
    total_rules = 0

    for cat, rules in all_results.items():
        for r in rules:
            total_rules += 1
            for cond in r['conditions']:
                # Extract metric name (everything before <= or >)
                metric = cond.split(' <= ')[0].split(' > ')[0].strip()
                metric_counts[metric] = metric_counts.get(metric, 0) + 1

    if total_rules == 0:
        print("No rules extracted. Trees may only predict negative class.\n")
        return

    length_proxy_short = {short_name(m) for m in LENGTH_PROXIES}
    length_count = sum(v for k, v in metric_counts.items()
                       if k in length_proxy_short)

    print(f"Total rules: {total_rules}")
    print(f"Conditions involving length proxies: {length_count}")
    print()

    print("Metric frequency in rule conditions:")
    for metric, count in sorted(metric_counts.items(), key=lambda x: -x[1]):
        tag = " [LENGTH]" if metric in length_proxy_short else ""
        print(f"  {metric:25s}  {count:2d} conditions{tag}")

    print()
    for cat, rules in all_results.items():
        if not rules:
            print(f"  {display_name(cat):20s}: (no positive rules)")
            continue
        metrics_used = set()
        for r in rules:
            for cond in r['conditions']:
                m = cond.split(' <= ')[0].split(' > ')[0].strip()
                metrics_used.add(m)
        content_metrics = metrics_used - length_proxy_short
        print(f"  {display_name(cat):20s}: {', '.join(sorted(content_metrics)) or '(length only)'}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'results/results.csv'
    df, feature_cols = load_data(path)

    # 1. All 19 metrics
    results_all = run_experiment(df, feature_cols, "ALL 19 METRICS")
    analyze_composition(results_all, feature_cols)

    # 2. Without length proxies (17 metrics)
    no_length_cols = [c for c in feature_cols if c not in LENGTH_PROXIES]
    results_no_len = run_experiment(df, no_length_cols,
                                   "WITHOUT LENGTH PROXIES (17 metrics)")
    analyze_composition(results_no_len, no_length_cols)


if __name__ == '__main__':
    main()
