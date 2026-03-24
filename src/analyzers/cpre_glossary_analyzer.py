#!/usr/bin/env python3
"""
CPRE Glossary Coverage Analyzer
Measures Requirements Engineering vocabulary usage based on IREB CPRE terms.
"""

import re
from typing import Dict, List
from collections import Counter
import json
import sys


class CPREGlossaryAnalyzer:
    """
    Analyzes text for IREB CPRE (Certified Professional for Requirements Engineering)
    glossary term usage.

    Focuses on:
    - Vocabulary coverage (% of 198 CPRE terms used)
    - Term density (CPRE terms per 100 words)
    """

    def __init__(self):
        """Initialize with IREB CPRE glossary terms."""
        # 198 official CPRE terms from IREB Glossary
        # Source: https://www.ireb.org/en/cpre/cpre-glossary/

        self.cpre_terms = {
            "Requirements Types": [
                "acceptance criteria", "activity", "adequacy", "attribute", "backlog item",
                "business requirement", "compliance", "constraint", "customer requirements specification",
                "domain requirement", "epic", "feature", "functional requirement",
                "item", "non-functional requirement", "performance requirement",
                "quality requirement", "requirement", "safety", "security", "user requirement"
            ],
            "Artifacts & Documents": [
                "artifact", "backlog", "baseline", "document template", "form template",
                "glossary", "model", "phrase template", "product backlog",
                "requirements document", "requirements specification", "requirements template",
                "software requirements specification", "specification", "sprint backlog",
                "story map", "storyboard", "system requirements specification",
                "template", "user story template", "work product", "customer requirements specification", "wireframe"
            ],
            "Activities & Processes": [
                "acceptance test", "activity", "elaboration", "elicitation", "inspection",
                "iteration", "negotiation", "prioritization", "prototyping", "refactoring",
                "requirements analysis", "requirements discovery", "requirements elicitation",
                "requirements management", "requirements negotiation", "review", "spike",
                "sprint", "timebox", "validation", "verification", "walkthrough"
            ],
            "Quality Criteria": [
                "ambiguity", "completeness", "consistency", "correctness", "feasibility",
                "modifiability", "necessity", "quality", "quality criteria", "traceability",
                "unambiguity", "understandability", "verifiability", "changeability",
                "efficiency", "maintainability", "portability", "reliability", "usability",
                "fault tolerance", "conformity", "adequacy"
            ],
            "Modeling & Techniques": [
                "activity diagram", "activity model", "class diagram", "class model",
                "context diagram", "context model", "data flow diagram", "data flow model",
                "decision table", "domain model", "entity-relationship diagram",
                "entity-relationship model", "feature diagram", "feature model",
                "goal model", "interaction model", "mock-up", "object diagram",
                "object model", "persona", "process model", "prototype", "scenario",
                "sequence diagram", "state machine", "state machine diagram",
                "state-transition diagram", "statechart", "use case", "use case diagram",
                "use case model", "view"
            ],
            "Roles & Stakeholders": [
                "actor", "client", "customer", "end user", "product owner",
                "requirements engineer", "role", "scrum", "stakeholder", "supplier", "user"
            ],
            "Concepts & Theory": [
                "agile", "behavior", "behavior model", "branch", "bug", "burndown chart",
                "cardinality", "change management", "change request", "class", "commonality",
                "component", "composition", "configuration", "conflict", "context",
                "context boundary", "control flow", "data flow", "defect", "design",
                "domain", "effectiveness", "entity", "error", "evolutionary prototype",
                "exploratory prototype", "fault", "functionality", "homonym", "increment",
                "kind of requirement", "language", "method", "methodology", "multiplicity",
                "native prototype", "natural language", "object", "practice", "priority",
                "problem", "process", "product", "product line", "release", "redundancy",
                "requirements baseline", "requirements branching", "requirements configuration",
                "requirements conflict", "requirements model", "requirements source", "risk",
                "scope", "semantics", "semi-formal", "service", "source", "specification by example",
                "specification language", "standard", "story", "structured analysis",
                "synonym", "syntax", "system", "system boundary", "system context",
                "system requirement", "task", "technique", "tool", "UML", "user story",
                "variability", "variant", "variation point", "velocity", "version",
                "viewpoint", "vision", "association"
            ]
        }

        # Flatten all terms for overall counting
        self.all_terms = []
        for category_terms in self.cpre_terms.values():
            self.all_terms.extend(category_terms)

        # Remove duplicates
        self.all_terms = list(set(self.all_terms))
        self.total_terms_available = len(self.all_terms)

    def tokenize_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        text = re.sub(r'\s+', ' ', text)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences

    def analyze(self, text: str) -> Dict:
        """
        Analyze text for CPRE term usage.

        Args:
            text: Input text to analyze

        Returns:
            Dictionary with term density per sentence
        """
        # Count sentences
        sentences = self.tokenize_sentences(text)
        total_sentences = len(sentences)

        if total_sentences == 0:
            return {
                "total_sentences": 0,
                "total_term_occurrences": 0,
                "cpre_terms_per_sentence": 0
            }

        # Find all CPRE terms
        term_occurrences = {}
        for term in self.all_terms:
            # Use word boundaries for exact matching
            pattern = r'\b' + re.escape(term) + r'\b'
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                term_occurrences[term] = len(matches)

        # Calculate metrics
        total_term_occurrences = sum(term_occurrences.values())
        terms_per_sentence = total_term_occurrences / total_sentences

        return {
            "total_sentences": total_sentences,
            "total_term_occurrences": total_term_occurrences,
            "cpre_terms_per_sentence": round(terms_per_sentence, 2)
        }

    def print_report(self, results: Dict):
        """
        Print a formatted CPRE glossary analysis report.

        Args:
            results: Results from analyze()
        """
        print("=" * 70)
        print("CPRE GLOSSARY ANALYSIS")
        print("=" * 70)

        print(f"\n### CPRE TERM DENSITY ###\n")
        print(f"  Total Sentences:              {results['total_sentences']}")
        print(f"  CPRE Term Occurrences:        {results['total_term_occurrences']}")
        print(f"  Terms per Sentence:           {results['cpre_terms_per_sentence']:.2f}")

        print("\n" + "=" * 70)


def main():
    """Command line interface."""
    if len(sys.argv) < 2:
        print("Usage: python3 cpre_glossary_analyzer.py <file_path> [--json]")
        print("\nAnalyzes CPRE glossary term usage in requirements documents.")
        sys.exit(1)

    file_path = sys.argv[1]
    output_json = '--json' in sys.argv

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        analyzer = CPREGlossaryAnalyzer()
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
