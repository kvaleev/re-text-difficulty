#!/usr/bin/env python3
"""
Metric redundancy analysis: identify which of the 19 metrics measure
overlapping constructs.

Produces:
1. Spearman correlation matrix with hierarchical clustering
2. Highly correlated pairs (|r| > threshold)
3. PCA — effective dimensionality (how many independent axes?)
4. Factor loadings — which metrics load on which latent dimensions

Usage:
    python metric_redundancy.py [path/to/results.csv]
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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

SHORT_METRIC = {
    'Entity persistence ratio (Entity Coherence)': 'Entity Persist.',
    'PU score (Entity Coherence)': 'PU Score',
    'PW score (Entity Coherence)': 'PW Score',
    'PACC uniform (Entity Coherence)': 'PACC Uniform',
    'PACC weighted (Entity Coherence)': 'PACC Weighted',
    'Avg entities/sentence (Entity Coherence)': 'Entities/Sent',
    'Total entities (Entity Coherence)': 'Total Entities',
    'Sentences analyzed (Entity Coherence)': 'Sentences Analyzed',
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

# Dimension labels for grouping
DIMENSION = {
    'Entity Persist.': 'Coherence',
    'PU Score': 'Coherence',
    'PW Score': 'Coherence',
    'PACC Uniform': 'Coherence',
    'PACC Weighted': 'Coherence',
    'Entities/Sent': 'Coherence',
    'Total Entities': 'Coherence',
    'Sentences Analyzed': 'Coherence',
    'Grade Level': 'Readability',
    'Headings/Sent': 'Structure',
    'Heading Count': 'Structure',
    'Lists/Sent': 'Structure',
    'List Items': 'Structure',
    'SMAO Count': 'Requirements',
    'SMAO %': 'Requirements',
    'Vague/Sent': 'Requirements',
    'Anaphora/Sent': 'Requirements',
    'Sentence CV': 'Requirements',
    'CPRE/Sent': 'CPRE',
}


def short_name(m):
    return SHORT_METRIC.get(m, m.split('(')[0].strip())


def load_data(path):
    df = pd.read_csv(path)
    df['Subfolder'] = df['Subfolder'].fillna('(root)').replace('', '(root)')
    numeric_cols = []
    for col in df.columns:
        if col in ('Subfolder', 'File', 'Interpretation (Readability)'):
            continue
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if not df[col].isna().all() and col not in EXCLUDED_METRICS:
            numeric_cols.append(col)
    return df, numeric_cols


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'results/results.csv'
    output_dir = 'analysis_output'
    os.makedirs(output_dir, exist_ok=True)

    df, feature_cols = load_data(path)
    X = df[feature_cols].copy()
    for col in X.columns:
        X[col] = X[col].fillna(X[col].median())

    short_cols = [short_name(c) for c in feature_cols]
    X.columns = short_cols

    print(f"Analyzing {len(short_cols)} metrics across {len(df)} documents\n")

    # -----------------------------------------------------------------------
    # 1. Spearman correlation matrix
    # -----------------------------------------------------------------------
    corr = X.corr(method='spearman')

    # Hierarchical clustering on correlation distance
    dist = 1 - corr.abs()
    np.fill_diagonal(dist.values, 0)
    linkage_matrix = linkage(squareform(dist), method='average')

    # Clustered heatmap
    g = sns.clustermap(
        corr,
        method='average',
        metric='euclidean',
        row_linkage=linkage_matrix,
        col_linkage=linkage_matrix,
        cmap='RdBu_r',
        center=0,
        vmin=-1, vmax=1,
        annot=True, fmt='.2f',
        annot_kws={'size': 7},
        figsize=(12, 10),
        linewidths=0.5,
        dendrogram_ratio=(0.15, 0.15),
    )
    g.ax_heatmap.set_title('Spearman Correlation (Hierarchically Clustered)',
                           fontsize=14, fontweight='bold', pad=20)
    plt.savefig(os.path.join(output_dir, 'metric_correlation_clustered.png'),
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: metric_correlation_clustered.png")

    # Also a compact version for the paper (no dendrograms)
    fig, ax = plt.subplots(figsize=(8, 6.5))
    # Reorder columns by cluster order from clustermap
    order = g.dendrogram_row.reordered_ind
    ordered_cols = [short_cols[i] for i in order]
    corr_ordered = corr.loc[ordered_cols, ordered_cols]

    mask = np.triu(np.ones_like(corr_ordered, dtype=bool), k=1)
    sns.heatmap(
        corr_ordered,
        mask=mask,
        cmap='RdBu_r',
        center=0, vmin=-1, vmax=1,
        annot=True, fmt='.2f',
        annot_kws={'size': 7},
        linewidths=0.5,
        cbar_kws={'label': 'Spearman ρ', 'shrink': 0.8},
        ax=ax,
    )
    ax.set_title('Metric Correlation (Spearman ρ, clustered order)',
                 fontsize=12, fontweight='bold', pad=10)
    ax.tick_params(axis='both', labelsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'metric_correlation_paper.png'),
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: metric_correlation_paper.png")

    # -----------------------------------------------------------------------
    # 2. Highly correlated pairs
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("HIGHLY CORRELATED PAIRS (|Spearman ρ| > 0.60)")
    print(f"{'='*60}\n")

    pairs = []
    for i in range(len(short_cols)):
        for j in range(i + 1, len(short_cols)):
            r = corr.iloc[i, j]
            if abs(r) > 0.60:
                pairs.append((short_cols[i], short_cols[j], r,
                               DIMENSION.get(short_cols[i], '?'),
                               DIMENSION.get(short_cols[j], '?')))

    pairs.sort(key=lambda x: -abs(x[2]))
    if not pairs:
        print("  No pairs above threshold.")
    for a, b, r, da, db in pairs:
        same = "SAME" if da == db else "CROSS"
        print(f"  {a:20s} × {b:20s}  ρ={r:+.3f}  [{da}/{db}] {same}")

    # -----------------------------------------------------------------------
    # 3. Metric clusters at different thresholds
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("METRIC CLUSTERS (correlation distance, average linkage)")
    print(f"{'='*60}\n")

    for threshold in [0.30, 0.40, 0.50]:
        clusters = fcluster(linkage_matrix, t=threshold, criterion='distance')
        n_clusters = len(set(clusters))
        print(f"  Distance threshold {threshold}: {n_clusters} clusters")
        for cid in sorted(set(clusters)):
            members = [short_cols[i] for i in range(len(short_cols))
                       if clusters[i] == cid]
            dims = set(DIMENSION.get(m, '?') for m in members)
            print(f"    Cluster {cid}: {', '.join(members)}  [{'/'.join(dims)}]")
        print()

    # -----------------------------------------------------------------------
    # 4. PCA — effective dimensionality
    # -----------------------------------------------------------------------
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA()
    pca.fit(X_scaled)

    cumvar = np.cumsum(pca.explained_variance_ratio_)

    print(f"{'='*60}")
    print("PCA — EXPLAINED VARIANCE")
    print(f"{'='*60}\n")

    for i, (var, cum) in enumerate(zip(pca.explained_variance_ratio_, cumvar)):
        bar = '█' * int(var * 50)
        print(f"  PC{i+1:2d}  {var:.3f}  (cum {cum:.3f})  {bar}")

    n_90 = np.argmax(cumvar >= 0.90) + 1
    n_95 = np.argmax(cumvar >= 0.95) + 1
    print(f"\n  Components for 90% variance: {n_90}")
    print(f"  Components for 95% variance: {n_95}")
    print(f"  Effective dimensionality: ~{n_90} independent axes from {len(short_cols)} metrics")

    # PCA scree plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.bar(range(1, len(pca.explained_variance_ratio_) + 1),
            pca.explained_variance_ratio_, color='steelblue', alpha=0.8)
    ax1.plot(range(1, len(cumvar) + 1), cumvar, 'ro-', markersize=5)
    ax1.axhline(y=0.90, color='gray', linestyle='--', alpha=0.5, label='90%')
    ax1.axhline(y=0.95, color='gray', linestyle=':', alpha=0.5, label='95%')
    ax1.set_xlabel('Principal Component', fontsize=11)
    ax1.set_ylabel('Variance Explained', fontsize=11)
    ax1.set_title('Scree Plot', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=9)

    # Top loadings for first 4 PCs
    loadings = pd.DataFrame(
        pca.components_[:4].T,
        index=short_cols,
        columns=[f'PC{i+1}' for i in range(4)]
    )

    sns.heatmap(loadings, cmap='RdBu_r', center=0, annot=True, fmt='.2f',
                annot_kws={'size': 8}, ax=ax2, linewidths=0.5,
                cbar_kws={'shrink': 0.8})
    ax2.set_title('PCA Loadings (first 4 components)', fontsize=12,
                  fontweight='bold')
    ax2.tick_params(axis='both', labelsize=9)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pca_analysis.png'),
                dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: pca_analysis.png")

    # -----------------------------------------------------------------------
    # 5. Top loadings per PC (interpretable)
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("PCA LOADINGS — TOP CONTRIBUTORS PER COMPONENT")
    print(f"{'='*60}\n")

    for pc_idx in range(min(n_90, 8)):
        pc_loadings = pd.Series(pca.components_[pc_idx], index=short_cols)
        pc_loadings = pc_loadings.reindex(pc_loadings.abs().sort_values(ascending=False).index)
        top = pc_loadings.head(5)
        var = pca.explained_variance_ratio_[pc_idx]
        print(f"  PC{pc_idx+1} ({var:.1%} variance):")
        for m, v in top.items():
            dim = DIMENSION.get(m, '?')
            print(f"    {m:20s}  {v:+.3f}  [{dim}]")
        print()


if __name__ == '__main__':
    main()
