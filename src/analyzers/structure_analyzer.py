#!/usr/bin/env python3
"""
Document Structure Analyzer
Measures document organization through heading and list detection.
"""

import re
from typing import Dict
import json
import sys


class StructureAnalyzer:
    """
    Analyzes document structure through heading and list detection.
    Works with Markdown, HTML, and plain text.
    """

    def __init__(self):
        """Initialize the analyzer."""
        pass

    def detect_format(self, text: str) -> str:
        """
        Detect document format (Markdown, HTML, or plain text).

        Args:
            text: Input text

        Returns:
            Format type: 'markdown', 'html', or 'plain'
        """
        # Check for Markdown indicators first (more specific)
        markdown_indicators = [
            r'^#{1,6}\s+',  # Headings
            r'\[.+\]\(.+\)',  # Links
            r'^\s*[-*+]\s+',  # Lists
            r'```',  # Code blocks
        ]

        markdown_count = 0
        for pattern in markdown_indicators:
            if re.search(pattern, text, re.MULTILINE):
                markdown_count += 1

        # If we have markdown indicators, it's markdown
        if markdown_count >= 2:
            return 'markdown'

        # Check for actual HTML tags (not just < or >)
        html_tags = re.findall(r'<(html|body|head|div|p|span|h[1-6]|ul|ol|li|table|tr|td)[^>]*>', text, re.IGNORECASE)
        if len(html_tags) >= 3:
            return 'html'

        return 'plain'

    def analyze_markdown_structure(self, text: str) -> Dict:
        """
        Analyze Markdown document structure.

        Args:
            text: Markdown text

        Returns:
            Dictionary with structural metrics
        """
        lines = text.split('\n')

        # Count headings
        headings = {i: 0 for i in range(1, 7)}
        heading_lines = []

        for i, line in enumerate(lines):
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                headings[level] += 1
                heading_lines.append((i, level, match.group(2)))

        total_headings = sum(headings.values())
        max_heading_depth = max([k for k, v in headings.items() if v > 0], default=0)

        # Count list items
        list_items = 0
        list_lines = []

        for i, line in enumerate(lines):
            # Bullet lists
            if re.match(r'^\s*[-*+]\s+.+$', line):
                list_items += 1
                list_lines.append(i)
            # Numbered lists
            elif re.match(r'^\s*\d+\.\s+.+$', line):
                list_items += 1
                list_lines.append(i)

        return {
            'headings': headings,
            'total_headings': total_headings,
            'max_heading_depth': max_heading_depth,
            'heading_lines': heading_lines,
            'list_items': list_items,
            'list_lines': list_lines
        }

    def analyze_html_structure(self, text: str) -> Dict:
        """
        Analyze HTML document structure.

        Args:
            text: HTML text

        Returns:
            Dictionary with structural metrics
        """
        # Count headings by level
        headings = {i: 0 for i in range(1, 7)}

        for level in range(1, 7):
            pattern = rf'<h{level}[^>]*>.*?</h{level}>'
            matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
            headings[level] = len(matches)

        total_headings = sum(headings.values())
        max_heading_depth = max([k for k, v in headings.items() if v > 0], default=0)

        # Count list items
        li_pattern = r'<li[^>]*>.*?</li>'
        list_matches = re.findall(li_pattern, text, re.IGNORECASE | re.DOTALL)
        list_items = len(list_matches)

        return {
            'headings': headings,
            'total_headings': total_headings,
            'max_heading_depth': max_heading_depth,
            'list_items': list_items
        }

    def analyze_plain_text_structure(self, text: str) -> Dict:
        """
        Infer structure from plain text using heuristics.

        Args:
            text: Plain text

        Returns:
            Dictionary with inferred structural metrics
        """
        lines = text.split('\n')

        # Heuristics for detecting headings in plain text
        heading_patterns = [
            r'^[A-Z][A-Z\s]{3,}$',  # ALL CAPS headings
            r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,4}$',  # Title Case (2-5 words)
            r'^\d+\.(?:\d+\.)*\s+[A-Z].+$',  # Numbered sections (1.2.3 Title)
            r'^(?:Chapter|Section|Part|Appendix)\s+\d+',  # Explicit sections
        ]

        inferred_headings = 0
        for line in lines:
            line = line.strip()
            if not line:
                continue

            for pattern in heading_patterns:
                if re.match(pattern, line):
                    inferred_headings += 1
                    break

        # Heuristics for detecting lists
        list_patterns = [
            r'^\s*[-*+•]\s+.+$',  # Bullet points
            r'^\s*\d+\.\s+.+$',  # Numbered lists (1., 2., 3.)
            r'^\s*[a-z]\)\s+.+$',  # Lettered lists (a), b), c))
            r'^\s*\([ivxIVX]+\)\s+.+$',  # Roman numeral lists
        ]

        inferred_list_items = 0
        for line in lines:
            for pattern in list_patterns:
                if re.match(pattern, line):
                    inferred_list_items += 1
                    break

        return {
            'inferred_headings': inferred_headings,
            'inferred_list_items': inferred_list_items
        }

    def analyze(self, text: str) -> Dict:
        """
        Perform complete structure analysis.

        Args:
            text: Input text

        Returns:
            Dictionary with all structural metrics
        """
        # Detect format
        format_type = self.detect_format(text)

        # Get word, line, and sentence counts
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        total_words = len(words)
        lines = text.split('\n')
        total_lines = len(lines)
        # Count sentences (split by sentence-ending punctuation)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        total_sentences = len(sentences)

        # Analyze structure based on format
        if format_type == 'markdown':
            structure = self.analyze_markdown_structure(text)
        elif format_type == 'html':
            structure = self.analyze_html_structure(text)
        else:
            structure = self.analyze_plain_text_structure(text)

        # Calculate densities
        heading_count = structure.get('total_headings', structure.get('inferred_headings', 0))
        list_count = structure.get('list_items', structure.get('inferred_list_items', 0))

        densities = {
            'heading_density': round((heading_count / total_words) * 1000, 2) if total_words > 0 else 0,
            'list_density': round((list_count / total_lines) * 100, 2) if total_lines > 0 else 0,
            'heading_per_100_lines': round((heading_count / total_lines) * 100, 2) if total_lines > 0 else 0,
            'list_per_100_lines': round((list_count / total_lines) * 100, 2) if total_lines > 0 else 0,
            'headings_per_sentence': round(heading_count / total_sentences, 2) if total_sentences > 0 else 0,
            'lists_per_sentence': round(list_count / total_sentences, 2) if total_sentences > 0 else 0
        }

        # Compile all metrics (raw only, no weighted scores)
        all_metrics = {
            'format': format_type,
            'basic_counts': {
                'total_words': total_words,
                'total_lines': total_lines,
                'total_sentences': total_sentences,
                'headings': heading_count,
                'list_items': list_count
            },
            'structure': structure,
            'densities': densities
        }

        return all_metrics

    def print_report(self, results: Dict):
        """
        Print a formatted structure analysis report.

        Args:
            results: Results from analyze()
        """
        print("=" * 70)
        print("DOCUMENT STRUCTURE ANALYSIS REPORT")
        print("=" * 70)

        # Format detection
        print(f"\n### DOCUMENT FORMAT ###\n")
        print(f"  Detected Format:              {results['format'].upper()}")

        # Basic counts
        print(f"\n### BASIC COUNTS ###\n")
        basic = results['basic_counts']
        print(f"  Total Words:                  {basic['total_words']:,}")
        print(f"  Total Lines:                  {basic['total_lines']:,}")
        print(f"  Headings:                     {basic['headings']}")
        print(f"  List Items:                   {basic['list_items']}")

        # Heading analysis
        if results['format'] == 'markdown':
            print(f"\n### HEADING HIERARCHY ###\n")
            headings = results['structure']['headings']
            for level in range(1, 7):
                if headings[level] > 0:
                    print(f"  Level {level} (H{level}):              {headings[level]}")

            print(f"\n  Max Heading Depth:            {results['structure']['max_heading_depth']}")
        elif results['format'] == 'html':
            print(f"\n### HEADING HIERARCHY ###\n")
            headings = results['structure']['headings']
            for level in range(1, 7):
                if headings[level] > 0:
                    print(f"  Level {level} (H{level}):              {headings[level]}")

        # Density metrics
        print(f"\n### DENSITY METRICS ###\n")
        dens = results['densities']
        print(f"  Heading Density:              {dens['heading_density']:.2f} per 1000 words")
        print(f"  List Density:                 {dens['list_density']:.2f} per 100 lines")
        print(f"  Headings per 100 Lines:       {dens['heading_per_100_lines']:.2f}")
        print(f"  List Items per 100 Lines:     {dens['list_per_100_lines']:.2f}")
        print(f"  Headings per Sentence:        {dens['headings_per_sentence']:.2f}")
        print(f"  Lists per Sentence:           {dens['lists_per_sentence']:.2f}")

        print("=" * 70)


def main():
    """Command line interface."""
    if len(sys.argv) < 2:
        print("Usage: python3 structure_analyzer.py <file_path> [--json]")
        print("\nAnalyzes document structure through heading and list detection.")
        sys.exit(1)

    file_path = sys.argv[1]
    output_json = '--json' in sys.argv

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        analyzer = StructureAnalyzer()
        results = analyzer.analyze(text)

        if output_json:
            print(json.dumps(results, indent=2))
        else:
            analyzer.print_report(results)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing file: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
