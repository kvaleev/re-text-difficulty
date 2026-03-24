#!/usr/bin/env python3
"""
Master Text Analysis Suite
Runs all 5 text analyzers on input documents and generates comprehensive reports.

Usage:
    python3 master_analyzer.py              # Analyze all files in input/
    python3 master_analyzer.py input.txt    # Analyze specific file
"""

import os
import sys
import json
import csv
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor, as_completed, TimeoutError

# Import all analyzers
from analyzers import (
    ReadabilityAnalyzer,
    StructureAnalyzer,
    RequirementsReadinessAnalyzer,
    CPREGlossaryAnalyzer,
    EntityCoherenceAnalyzer,
    ENTITY_COHERENCE_AVAILABLE
)

# Print message if TRUNAJOD Entity Coherence is not available
if not ENTITY_COHERENCE_AVAILABLE:
    print("Note: TRUNAJOD Entity Coherence Analyzer not available (requires python3.9, TRUNAJOD, spaCy)")
    print("      Other analyzers will run normally.")
    print("      Install with: pip3 install TRUNAJOD spacy && python3 -m spacy download en_core_web_sm")


class MasterAnalyzer:
    """
    Master analyzer that coordinates all text analysis tools.
    """

    def __init__(self):
        """Initialize all analyzers."""
        print("Initializing Text Analysis Suite...")
        if ENTITY_COHERENCE_AVAILABLE:
            print("  • TRUNAJOD Entity Coherence Analyzer (syntactic complexity + coherence)")
        else:
            print("  • TRUNAJOD Entity Coherence Analyzer (SKIPPED - not available)")
        print("  • Readability Metrics Analyzer")
        print("  • Structure Analyzer")
        print("  • Requirements Readiness Analyzer")
        print("  • CPRE Glossary Analyzer")
        print()

        if ENTITY_COHERENCE_AVAILABLE:
            self.entity_coherence = EntityCoherenceAnalyzer()
        else:
            self.entity_coherence = None
        self.readability = ReadabilityAnalyzer()
        self.structure = StructureAnalyzer()
        self.requirements = RequirementsReadinessAnalyzer()
        self.cpre = CPREGlossaryAnalyzer()

    def analyze_file(self, file_path: str, output_dir: str):
        """
        Analyze a single file with all analyzers.

        Args:
            file_path: Path to input file
            output_dir: Directory for output files
        """
        # Read file
        print(f"Analyzing: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        file_name = Path(file_path).stem
        print(f"  File size: {len(text)} characters")
        print(f"  Output directory: {output_dir}")
        print()

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Run all analyzers
        results = {}

        print("  [1/5] Running TRUNAJOD Entity Coherence Analyzer...")
        if self.entity_coherence:
            try:
                results['entity_coherence'] = self.entity_coherence.analyze(text)
                self._save_json(results['entity_coherence'], os.path.join(output_dir, 'entity_coherence_results.json'))
            except Exception as e:
                print(f"       Warning: Entity Coherence analysis failed: {e}")
                results['entity_coherence'] = None
        else:
            print("       Skipped (not available)")
            results['entity_coherence'] = None

        print("  [2/5] Running Readability Analyzer...")
        results['readability'] = self.readability.analyze(text)
        self._save_json(results['readability'], os.path.join(output_dir, 'readability_results.json'))

        print("  [3/5] Running Structure Analyzer...")
        results['structure'] = self.structure.analyze(text)
        self._save_json(results['structure'], os.path.join(output_dir, 'structure_results.json'))

        print("  [4/5] Running Requirements Readiness Analyzer...")
        results['requirements'] = self.requirements.analyze(text)
        self._save_json(results['requirements'], os.path.join(output_dir, 'requirements_readiness_results.json'))

        print("  [5/5] Running CPRE Glossary Analyzer...")
        results['cpre'] = self.cpre.analyze(text)
        self._save_json(results['cpre'], os.path.join(output_dir, 'cpre_glossary_results.json'))

        print()
        print("  ✓ All analyses complete!")
        print()

        # Generate summary report
        self._generate_summary_report(file_name, results, output_dir)

        # Generate per-file summary CSV
        self._generate_summary_csv(results, output_dir)

        # Update frontmatter in markdown files
        self._update_frontmatter(file_path, results)

        return results

    def _save_json(self, data: dict, file_path: str):
        """Save data as JSON."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def _extract_metrics_for_frontmatter(self, results: dict) -> dict:
        """
        Extract key metrics for YAML frontmatter.

        Args:
            results: Dictionary with all analysis results

        Returns:
            Dictionary with metrics for frontmatter
        """
        metrics = {}

        # Readability - Consensus grade level
        read = results['readability']
        consensus = (read['ari']['grade_level'] + read['flesch_kincaid_grade']['grade_level'] +
                    read['gunning_fog']['grade_level'] + read['smog_index']['grade_level'] +
                    read['coleman_liau']['grade_level']) / 5
        metrics['consensus_grade_level'] = round(consensus, 1)

        # Structure metrics
        struct = results['structure']
        metrics['headings_per_sentence'] = round(struct['densities']['headings_per_sentence'], 3)
        metrics['lists_per_sentence'] = round(struct['densities']['lists_per_sentence'], 3)

        # Requirements Readiness metrics
        req = results['requirements']
        smao = req['features']['sao_pattern']
        metrics['smao_sentences_pct'] = round(smao.get('smao_percentage', smao.get('sao_percentage', 0)), 1)
        metrics['vague_words_per_sentence'] = round(req['features']['ambiguity']['vague_words']['per_sentence'], 2)
        metrics['anaphora_per_sentence'] = round(req['features']['ambiguity']['anaphora']['per_sentence'], 2)
        metrics['sentence_cv'] = round(req['features']['sentence_variation']['coefficient_of_variation'], 3)

        # CPRE Glossary
        cpre = results['cpre']
        metrics['cpre_terms_per_sentence'] = round(cpre['cpre_terms_per_sentence'], 2)

        return metrics

    def _update_frontmatter(self, file_path: str, results: dict):
        """
        Update or add YAML frontmatter with analysis metrics to a markdown file.

        Args:
            file_path: Path to the markdown file
            results: Dictionary with all analysis results
        """
        # Only process markdown files
        if not file_path.endswith('.md'):
            return

        # Extract metrics
        metrics = self._extract_metrics_for_frontmatter(results)

        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has existing frontmatter
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)

        if match:
            # Parse existing frontmatter
            existing_frontmatter = match.group(1)
            body = content[match.end():]

            # Parse existing YAML (simple key: value parsing)
            existing_data = {}
            for line in existing_frontmatter.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    existing_data[key.strip()] = value.strip()

            # Update with new metrics
            existing_data.update(metrics)

            # Generate new frontmatter
            frontmatter_lines = ['---']
            for key, value in existing_data.items():
                frontmatter_lines.append(f'{key}: {value}')
            frontmatter_lines.append('---')
            frontmatter_lines.append('')

            new_content = '\n'.join(frontmatter_lines) + body
        else:
            # No existing frontmatter - create new one
            frontmatter_lines = ['---']
            for key, value in metrics.items():
                frontmatter_lines.append(f'{key}: {value}')
            frontmatter_lines.append('---')
            frontmatter_lines.append('')

            new_content = '\n'.join(frontmatter_lines) + content

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  Frontmatter updated: {file_path}")

    def _generate_summary_report(self, file_name: str, results: dict, output_dir: str):
        """
        Generate a text summary report.

        Args:
            file_name: Name of analyzed file
            results: Dictionary with all analysis results
            output_dir: Output directory
        """
        report_path = os.path.join(output_dir, 'summary_report.txt')

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("COMPREHENSIVE TEXT ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"File: {file_name}\n")
            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")

            # Entity Coherence Results (TRUNAJOD)
            if results['entity_coherence']:
                f.write("### 1. TRUNAJOD ENTITY COHERENCE ANALYSIS ###\n\n")
                ec = results['entity_coherence']
                f.write(f"  Sentences Analyzed:           {ec['basic_info']['sentence_count']}\n")
                f.write(f"  Entity Count:                 {ec['basic_info']['entity_count']}\n")
                f.write(f"  Coherence Score (PW):         {ec['coherence_scores']['PW']:.2f}\n")
                f.write(f"  Coherence Score (PU):         {ec['coherence_scores']['PU']:.2f}\n")
                f.write(f"  Avg Entities per Sentence:    {ec['basic_info']['avg_entities_per_sentence']:.2f}\n")
                f.write("\n")
            else:
                f.write("### 1. TRUNAJOD ENTITY COHERENCE ANALYSIS ###\n\n")
                f.write("  Analysis not available (requires python3.9, TRUNAJOD, and spaCy)\n")
                f.write("  Install with: pip3 install TRUNAJOD spacy && python3 -m spacy download en_core_web_sm\n\n")

            # Readability Results
            f.write("### 2. READABILITY ANALYSIS ###\n\n")
            read = results['readability']
            f.write(f"  ARI Score:                    {read['ari']['score']:.1f} (Grade {read['ari']['grade_level']})\n")
            f.write(f"  Flesch Reading Ease:          {read['flesch_reading_ease']['score']:.1f}\n")
            f.write(f"  Flesch-Kincaid Grade:         {read['flesch_kincaid_grade']['grade_level']:.1f}\n")
            f.write(f"  Gunning Fog Index:            {read['gunning_fog']['score']:.1f}\n")
            f.write(f"  SMOG Index:                   {read['smog_index']['score']:.1f}\n")
            f.write(f"  Coleman-Liau Index:           {read['coleman_liau']['score']:.1f}\n")
            # Calculate consensus
            consensus = (read['ari']['grade_level'] + read['flesch_kincaid_grade']['grade_level'] +
                        read['gunning_fog']['grade_level'] + read['smog_index']['grade_level'] +
                        read['coleman_liau']['grade_level']) / 5
            f.write(f"  Consensus Grade Level:        {consensus:.1f}\n")
            f.write("\n")

            # Structure Results
            f.write("### 3. STRUCTURE ANALYSIS ###\n\n")
            struct = results['structure']
            f.write(f"  Format Detected:              {struct['format'].upper()}\n")
            f.write(f"  Total Headings:               {struct['basic_counts']['headings']}\n")
            f.write(f"  List Items:                   {struct['basic_counts']['list_items']}\n")
            f.write(f"  Heading Density:              {struct['densities']['heading_density']:.2f} per 1000 words\n")
            f.write(f"  List Density:                 {struct['densities']['list_density']:.2f} per 100 lines\n")
            f.write(f"  Headings per sentence:        {struct['densities']['headings_per_sentence']:.2f}\n")
            f.write(f"  Lists per sentence:           {struct['densities']['lists_per_sentence']:.2f}\n")
            f.write("\n")

            # Requirements Readiness Results
            f.write("### 4. REQUIREMENTS READINESS ANALYSIS ###\n\n")
            req = results['requirements']
            metrics = req['metrics']
            f.write(f"  Sentence count:               {metrics['sentence_count']}\n")
            f.write(f"  Avg sentence length:          {metrics['avg_sentence_length']:.1f} words\n")
            f.write(f"  Sentence CV:                  {metrics['sentence_cv']:.3f}\n")
            f.write(f"  Vague words per sentence:     {metrics['vague_words_per_sentence']:.2f}\n")
            f.write(f"  Anaphora per sentence:        {metrics['anaphora_per_sentence']:.2f}\n")
            f.write(f"  SMAO sentences:               {metrics['smao_sentences_count']} ({metrics['smao_percentage']:.1f}%)\n")
            if 'subject_consistency_percentage' in metrics:
                f.write(f"  Subject consistency:          {metrics.get('dominant_subject', 'N/A')} ({metrics['subject_consistency_percentage']:.1f}%)\n")
            f.write("\n")

            # CPRE Glossary Results
            f.write("### 5. CPRE GLOSSARY ANALYSIS ###\n\n")
            cpre = results['cpre']
            f.write(f"  CPRE Terms per Sentence:      {cpre['cpre_terms_per_sentence']:.2f}\n")
            f.write("\n")

            f.write("=" * 80 + "\n")

        print(f"  Summary report saved: {report_path}")

    def _generate_summary_csv(self, results: dict, output_dir: str):
        """
        Generate a summary CSV with one row per analyzer showing key metrics.

        Args:
            results: Dictionary with all analysis results
            output_dir: Output directory
        """
        csv_path = os.path.join(output_dir, 'summary_scores.csv')

        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Analyzer', 'Primary Score', 'Metric 1', 'Metric 2', 'Metric 3', 'Metric 4']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # TRUNAJOD Entity Coherence
            if results['entity_coherence']:
                ec = results['entity_coherence']
                writer.writerow({
                    'Analyzer': 'Entity Coherence',
                    'Primary Score': f"{ec['coherence_scores']['PW']:.2f} PW score",
                    'Metric 1': f"{ec['coherence_scores']['PU']:.2f} PU score",
                    'Metric 2': f"{ec['basic_info']['avg_entities_per_sentence']:.2f} avg entities/sentence",
                    'Metric 3': f"{ec['basic_info']['entity_count']} total entities",
                    'Metric 4': f"{ec['basic_info']['sentence_count']} sentences analyzed"
                })
            else:
                writer.writerow({
                    'Analyzer': 'Entity Coherence',
                    'Primary Score': 'N/A (not available)',
                    'Metric 1': '-',
                    'Metric 2': '-',
                    'Metric 3': '-',
                    'Metric 4': 'Requires python3.9 + TRUNAJOD'
                })

            # Readability
            read = results['readability']
            consensus = (read['ari']['grade_level'] + read['flesch_kincaid_grade']['grade_level'] +
                        read['gunning_fog']['grade_level'] + read['smog_index']['grade_level'] +
                        read['coleman_liau']['grade_level']) / 5
            writer.writerow({
                'Analyzer': 'Readability Metrics',
                'Primary Score': f"Grade {consensus:.1f} (consensus)",
                'Metric 1': f"{read['flesch_reading_ease']['score']:.1f} Flesch Reading Ease",
                'Metric 2': f"Grade {read['ari']['grade_level']} ARI",
                'Metric 3': f"Grade {read['flesch_kincaid_grade']['grade_level']:.1f} F-K",
                'Metric 4': f"{read['flesch_reading_ease']['interpretation']}"
            })

            # Structure
            struct = results['structure']
            writer.writerow({
                'Analyzer': 'Structure Analysis',
                'Primary Score': f"{struct['basic_counts']['headings']} headings, {struct['basic_counts']['list_items']} lists",
                'Metric 1': f"{struct['densities']['heading_density']:.1f} headings/1000 words",
                'Metric 2': f"{struct['densities']['list_density']:.1f} lists/100 lines",
                'Metric 3': f"{struct['format'].upper()} format",
                'Metric 4': ''
            })

            # Requirements Readiness
            req = results['requirements']
            metrics = req['metrics']
            writer.writerow({
                'Analyzer': 'Requirements Readiness',
                'Primary Score': f"{metrics['smao_percentage']:.1f}% SMAO",
                'Metric 1': f"{metrics['smao_sentences_count']} SMAO sentences",
                'Metric 2': f"{metrics['vague_words_per_sentence']:.2f} vague/sent",
                'Metric 3': f"{metrics['anaphora_per_sentence']:.2f} anaph/sent",
                'Metric 4': f"CV: {metrics['sentence_cv']:.3f}"
            })

            # CPRE Glossary
            cpre = results['cpre']
            writer.writerow({
                'Analyzer': 'CPRE Glossary Analysis',
                'Primary Score': f"{cpre['cpre_terms_per_sentence']:.2f} terms/sentence",
                'Metric 1': '',
                'Metric 2': '',
                'Metric 3': '',
                'Metric 4': ''
            })

        print(f"  Summary CSV saved: {csv_path}")

    @staticmethod
    def get_csv_fieldnames():
        """Return the CSV column names."""
        return [
            'Subfolder',
            'File',
            # Entity Coherence
            'PW score (Entity Coherence)',
            'PU score (Entity Coherence)',
            'PACC uniform (Entity Coherence)',
            'PACC weighted (Entity Coherence)',
            'Avg entities/sentence (Entity Coherence)',
            'Total entities (Entity Coherence)',
            'Sentences analyzed (Entity Coherence)',
            'Entity persistence ratio (Entity Coherence)',
            # Readability
            'Consensus grade level (Readability)',
            'Flesch Reading Ease 0-100 (Readability)',
            'Flesch-Kincaid grade level (Readability)',
            'ARI grade level (Readability)',
            'Gunning Fog grade level (Readability)',
            'SMOG grade level (Readability)',
            'Coleman-Liau grade level (Readability)',
            'Interpretation (Readability)',
            # Structure
            'Headings count (Structure)',
            'Headings per sentence (Structure)',
            'List items count (Structure)',
            'Lists per sentence (Structure)',
            # Requirements Readiness
            'Sentence count (Requirements)',
            'Avg sentence length (Requirements)',
            'Sentence CV (Requirements)',
            'Vague words count (Requirements)',
            'Vague words per sentence (Requirements)',
            'Anaphora count (Requirements)',
            'Anaphora per sentence (Requirements)',
            'SMAO sentences count (Requirements)',
            'SMAO sentences % (Requirements)',
            'Subject consistency % (Requirements)',
            # CPRE Glossary
            'CPRE terms per sentence (CPRE)',
        ]

    @staticmethod
    def build_csv_row(results: dict, subfolder: str, file_name: str) -> dict:
        """
        Build a CSV row from analysis results.

        Args:
            results: Analysis results dictionary
            subfolder: Subfolder name
            file_name: File name

        Returns:
            Dictionary representing a CSV row
        """
        row = {
            'Subfolder': subfolder,
            'File': file_name,
        }

        # Entity Coherence
        if results['entity_coherence']:
            ec = results['entity_coherence']
            row.update({
                'PW score (Entity Coherence)': round(ec['coherence_scores']['PW'], 2),
                'PU score (Entity Coherence)': round(ec['coherence_scores']['PU'], 2),
                'PACC uniform (Entity Coherence)': round(ec['coherence_scores']['PACC_uniform'], 2),
                'PACC weighted (Entity Coherence)': round(ec['coherence_scores']['PACC_weighted'], 2),
                'Avg entities/sentence (Entity Coherence)': ec['basic_info']['avg_entities_per_sentence'],
                'Total entities (Entity Coherence)': ec['basic_info']['entity_count'],
                'Sentences analyzed (Entity Coherence)': ec['basic_info']['sentence_count'],
                'Entity persistence ratio (Entity Coherence)': ec['entity_statistics']['entity_persistence_ratio'],
            })
        else:
            row.update({
                'PW score (Entity Coherence)': 'N/A',
                'PU score (Entity Coherence)': 'N/A',
                'PACC uniform (Entity Coherence)': 'N/A',
                'PACC weighted (Entity Coherence)': 'N/A',
                'Avg entities/sentence (Entity Coherence)': 'N/A',
                'Total entities (Entity Coherence)': 'N/A',
                'Sentences analyzed (Entity Coherence)': 'N/A',
                'Entity persistence ratio (Entity Coherence)': 'N/A',
            })

        # Readability
        read = results['readability']
        consensus = (read['ari']['grade_level'] + read['flesch_kincaid_grade']['grade_level'] +
                    read['gunning_fog']['grade_level'] + read['smog_index']['grade_level'] +
                    read['coleman_liau']['grade_level']) / 5
        row.update({
            'Consensus grade level (Readability)': round(consensus, 1),
            'Flesch Reading Ease 0-100 (Readability)': read['flesch_reading_ease']['score'],
            'Flesch-Kincaid grade level (Readability)': read['flesch_kincaid_grade']['grade_level'],
            'ARI grade level (Readability)': read['ari']['grade_level'],
            'Gunning Fog grade level (Readability)': read['gunning_fog']['score'],
            'SMOG grade level (Readability)': read['smog_index']['score'],
            'Coleman-Liau grade level (Readability)': read['coleman_liau']['score'],
            'Interpretation (Readability)': read['flesch_reading_ease']['interpretation'],
        })

        # Structure
        struct = results['structure']
        row.update({
            'Headings count (Structure)': struct['basic_counts']['headings'],
            'Headings per sentence (Structure)': struct['densities']['headings_per_sentence'],
            'List items count (Structure)': struct['basic_counts']['list_items'],
            'Lists per sentence (Structure)': struct['densities']['lists_per_sentence'],
        })

        # Requirements Readiness
        req = results['requirements']
        metrics = req['metrics']
        row.update({
            'Sentence count (Requirements)': metrics['sentence_count'],
            'Avg sentence length (Requirements)': metrics['avg_sentence_length'],
            'Sentence CV (Requirements)': metrics['sentence_cv'],
            'Vague words count (Requirements)': metrics['vague_words_count'],
            'Vague words per sentence (Requirements)': metrics['vague_words_per_sentence'],
            'Anaphora count (Requirements)': metrics['anaphora_count'],
            'Anaphora per sentence (Requirements)': metrics['anaphora_per_sentence'],
            'SMAO sentences count (Requirements)': metrics['smao_sentences_count'],
            'SMAO sentences % (Requirements)': metrics['smao_percentage'],
            'Subject consistency % (Requirements)': metrics.get('subject_consistency_percentage', ''),
        })

        # CPRE Glossary
        cpre = results['cpre']
        row.update({
            'CPRE terms per sentence (CPRE)': cpre['cpre_terms_per_sentence'],
        })

        return row

    @staticmethod
    def init_results_csv(output_path: str):
        """
        Initialize the results CSV file with header.

        Args:
            output_path: Path to the CSV file
        """
        fieldnames = MasterAnalyzer.get_csv_fieldnames()
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    @staticmethod
    def append_result_to_csv(output_path: str, results: dict, subfolder: str, file_name: str):
        """
        Append a single result to the CSV file.

        Args:
            output_path: Path to the CSV file
            results: Analysis results dictionary
            subfolder: Subfolder name
            file_name: File name
        """
        fieldnames = MasterAnalyzer.get_csv_fieldnames()
        row = MasterAnalyzer.build_csv_row(results, subfolder, file_name)

        with open(output_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(row)

    def generate_csv_report(self, all_results: dict, output_path: str):
        """
        Generate CSV report with all file results (batch mode).

        Args:
            all_results: Dictionary mapping file keys to result data
            output_path: Path to output CSV file
        """
        print(f"\nGenerating results CSV: {output_path}")

        fieldnames = self.get_csv_fieldnames()

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for result_key, result_data in all_results.items():
                row = self.build_csv_row(
                    result_data['results'],
                    result_data['subfolder'],
                    result_data['file_name']
                )
                writer.writerow(row)

        print(f"✓ Results CSV generated successfully")


def analyze_file_worker(args):
    """
    Worker function for parallel processing.
    Must be a top-level function to be picklable.

    Args:
        args: Tuple of (input_file, subfolder, results_dir)

    Returns:
        Tuple of (result_key, result_data) or (result_key, None) on error
    """
    input_file, subfolder, results_dir = args
    file_name = Path(input_file).stem

    # Include subfolder in output directory to avoid name collisions
    if subfolder:
        output_dir = os.path.join(results_dir, subfolder, file_name)
    else:
        output_dir = os.path.join(results_dir, file_name)

    result_key = f"{subfolder}/{file_name}" if subfolder else file_name

    try:
        # Create a new analyzer instance for this worker
        # (each process needs its own instance)
        analyzer = MasterAnalyzer.__new__(MasterAnalyzer)
        analyzer.entity_coherence = None
        if ENTITY_COHERENCE_AVAILABLE:
            analyzer.entity_coherence = EntityCoherenceAnalyzer()
        analyzer.readability = ReadabilityAnalyzer()
        analyzer.structure = StructureAnalyzer()
        analyzer.requirements = RequirementsReadinessAnalyzer()
        analyzer.cpre = CPREGlossaryAnalyzer()

        results = analyzer.analyze_file(input_file, output_dir)

        return (result_key, {
            'results': results,
            'subfolder': subfolder,
            'file_name': file_name
        })
    except Exception as e:
        print(f"Error analyzing {input_file}: {e}")
        import traceback
        traceback.print_exc()
        return (result_key, None)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Comprehensive Text Analysis Suite',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 master_analyzer.py                    # Analyze all files in input/
  python3 master_analyzer.py input.txt          # Analyze specific file
  python3 master_analyzer.py --workers 4        # Use 4 parallel workers
  python3 master_analyzer.py --workers 1        # Sequential processing
  python3 master_analyzer.py --timeout 120      # 2 minute timeout per file
        """
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='Specific file to analyze (optional, defaults to all files in input/)'
    )
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=None,
        help='Number of parallel workers (default: CPU cores - 1)'
    )
    parser.add_argument(
        '--timeout', '-t',
        type=int,
        default=60,
        help='Timeout in seconds per file (default: 60). Use 0 for no timeout.'
    )
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()

    print("=" * 80)
    print("COMPREHENSIVE TEXT ANALYSIS SUITE")
    print("=" * 80)
    print()

    # Setup paths
    input_dir = 'input'
    results_dir = 'results'

    # Create input directory if it doesn't exist
    os.makedirs(input_dir, exist_ok=True)

    # Clear results directory before each run
    if os.path.exists(results_dir):
        print(f"Clearing previous results in '{results_dir}/'...")
        shutil.rmtree(results_dir)
    os.makedirs(results_dir, exist_ok=True)

    # Get input files (including from subfolders)
    if args.file:
        # Specific file provided
        input_files = [(args.file, '')]  # (file_path, subfolder)
    else:
        # Analyze all files in input directory and subfolders
        input_files = []
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith(('.txt', '.md', '.rst')):
                    file_path = os.path.join(root, file)
                    # Get subfolder relative to input_dir
                    rel_path = os.path.relpath(root, input_dir)
                    subfolder = '' if rel_path == '.' else rel_path
                    input_files.append((file_path, subfolder))

    if not input_files:
        print(f"Error: No input files found in '{input_dir}/' directory")
        print(f"\nPlease place text files (.txt, .md, .rst) in the '{input_dir}/' folder")
        sys.exit(1)

    print(f"Found {len(input_files)} file(s) to analyze:")
    if len(input_files) <= 20:
        for file_path, subfolder in input_files:
            subfolder_display = f" [{subfolder}]" if subfolder else ""
            print(f"  • {file_path}{subfolder_display}")
    else:
        # Show first 10 and last 5 for large file lists
        for file_path, subfolder in input_files[:10]:
            subfolder_display = f" [{subfolder}]" if subfolder else ""
            print(f"  • {file_path}{subfolder_display}")
        print(f"  ... and {len(input_files) - 15} more files ...")
        for file_path, subfolder in input_files[-5:]:
            subfolder_display = f" [{subfolder}]" if subfolder else ""
            print(f"  • {file_path}{subfolder_display}")
    print()

    # Determine number of workers
    max_workers = args.workers
    if max_workers is None:
        max_workers = max(1, (os.cpu_count() or 4) - 1)

    # Initialize results CSV with header (incremental writing)
    csv_path = os.path.join(results_dir, 'results.csv')
    MasterAnalyzer.init_results_csv(csv_path)
    print(f"Results CSV initialized: {csv_path}")
    print("(Results are saved incrementally after each file)")

    # Timeout setting
    timeout = args.timeout if args.timeout > 0 else None
    if timeout:
        print(f"Timeout per file: {timeout} seconds")
    print()

    completed_count = 0
    failed_count = 0
    timeout_count = 0
    total = len(input_files)

    # Use sequential processing for single file or if workers=1
    if len(input_files) == 1 or max_workers == 1:
        print("Processing sequentially...")
        print()

        # Initialize master analyzer
        master = MasterAnalyzer()

        for input_file, subfolder in input_files:
            file_name = Path(input_file).stem
            if subfolder:
                output_dir = os.path.join(results_dir, subfolder, file_name)
            else:
                output_dir = os.path.join(results_dir, file_name)

            print("-" * 80)
            try:
                results = master.analyze_file(input_file, output_dir)

                # Append to CSV immediately
                MasterAnalyzer.append_result_to_csv(csv_path, results, subfolder, file_name)
                completed_count += 1
                print(f"  → Saved to CSV ({completed_count}/{total})")

            except Exception as e:
                print(f"Error analyzing {input_file}: {e}")
                import traceback
                traceback.print_exc()
                failed_count += 1
                continue
    else:
        # Parallel processing
        print(f"Processing in parallel with {max_workers} workers...")
        print()

        # Prepare arguments for workers
        worker_args = [(f, sf, results_dir) for f, sf in input_files]

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            futures = {executor.submit(analyze_file_worker, arg): arg for arg in worker_args}

            # Process results as they complete
            for future in as_completed(futures):
                input_file, subfolder, _ = futures[future]
                file_name = Path(input_file).stem

                try:
                    result_key, result_data = future.result(timeout=timeout)

                    if result_data:
                        # Append to CSV immediately (from main process, thread-safe)
                        MasterAnalyzer.append_result_to_csv(
                            csv_path,
                            result_data['results'],
                            result_data['subfolder'],
                            result_data['file_name']
                        )
                        completed_count += 1
                    else:
                        failed_count += 1

                except TimeoutError:
                    print(f"⏱ TIMEOUT: {input_file} (>{timeout}s) - skipping")
                    timeout_count += 1
                    future.cancel()
                except Exception as e:
                    print(f"Error processing {input_file}: {e}")
                    failed_count += 1

                # Progress update
                processed = completed_count + failed_count + timeout_count
                print(f"Progress: {completed_count}/{total} saved, {timeout_count} timeouts, {failed_count} errors ({100*processed/total:.1f}%)")

    print()
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    print(f"Results saved in: {results_dir}/")
    print(f"  • Individual JSON files for each analyzer")
    print(f"  • Summary reports (summary_report.txt)")
    print(f"  • Results CSV: {csv_path} ({completed_count} files)")
    if len(input_files) > 1 and max_workers > 1:
        print(f"  • Processed with {max_workers} parallel workers")
    if timeout_count > 0:
        print(f"  ⏱ Timeouts: {timeout_count} file(s) exceeded {timeout}s limit")
    if failed_count > 0:
        print(f"  ⚠ Errors: {failed_count} file(s) failed to process")
    print()


if __name__ == "__main__":
    main()
