#!/usr/bin/env python3
"""
Generate a heatmap figure showing per-category feature importance
from shallow decision trees (one-vs-rest, without length proxies).
Suitable for inclusion in the RE@Next! paper.
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------------------
# Config (mirrors analyze_results.py)
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

LENGTH_PROXIES = {
    'Sentences analyzed (Entity Coherence)',
    'Total entities (Entity Coherence)',
}

CATEGORY_NAMES = {
    'small_prd_files': 'Small PRD',
    'prd_files': 'Long PRD',
    'pure_raw_markdown': 'PURE',
    'non_related_github': 'GitHub Articles',
    'non_related_wikipedia_samples': 'Wikipedia',
}

# Order categories by domain relevance (requirements first, then non-RE)
CATEGORY_ORDER = [
    'small_prd_files',
    'prd_files',
    'pure_raw_markdown',
    'non_related_github',
    'non_related_wikipedia_samples',
]

SHORT_METRIC = {
    'Entity persistence ratio (Entity Coherence)': 'Entity Persistence',
    'PU score (Entity Coherence)': 'PU Score',
    'PW score (Entity Coherence)': 'PW Score',
    'PACC uniform (Entity Coherence)': 'PACC Uniform',
    'PACC weighted (Entity Coherence)': 'PACC Weighted',
    'Avg entities/sentence (Entity Coherence)': 'Entities/Sent',
    'Consensus grade level (Readability)': 'Grade Level',
    'Headings per sentence (Structure)': 'Headings/Sent',
    'Headings count (Structure)': 'Heading Count',
    'Lists per sentence (Structure)': 'Lists/Sent',
    'List items count (Structure)': 'List Items',
    'SMAO sentences count (Requirements)': 'SMAO Count',
    'SMAO sentences % (Requirements)': 'SMAO %',
    'Vague words per sentence (Requirements)': 'Vague/Sent',
    'Anaphora per sentence (Requirements)': 'Anaphora/Sent',
    'Sentence CV (Requirements)': 'Sentence CV',
    'CPRE terms per sentence (CPRE)': 'CPRE/Sent',
}


def short_name(m):
    return SHORT_METRIC.get(m, m.split('(')[0].strip())


def display_name(c):
    return CATEGORY_NAMES.get(c, c)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'results/results.csv'
    output_path = sys.argv[2] if len(sys.argv) > 2 else 'analysis_output/rule_importance_heatmap.png'

    # Load data
    df = pd.read_csv(path)
    df['Subfolder'] = df['Subfolder'].fillna('(root)').replace('', '(root)')

    numeric_cols = []
    for col in df.columns:
        if col in ('Subfolder', 'File', 'Interpretation (Readability)'):
            continue
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if (not df[col].isna().all()
                and col not in EXCLUDED_METRICS
                and col not in LENGTH_PROXIES):
            numeric_cols.append(col)

    # Prepare features
    X = df[numeric_cols].copy()
    for col in X.columns:
        X[col] = X[col].fillna(X[col].median())

    # Fit one-vs-rest trees, collect importance
    importance_matrix = {}

    for cat in CATEGORY_ORDER:
        if cat not in df['Subfolder'].values:
            continue
        y_binary = (df['Subfolder'] == cat).astype(int)

        dt = DecisionTreeClassifier(
            max_depth=3,
            min_samples_leaf=max(3, int(0.02 * len(y_binary))),
            class_weight='balanced',
            random_state=42,
        )
        dt.fit(X.values, y_binary.values)

        imp = pd.Series(dt.feature_importances_, index=numeric_cols)
        importance_matrix[display_name(cat)] = imp

    imp_df = pd.DataFrame(importance_matrix).T
    imp_df.columns = [short_name(c) for c in imp_df.columns]

    # Drop metrics that are zero everywhere
    imp_df = imp_df.loc[:, (imp_df > 0).any(axis=0)]

    # Sort columns by total importance (most important first)
    col_order = imp_df.sum(axis=0).sort_values(ascending=False).index
    imp_df = imp_df[col_order]

    # Plot — sized for IEEE two-column format
    fig, ax = plt.subplots(figsize=(7, 3.2))

    sns.heatmap(
        imp_df,
        annot=True,
        fmt='.2f',
        cmap='YlOrRd',
        linewidths=0.5,
        linecolor='white',
        cbar_kws={'label': 'Feature Importance', 'shrink': 0.8},
        ax=ax,
        vmin=0,
        vmax=1,
        annot_kws={'size': 9},
    )

    ax.set_title('Per-Category Feature Importance (Decision Tree, depth ≤ 3)',
                 fontsize=12, fontweight='bold', pad=10)
    ax.set_ylabel('')
    ax.set_xlabel('')
    ax.tick_params(axis='x', labelsize=9, rotation=35)
    ax.tick_params(axis='y', labelsize=10, rotation=0)
    plt.setp(ax.get_xticklabels(), ha='right')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved to {output_path}")
    print(f"\nImportance matrix:\n{imp_df.to_string()}")


if __name__ == '__main__':
    main()
