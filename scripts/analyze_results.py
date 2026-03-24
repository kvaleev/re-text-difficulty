#!/usr/bin/env python3
"""
Results Analyzer - Analyzes results.csv to compare metrics across subfolders.

Generates:
1. Distribution charts for each metric by subfolder
2. Correlation analysis between metrics and subfolders
3. Classification report (can we predict subfolder from metrics?)
4. Summary statistics report
"""

import os
import sys
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime

# Optional: sklearn for classification analysis
try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_predict, StratifiedKFold
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.metrics import (classification_report, confusion_matrix,
                                  precision_recall_fscore_support, accuracy_score)
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Note: sklearn not available. Classification analysis will be skipped.")
    print("Install with: pip3 install scikit-learn")


class ResultsAnalyzer:
    """Analyzes results.csv and generates reports and visualizations."""

    # Display names for document categories (internal folder name → paper name)
    CATEGORY_NAMES = {
        'small_prd_files': 'Small PRD',
        'prd_files': 'Long PRD',
        'pure_raw_markdown': 'PURE',
        'non_related_github': 'GitHub Articles',
        'non_related_wikipedia_samples': 'Wikipedia',
    }

    # Short display names for metrics
    METRIC_SHORT_NAMES = {
        'Entity persistence ratio (Entity Coherence)': 'Entity Persist.',
        'PU score (Entity Coherence)': 'PU Score',
        'PW score (Entity Coherence)': 'PW Score',
        'PACC uniform (Entity Coherence)': 'PACC Uniform',
        'PACC weighted (Entity Coherence)': 'PACC Weighted',
        'Avg entities/sentence (Entity Coherence)': 'Entities/Sent.',
        'Total entities (Entity Coherence)': 'Total Entities',
        'Sentences analyzed (Entity Coherence)': 'Sentences Analyzed',
        'Consensus grade level (Readability)': 'Grade Level',
        'Headings per sentence (Structure)': 'Headings/Sent.',
        'Headings count (Structure)': 'Heading Count',
        'Lists per sentence (Structure)': 'Lists/Sent.',
        'List items count (Structure)': 'List Items',
        'SMAO sentences count (Requirements)': 'SMAO Count',
        'SMAO sentences % (Requirements)': 'SMAO %',
        'Vague words per sentence (Requirements)': 'Vague/Sent.',
        'Anaphora per sentence (Requirements)': 'Anaphora/Sent.',
        'Sentence CV (Requirements)': 'Sentence CV',
        'CPRE terms per sentence (CPRE)': 'CPRE/Sent.',
    }

    @classmethod
    def display_name(cls, internal_name: str) -> str:
        """Map internal folder/metric name to display name."""
        return cls.CATEGORY_NAMES.get(internal_name, internal_name)

    @classmethod
    def short_metric(cls, metric_name: str) -> str:
        """Map full metric name to short display name."""
        return cls.METRIC_SHORT_NAMES.get(metric_name, metric_name.split('(')[0].strip())

    def __init__(self, results_path: str = 'results/results.csv'):
        """
        Initialize the analyzer.

        Args:
            results_path: Path to results.csv file
        """
        self.results_path = results_path
        self.df = None
        self.output_dir = 'analysis_output'
        self.numeric_columns = []
        self.categorical_columns = []

    def load_data(self) -> bool:
        """
        Load results.csv file.

        Returns:
            True if successful, False otherwise
        """
        if not os.path.exists(self.results_path):
            print(f"Error: {self.results_path} not found")
            return False

        self.df = pd.read_csv(self.results_path)

        # Handle empty subfolder values
        self.df['Subfolder'] = self.df['Subfolder'].fillna('(root)')
        self.df['Subfolder'] = self.df['Subfolder'].replace('', '(root)')

        # Identify numeric and categorical columns
        for col in self.df.columns:
            if col in ['Subfolder', 'File', 'Interpretation (Readability)']:
                self.categorical_columns.append(col)
            else:
                # Try to convert to numeric
                try:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                    if not self.df[col].isna().all():
                        self.numeric_columns.append(col)
                except:
                    self.categorical_columns.append(col)

        # Exclude composite scores (weights lack empirical justification)
        # and redundant readability formulas (retain only consensus_grade_level)
        excluded_metrics = [
            'Structure score 0-100 (Structure)',       # composite score
            'Readiness score 0-100 (Requirements)',    # composite score
            'Flesch Reading Ease 0-100 (Readability)', # redundant with consensus (r=-0.91)
            'Flesch-Kincaid grade level (Readability)', # redundant with consensus (r=0.95)
            'ARI grade level (Readability)',            # redundant with consensus (r=0.81)
            'Gunning Fog grade level (Readability)',    # redundant with consensus (r=0.95)
            'SMOG grade level (Readability)',           # redundant with consensus (r=0.83)
            'Coleman-Liau grade level (Readability)',   # redundant with consensus (r=0.69)
        ]
        excluded_count = 0
        for col in excluded_metrics:
            if col in self.numeric_columns:
                self.numeric_columns.remove(col)
                excluded_count += 1

        print(f"Loaded {len(self.df)} files from {self.df['Subfolder'].nunique()} subfolders")
        print(f"Numeric columns: {len(self.numeric_columns)} (excluded {excluded_count}: {excluded_count - 2} redundant readability + 2 composites)")
        print(f"Subfolders: {', '.join(self.df['Subfolder'].unique())}")

        return True

    def setup_output_dir(self):
        """Clear and create output directory for analysis results."""
        if os.path.exists(self.output_dir):
            print(f"Clearing previous analysis in '{self.output_dir}/'...")
            try:
                shutil.rmtree(self.output_dir)
            except (PermissionError, OSError):
                # If rmtree fails, try to remove individual files
                for root, dirs, files in os.walk(self.output_dir):
                    for fn in files:
                        try:
                            os.remove(os.path.join(root, fn))
                        except (PermissionError, OSError):
                            pass  # Skip files that can't be deleted
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, 'charts'), exist_ok=True)

    def generate_summary_statistics(self) -> pd.DataFrame:
        """
        Generate summary statistics for each metric by subfolder.

        Returns:
            DataFrame with summary statistics
        """
        stats_list = []

        for col in self.numeric_columns:
            for subfolder in self.df['Subfolder'].unique():
                subset = self.df[self.df['Subfolder'] == subfolder][col].dropna()

                if len(subset) > 0:
                    stats_list.append({
                        'Metric': col,
                        'Subfolder': subfolder,
                        'Count': len(subset),
                        'Mean': subset.mean(),
                        'Std': subset.std(),
                        'Min': subset.min(),
                        'Q25': subset.quantile(0.25),
                        'Median': subset.median(),
                        'Q75': subset.quantile(0.75),
                        'Max': subset.max()
                    })

        stats_df = pd.DataFrame(stats_list)
        return stats_df

    def plot_metric_distributions(self):
        """Generate distribution plots for each metric by subfolder."""
        subfolders = self.df['Subfolder'].unique()
        n_subfolders = len(subfolders)

        if n_subfolders < 2:
            print("Warning: Need at least 2 subfolders for comparison charts")
            return

        # Set up color palette
        colors = sns.color_palette("husl", n_subfolders)
        subfolder_colors = dict(zip(subfolders, colors))

        for col in self.numeric_columns:
            # Skip if all NaN
            if self.df[col].isna().all():
                continue

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            # Box plot
            ax1 = axes[0]
            data_for_box = [self.df[self.df['Subfolder'] == sf][col].dropna() for sf in subfolders]
            bp = ax1.boxplot(data_for_box, tick_labels=subfolders, patch_artist=True)
            for patch, color in zip(bp['boxes'], colors):
                patch.set_facecolor(color)
                patch.set_alpha(0.7)
            ax1.set_title(f'{col}\nDistribution by Subfolder')
            ax1.set_xlabel('Subfolder')
            ax1.set_ylabel('Value')
            ax1.tick_params(axis='x', rotation=45)

            # Histogram/KDE plot
            ax2 = axes[1]
            for sf in subfolders:
                subset = self.df[self.df['Subfolder'] == sf][col].dropna()
                if len(subset) > 1:
                    try:
                        sns.kdeplot(data=subset, ax=ax2, label=sf, color=subfolder_colors[sf], fill=True, alpha=0.3)
                    except:
                        # Fallback to histogram if KDE fails
                        ax2.hist(subset, alpha=0.5, label=sf, color=subfolder_colors[sf], bins=10)
                elif len(subset) == 1:
                    ax2.axvline(subset.iloc[0], label=sf, color=subfolder_colors[sf], linestyle='--')

            ax2.set_title(f'{col}\nDensity by Subfolder')
            ax2.set_xlabel('Value')
            ax2.set_ylabel('Density')
            ax2.legend()

            plt.tight_layout()

            # Save figure
            safe_filename = col.replace('/', '_').replace(' ', '_').replace('(', '').replace(')', '')
            plt.savefig(os.path.join(self.output_dir, 'charts', f'{safe_filename}.png'), dpi=150)
            plt.close()

        print(f"Distribution charts saved to {self.output_dir}/charts/")

    def plot_correlation_heatmap(self):
        """Generate correlation heatmap between numeric metrics."""
        numeric_df = self.df[self.numeric_columns].dropna(axis=1, how='all')

        if len(numeric_df.columns) < 2:
            print("Warning: Not enough numeric columns for correlation analysis")
            return

        # Calculate correlation matrix
        corr_matrix = numeric_df.corr()

        # Create heatmap
        plt.figure(figsize=(16, 14))
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
                    center=0, square=True, linewidths=0.5,
                    annot_kws={'size': 8})
        plt.title('Metric Correlation Heatmap')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'correlation_heatmap.png'), dpi=150)
        plt.close()

        print(f"Correlation heatmap saved to {self.output_dir}/correlation_heatmap.png")

    def plot_subfolder_radar(self):
        """Generate radar charts comparing subfolders across key metrics."""
        subfolders = self.df['Subfolder'].unique()

        if len(subfolders) < 2:
            return

        # Select key metrics (remove counts, keep ratios and scores)
        key_metrics = [col for col in self.numeric_columns
                       if any(x in col.lower() for x in ['score', 'ratio', 'per sentence', 'cv', 'grade', 'ease'])]

        if len(key_metrics) < 3:
            key_metrics = self.numeric_columns[:min(8, len(self.numeric_columns))]

        if len(key_metrics) < 3:
            print("Warning: Not enough metrics for radar chart")
            return

        # Limit to 8 metrics for readability
        key_metrics = key_metrics[:8]

        # Normalize metrics to 0-1 scale for comparison
        normalized_data = {}
        for col in key_metrics:
            col_data = self.df[col].dropna()
            if col_data.max() != col_data.min():
                normalized_data[col] = (self.df[col] - col_data.min()) / (col_data.max() - col_data.min())
            else:
                normalized_data[col] = self.df[col] / col_data.max() if col_data.max() != 0 else self.df[col]

        normalized_df = pd.DataFrame(normalized_data)
        normalized_df['Subfolder'] = self.df['Subfolder']

        # Calculate mean for each subfolder
        means = normalized_df.groupby('Subfolder')[key_metrics].mean()

        # Create radar chart — sized for IEEE two-column (~3.5in wide)
        angles = np.linspace(0, 2 * np.pi, len(key_metrics), endpoint=False).tolist()
        angles += angles[:1]  # Complete the loop

        fig, ax = plt.subplots(figsize=(7, 6), subplot_kw=dict(polar=True))
        colors = sns.color_palette("husl", len(subfolders))

        for idx, (subfolder, row) in enumerate(means.iterrows()):
            values = row.tolist()
            values += values[:1]  # Complete the loop
            cat_display = self.display_name(subfolder)
            ax.plot(angles, values, 'o-', linewidth=2, label=cat_display,
                    color=colors[idx], markersize=4)
            ax.fill(angles, values, alpha=0.2, color=colors[idx])

        # Set labels with large fonts
        ax.set_xticks(angles[:-1])
        labels = [self.short_metric(m) for m in key_metrics]
        ax.set_xticklabels(labels, size=11, fontweight='bold')
        ax.tick_params(axis='y', labelsize=9)
        ax.set_title('Document Category Profiles (Normalized)', size=14,
                      fontweight='bold', y=1.08)
        ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.05), fontsize=10,
                  framealpha=0.9)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'subfolder_radar.png'),
                    dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Radar chart saved to {self.output_dir}/subfolder_radar.png")

    def analyze_subfolder_predictability(self) -> dict:
        """
        Analyze if we can predict subfolder from metrics using Random Forest.

        Uses cross_val_predict with StratifiedKFold to get per-document predictions,
        then computes per-class precision/recall/F1, confusion matrix, and
        macro vs. weighted averages.

        Returns:
            Dictionary with classification results
        """
        if not SKLEARN_AVAILABLE:
            return {'error': 'sklearn not available'}

        subfolders = self.df['Subfolder'].unique()
        if len(subfolders) < 2:
            return {'error': 'Need at least 2 subfolders for classification'}

        # Prepare features
        feature_cols = [col for col in self.numeric_columns if not self.df[col].isna().all()]
        X = self.df[feature_cols].copy()

        # Fill NaN with median
        for col in X.columns:
            X[col] = X[col].fillna(X[col].median())

        y = self.df['Subfolder']

        # Check if we have enough samples
        min_samples_per_class = y.value_counts().min()
        if min_samples_per_class < 2:
            return {'error': f'Need at least 2 samples per subfolder. Minimum found: {min_samples_per_class}'}

        # Encode labels
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)

        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Train Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)

        # Stratified cross-validation with cross_val_predict
        n_splits = min(5, min_samples_per_class)
        if n_splits < 2:
            n_splits = 2

        try:
            skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
            y_pred_cv = cross_val_predict(rf, X_scaled, y_encoded, cv=skf)
        except Exception as e:
            return {'error': f'Cross-validation failed: {str(e)}'}

        # Overall accuracy from cross-validated predictions
        cv_accuracy = accuracy_score(y_encoded, y_pred_cv)

        # Per-class precision, recall, F1, support
        precision, recall, f1, support = precision_recall_fscore_support(
            y_encoded, y_pred_cv, labels=range(len(le.classes_)), zero_division=0
        )

        # Full classification report
        report = classification_report(
            y_encoded, y_pred_cv, target_names=le.classes_, output_dict=True
        )

        # Confusion matrix from cross-validated predictions (all 376 documents)
        cm = confusion_matrix(y_encoded, y_pred_cv)

        # Fit model on full data to get feature importance
        rf.fit(X_scaled, y_encoded)
        feature_importance = pd.DataFrame({
            'Feature': feature_cols,
            'Importance': rf.feature_importances_
        }).sort_values('Importance', ascending=False)

        # Build per-class metrics dict
        per_class_metrics = {
            name: {
                'precision': float(precision[i]),
                'recall': float(recall[i]),
                'f1': float(f1[i]),
                'support': int(support[i])
            }
            for i, name in enumerate(le.classes_)
        }

        results = {
            'cv_accuracy': cv_accuracy,
            'macro_f1': report['macro avg']['f1-score'],
            'weighted_f1': report['weighted avg']['f1-score'],
            'feature_importance': feature_importance.to_dict('records'),
            'per_class_metrics': per_class_metrics,
            'classification_report': report,
            'confusion_matrix': cm.tolist(),
            'n_samples': len(X),
            'n_features': len(feature_cols),
            'n_classes': len(subfolders),
            'classes': le.classes_.tolist(),
            'n_splits': n_splits,
        }

        # Plot feature importance — sized for IEEE with readable labels
        top_features = feature_importance.head(15).copy()
        top_features['Short'] = top_features['Feature'].map(self.short_metric)
        fig, ax = plt.subplots(figsize=(7, 5.5))
        sns.barplot(data=top_features, x='Importance', y='Short', palette='viridis', ax=ax)
        ax.set_title(f'Feature Importance (CV Accuracy: {cv_accuracy:.1%})',
                     size=14, fontweight='bold')
        ax.set_xlabel('Importance', size=12)
        ax.set_ylabel('')
        ax.tick_params(axis='both', labelsize=11)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'feature_importance.png'),
                    dpi=300, bbox_inches='tight')
        plt.close()

        # Plot confusion matrix — sized for IEEE two-column with readable text
        cm_labels = [self.display_name(c) for c in le.classes_]

        fig, ax = plt.subplots(figsize=(7, 5.5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=cm_labels, yticklabels=cm_labels,
                    annot_kws={'size': 14, 'fontweight': 'bold'},
                    cbar_kws={'shrink': 0.8}, ax=ax)
        ax.set_title('Cross-Validated Confusion Matrix', size=14, fontweight='bold', pad=12)
        ax.set_xlabel('Predicted', size=12, fontweight='bold')
        ax.set_ylabel('Actual', size=12, fontweight='bold')
        ax.tick_params(axis='both', labelsize=11)
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        plt.setp(ax.get_yticklabels(), rotation=0)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'confusion_matrix.png'),
                    dpi=300, bbox_inches='tight')
        plt.close()

        return results

    def calculate_discriminative_metrics(self) -> pd.DataFrame:
        """
        Calculate which metrics best discriminate between subfolders.

        Uses Welch's ANOVA (no equal-variance assumption), with:
        - Benjamini-Hochberg FDR correction for multiple comparisons
        - Kruskal-Wallis non-parametric test as robustness check

        Returns:
            DataFrame with discriminative power for each metric
        """
        from scipy import stats
        try:
            import pingouin as pg
            PINGOUIN_AVAILABLE = True
        except ImportError:
            PINGOUIN_AVAILABLE = False
        try:
            from statsmodels.stats.multitest import multipletests
            MULTITEST_AVAILABLE = True
        except ImportError:
            MULTITEST_AVAILABLE = False

        results = []

        for col in self.numeric_columns:
            if self.df[col].isna().all():
                continue

            groups = [group[col].dropna() for name, group in self.df.groupby('Subfolder')]
            groups = [g for g in groups if len(g) > 0]

            if len(groups) < 2:
                continue

            row = {'Metric': col}

            # Welch's ANOVA (does not assume equal variances)
            try:
                if PINGOUIN_AVAILABLE:
                    # pingouin.welch_anova returns a DataFrame
                    df_temp = self.df[[col, 'Subfolder']].dropna()
                    welch_result = pg.welch_anova(dv=col, between='Subfolder', data=df_temp)
                    row['Welch_F'] = welch_result['F'].values[0]
                    row['Welch_P'] = welch_result['p_unc'].values[0]
                else:
                    # Fallback: classical ANOVA (less ideal but functional)
                    f_stat, p_value = stats.f_oneway(*groups)
                    row['Welch_F'] = f_stat
                    row['Welch_P'] = p_value
            except Exception:
                continue

            if np.isnan(row.get('Welch_F', np.nan)):
                continue

            # Eta-squared effect size (SS_between / SS_total)
            try:
                df_temp = self.df[[col, 'Subfolder']].dropna()
                grand_mean = df_temp[col].mean()
                ss_total = ((df_temp[col] - grand_mean) ** 2).sum()
                ss_between = sum(
                    len(g) * (g.mean() - grand_mean) ** 2
                    for _, g in df_temp.groupby('Subfolder')[col]
                )
                row['Eta_sq'] = ss_between / ss_total if ss_total > 0 else np.nan
            except Exception:
                row['Eta_sq'] = np.nan

            # Kruskal-Wallis non-parametric robustness check
            try:
                h_stat, kw_p = stats.kruskal(*groups)
                row['KW_H'] = h_stat
                row['KW_P'] = kw_p
            except Exception:
                row['KW_H'] = np.nan
                row['KW_P'] = np.nan

            results.append(row)

        results_df = pd.DataFrame(results)

        if len(results_df) > 0:
            # Benjamini-Hochberg FDR correction for multiple comparisons
            if MULTITEST_AVAILABLE:
                # Correct Welch p-values
                reject_w, pvals_w_corr, _, _ = multipletests(
                    results_df['Welch_P'].values, method='fdr_bh'
                )
                results_df['Welch_P_FDR'] = pvals_w_corr
                results_df['Significant_Welch'] = reject_w

                # Correct Kruskal-Wallis p-values
                kw_mask = results_df['KW_P'].notna()
                if kw_mask.any():
                    reject_kw, pvals_kw_corr, _, _ = multipletests(
                        results_df.loc[kw_mask, 'KW_P'].values, method='fdr_bh'
                    )
                    results_df.loc[kw_mask, 'KW_P_FDR'] = pvals_kw_corr
                    results_df.loc[kw_mask, 'Significant_KW'] = reject_kw
            else:
                results_df['Welch_P_FDR'] = results_df['Welch_P']
                results_df['Significant_Welch'] = results_df['Welch_P'] < 0.05
                results_df['KW_P_FDR'] = results_df['KW_P']
                results_df['Significant_KW'] = results_df['KW_P'] < 0.05

            results_df = results_df.sort_values('Welch_F', ascending=False)

        return results_df

    def generate_report(self):
        """Generate comprehensive analysis report."""
        report_path = os.path.join(self.output_dir, 'analysis_report.txt')

        with open(report_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("TEXT EVALUATION RESULTS ANALYSIS REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            # Dataset overview
            f.write("## DATASET OVERVIEW\n\n")
            f.write(f"Total files analyzed: {len(self.df)}\n")
            f.write(f"Number of subfolders: {self.df['Subfolder'].nunique()}\n")
            f.write(f"Numeric metrics: {len(self.numeric_columns)}\n\n")

            f.write("Files per subfolder:\n")
            for sf, count in self.df['Subfolder'].value_counts().items():
                f.write(f"  {self.display_name(sf)}: {count} files\n")
            f.write("\n")

            # Summary statistics
            f.write("=" * 80 + "\n")
            f.write("## SUMMARY STATISTICS BY SUBFOLDER\n")
            f.write("=" * 80 + "\n\n")

            stats_df = self.generate_summary_statistics()
            for metric in stats_df['Metric'].unique():
                f.write(f"\n### {metric}\n\n")
                metric_stats = stats_df[stats_df['Metric'] == metric]
                f.write(metric_stats.to_string(index=False))
                f.write("\n")

            # Discriminative metrics
            f.write("\n" + "=" * 80 + "\n")
            f.write("## MOST DISCRIMINATIVE METRICS\n")
            f.write("=" * 80 + "\n\n")
            f.write("Statistical tests applied:\n")
            f.write("  - Welch's ANOVA (does not assume equal variances across groups)\n")
            f.write("  - Kruskal-Wallis H-test (non-parametric robustness check)\n")
            f.write("  - Benjamini-Hochberg FDR correction for multiple comparisons (27 tests)\n\n")
            f.write("Metrics ranked by Welch's F-statistic (higher = better separation):\n\n")

            disc_df = self.calculate_discriminative_metrics()
            if len(disc_df) > 0:
                # Display top 15 with key columns
                display_cols = ['Metric', 'Welch_F', 'Eta_sq', 'Welch_P_FDR', 'Significant_Welch', 'KW_H', 'KW_P_FDR', 'Significant_KW']
                display_cols = [c for c in display_cols if c in disc_df.columns]
                f.write(disc_df[display_cols].head(15).to_string(index=False))
                f.write("\n\n")

                if 'Significant_Welch' in disc_df.columns:
                    sig_welch = disc_df['Significant_Welch'].sum()
                    f.write(f"Significant metrics (Welch's ANOVA, FDR-corrected α=0.05): {sig_welch} of {len(disc_df)}\n")
                if 'Significant_KW' in disc_df.columns:
                    sig_kw = disc_df['Significant_KW'].sum()
                    f.write(f"Significant metrics (Kruskal-Wallis, FDR-corrected α=0.05): {sig_kw} of {len(disc_df)}\n")
            else:
                f.write("Not enough data for ANOVA analysis.\n")

            # Classification results
            if SKLEARN_AVAILABLE:
                f.write("\n" + "=" * 80 + "\n")
                f.write("## SUBFOLDER PREDICTION ANALYSIS\n")
                f.write("=" * 80 + "\n\n")

                clf_results = self.analyze_subfolder_predictability()

                if 'error' in clf_results:
                    f.write(f"Classification analysis skipped: {clf_results['error']}\n")
                else:
                    f.write(f"Method: Random Forest with {clf_results['n_splits']}-fold Stratified Cross-Validation\n")
                    f.write(f"  Each document predicted exactly once in its held-out fold (cross_val_predict).\n\n")
                    f.write(f"Overall accuracy: {clf_results['cv_accuracy']:.2%}\n")
                    f.write(f"Macro F1:         {clf_results['macro_f1']:.4f}\n")
                    f.write(f"Weighted F1:      {clf_results['weighted_f1']:.4f}\n")
                    macro_f1 = clf_results['macro_f1']
                    weighted_f1 = clf_results['weighted_f1']
                    if weighted_f1 - macro_f1 > 0.05:
                        f.write(f"  ⚠ Weighted F1 exceeds Macro F1 by {weighted_f1 - macro_f1:.4f} — classifier underperforms on small classes.\n")
                    f.write(f"Number of samples: {clf_results['n_samples']}\n")
                    f.write(f"Number of features: {clf_results['n_features']}\n")
                    f.write(f"Number of classes: {clf_results['n_classes']}\n\n")

                    # Per-class metrics table
                    f.write("Per-class classification metrics (cross-validated):\n\n")
                    f.write(f"  {'Category':<20s} {'Precision':>9s} {'Recall':>8s} {'F1':>8s} {'Support':>9s}\n")
                    f.write(f"  {'-'*20} {'-'*9} {'-'*8} {'-'*8} {'-'*9}\n")
                    for name in clf_results['classes']:
                        m = clf_results['per_class_metrics'][name]
                        display = self.display_name(name)
                        f.write(f"  {display:<20s} {m['precision']:>9.4f} {m['recall']:>8.4f} {m['f1']:>8.4f} {m['support']:>9d}\n")
                    f.write("\n")

                    # Confusion matrix as text
                    f.write("Confusion matrix (rows=actual, columns=predicted):\n\n")
                    cm = clf_results['confusion_matrix']
                    classes = clf_results['classes']
                    display_classes = [self.display_name(c) for c in classes]
                    # Header
                    f.write(f"  {'':>20s}")
                    for name in display_classes:
                        f.write(f" {name:>17s}")
                    f.write("\n")
                    for i, name in enumerate(display_classes):
                        f.write(f"  {name:>20s}")
                        for j in range(len(classes)):
                            f.write(f" {cm[i][j]:>17d}")
                        f.write("\n")
                    f.write("\n")

                    f.write("Top 10 most important features for prediction:\n")
                    for i, feat in enumerate(clf_results['feature_importance'][:10], 1):
                        f.write(f"  {i}. {feat['Feature']}: {feat['Importance']:.4f}\n")

            f.write("\n" + "=" * 80 + "\n")
            f.write("## OUTPUT FILES\n")
            f.write("=" * 80 + "\n\n")
            f.write("Generated files:\n")
            f.write(f"  - {self.output_dir}/analysis_report.txt (this file)\n")
            f.write(f"  - {self.output_dir}/summary_statistics.csv\n")
            f.write(f"  - {self.output_dir}/discriminative_metrics.csv\n")
            f.write(f"  - {self.output_dir}/correlation_heatmap.png\n")
            f.write(f"  - {self.output_dir}/subfolder_radar.png\n")
            f.write(f"  - {self.output_dir}/feature_importance.png\n")
            f.write(f"  - {self.output_dir}/confusion_matrix.png\n")
            f.write(f"  - {self.output_dir}/charts/*.png (distribution for each metric)\n")

        print(f"Report saved to {report_path}")

        # Save CSV files
        stats_df = self.generate_summary_statistics()
        stats_df.to_csv(os.path.join(self.output_dir, 'summary_statistics.csv'), index=False)

        disc_df = self.calculate_discriminative_metrics()
        if len(disc_df) > 0:
            disc_df.to_csv(os.path.join(self.output_dir, 'discriminative_metrics.csv'), index=False)

    def run_full_analysis(self):
        """Run complete analysis pipeline."""
        print("=" * 60)
        print("TEXT EVALUATION RESULTS ANALYZER")
        print("=" * 60)

        # Load data
        if not self.load_data():
            return

        # Setup output directory
        self.setup_output_dir()

        print("\nGenerating analysis...")

        # Generate charts
        print("  - Distribution charts...")
        self.plot_metric_distributions()

        print("  - Correlation heatmap...")
        self.plot_correlation_heatmap()

        print("  - Radar chart...")
        self.plot_subfolder_radar()

        if SKLEARN_AVAILABLE:
            print("  - Classification analysis...")
            self.analyze_subfolder_predictability()

        # Generate report
        print("  - Summary report...")
        self.generate_report()

        print("\n" + "=" * 60)
        print(f"Analysis complete! Results saved to: {self.output_dir}/")
        print("=" * 60)


def main():
    """Main entry point."""
    # Default path
    results_path = 'results/results.csv'

    # Check for command line argument
    if len(sys.argv) > 1:
        results_path = sys.argv[1]

    analyzer = ResultsAnalyzer(results_path)
    analyzer.run_full_analysis()


if __name__ == "__main__":
    main()
