#!/usr/bin/env python3.9
"""
Entity-Based Coherence Model Analyzer using TRUNAJOD
Analyzes text coherence using Entity Grid models.
"""

import sys
import spacy
from TRUNAJOD import entity_grid
from typing import Dict, List, Tuple
import json


class EntityCoherenceAnalyzer:
    """
    Analyzes text coherence using Entity-Based Coherence Model via TRUNAJOD library.
    """

    def __init__(self, model_name='en_core_web_sm'):
        """
        Initialize the analyzer with a spaCy language model.

        Args:
            model_name: Name of the spaCy model to use (default: en_core_web_sm)
        """
        print(f"Loading spaCy model: {model_name}...")
        try:
            self.nlp = spacy.load(model_name)
            print("Model loaded successfully!")
        except OSError:
            print(f"Error: Model '{model_name}' not found.")
            print(f"Please install it with: python3.9 -m spacy download {model_name}")
            sys.exit(1)

    def analyze(self, text: str) -> Dict:
        """
        Perform entity-based coherence analysis on text.

        Args:
            text: Input text to analyze

        Returns:
            Dictionary containing coherence metrics and entity grid information
        """
        # Process text with spaCy
        print("Processing text with spaCy...")
        doc = self.nlp(text)

        # Create entity grid
        print("Creating entity grid...")
        egrid = entity_grid.EntityGrid(doc, model_name='spacy')

        # Get basic information
        sentence_count = egrid.get_sentence_count()

        # Get entity grid for inspection
        grid_dict = egrid.get_egrid()

        # Count entities
        entity_count = len(grid_dict)

        # Get all entity transition ratios
        transitions = self._get_all_transitions(egrid)

        # Get local coherence scores
        print("Calculating local coherence scores...")
        coherence_scores = entity_grid.get_local_coherence(egrid)

        # Analyze entity distribution
        entity_stats = self._analyze_entity_distribution(grid_dict, sentence_count)

        return {
            'basic_info': {
                'sentence_count': sentence_count,
                'entity_count': entity_count,
                'avg_entities_per_sentence': round(entity_count / sentence_count, 2) if sentence_count > 0 else 0
            },
            'coherence_scores': {
                'PU': coherence_scores[0],  # Probability-based Uniform
                'PW': coherence_scores[1],  # Probability-based Weighted
                'PACC_uniform': coherence_scores[2],  # Accuracy-based Uniform
                'PACC_weighted': coherence_scores[3]  # Accuracy-based Weighted
            },
            'entity_transitions': transitions,
            'entity_statistics': entity_stats,
            'entity_grid_sample': self._get_grid_sample(grid_dict, limit=10)
        }

    def _get_all_transitions(self, egrid) -> Dict[str, float]:
        """
        Get all entity transition ratios from the entity grid.

        Transitions represent how entities move between syntactic roles:
        - S: Subject
        - O: Object
        - X: Other
        - -: Absent (represented as 'n' in some transitions)
        """
        return {
            # Subject transitions
            'SS': egrid.get_ss_transitions(),  # Subject -> Subject
            'SN': egrid.get_sn_transitions(),  # Subject -> Absent
            'SO': egrid.get_so_transitions(),  # Subject -> Object
            'SX': egrid.get_sx_transitions(),  # Subject -> Other

            # Absent transitions (N)
            'NS': egrid.get_ns_transitions(),  # Absent -> Subject
            'NN': egrid.get_nn_transitions(),  # Absent -> Absent
            'NO': egrid.get_no_transitions(),  # Absent -> Object
            'NX': egrid.get_nx_transitions(),  # Absent -> Other

            # Object transitions
            'OS': egrid.get_os_transitions(),  # Object -> Subject
            'ON': egrid.get_on_transitions(),  # Object -> Absent
            'OO': egrid.get_oo_transitions(),  # Object -> Object
            'OX': egrid.get_ox_transitions(),  # Object -> Other

            # Other transitions
            'XS': egrid.get_xs_transitions(),  # Other -> Subject
            'XN': egrid.get_xn_transitions(),  # Other -> Absent
            'XO': egrid.get_xo_transitions(),  # Other -> Object
            'XX': egrid.get_xx_transitions(),  # Other -> Other
        }

    def _analyze_entity_distribution(self, grid_dict: Dict, sentence_count: int) -> Dict:
        """
        Analyze how entities are distributed across sentences.
        """
        if not grid_dict:
            return {
                'avg_entity_span': 0,
                'max_entity_span': 0,
                'entities_appearing_once': 0,
                'entities_appearing_multiple': 0
            }

        entity_spans = []
        single_occurrence = 0
        multiple_occurrence = 0

        for entity, roles in grid_dict.items():
            # Count non-absent roles
            appearances = sum(1 for role in roles if role != '-')

            if appearances == 1:
                single_occurrence += 1
            elif appearances > 1:
                multiple_occurrence += 1

            # Calculate span (first to last appearance)
            role_indices = [i for i, role in enumerate(roles) if role != '-']
            if role_indices:
                span = max(role_indices) - min(role_indices) + 1
                entity_spans.append(span)

        return {
            'avg_entity_span': round(sum(entity_spans) / len(entity_spans), 2) if entity_spans else 0,
            'max_entity_span': max(entity_spans) if entity_spans else 0,
            'entities_appearing_once': single_occurrence,
            'entities_appearing_multiple': multiple_occurrence,
            'entity_persistence_ratio': round(multiple_occurrence / len(grid_dict), 2) if grid_dict else 0
        }

    def _get_grid_sample(self, grid_dict: Dict, limit: int = 10) -> Dict:
        """
        Get a sample of the entity grid for inspection.
        """
        if not grid_dict:
            return {}

        # Sort by number of appearances (most frequent first)
        sorted_entities = sorted(
            grid_dict.items(),
            key=lambda x: sum(1 for role in x[1] if role != '-'),
            reverse=True
        )

        # Return top entities
        return {entity: roles for entity, roles in sorted_entities[:limit]}

    def print_report(self, results: Dict, detailed: bool = True):
        """
        Print a formatted report of the entity-based coherence analysis.
        """
        print("\n" + "=" * 70)
        print("ENTITY-BASED COHERENCE ANALYSIS REPORT")
        print("=" * 70)

        # Basic Information
        print("\n### BASIC INFORMATION ###\n")
        basic = results['basic_info']
        print(f"  Sentences:                    {basic['sentence_count']}")
        print(f"  Unique Entities:              {basic['entity_count']}")
        print(f"  Avg Entities per Sentence:    {basic['avg_entities_per_sentence']}")

        # Coherence Scores
        print("\n### COHERENCE SCORES ###\n")
        scores = results['coherence_scores']
        print("Entity Grid Local Coherence Metrics:")
        print(f"  PU  (Probability Uniform):    {scores['PU']:.4f}")
        print(f"  PW  (Probability Weighted):   {scores['PW']:.4f}")
        print(f"  PACC_U (Accuracy Uniform):    {scores['PACC_uniform']:.4f}")
        print(f"  PACC_W (Accuracy Weighted):   {scores['PACC_weighted']:.4f}")

        print("\nInterpretation:")
        print("  Higher scores indicate better local coherence.")
        print("  Weighted metrics emphasize syntactic importance (S > O > X).")

        # Entity Statistics
        print("\n### ENTITY DISTRIBUTION ###\n")
        stats = results['entity_statistics']
        print(f"  Avg Entity Span:              {stats['avg_entity_span']} sentences")
        print(f"  Max Entity Span:              {stats['max_entity_span']} sentences")
        print(f"  Single-occurrence Entities:   {stats['entities_appearing_once']}")
        print(f"  Multi-occurrence Entities:    {stats['entities_appearing_multiple']}")
        print(f"  Entity Persistence Ratio:     {stats['entity_persistence_ratio']}")

        print("\nInterpretation:")
        print("  Higher entity spans indicate better entity continuity.")
        print("  Higher persistence ratio suggests more cohesive text.")

        # Entity Transitions
        if detailed:
            print("\n### ENTITY TRANSITIONS ###\n")
            trans = results['entity_transitions']

            print("Entity Role Transitions (S=Subject, O=Object, X=Other, N=Absent):")
            print("\nSubject Transitions:")
            print(f"  S -> S: {trans['SS']:.4f}  (Subject continuity)")
            print(f"  S -> O: {trans['SO']:.4f}  (Subject to object)")
            print(f"  S -> X: {trans['SX']:.4f}  (Subject to other role)")
            print(f"  S -> N: {trans['SN']:.4f}  (Subject disappears)")

            print("\nObject Transitions:")
            print(f"  O -> S: {trans['OS']:.4f}  (Object becomes subject)")
            print(f"  O -> O: {trans['OO']:.4f}  (Object continuity)")
            print(f"  O -> X: {trans['OX']:.4f}  (Object to other role)")
            print(f"  O -> N: {trans['ON']:.4f}  (Object disappears)")

            print("\nNew Entity Introduction:")
            print(f"  N -> S: {trans['NS']:.4f}  (New subject introduced)")
            print(f"  N -> O: {trans['NO']:.4f}  (New object introduced)")
            print(f"  N -> X: {trans['NX']:.4f}  (New other role introduced)")

            print("\nOther Transitions:")
            print(f"  X -> S: {trans['XS']:.4f}")
            print(f"  X -> O: {trans['XO']:.4f}")
            print(f"  X -> X: {trans['XX']:.4f}")
            print(f"  X -> N: {trans['XN']:.4f}")

            print("\nKey Patterns:")
            if trans['SS'] > 0.3:
                print("  ✓ Strong subject continuity (good for coherence)")
            if trans['OS'] > 0.2:
                print("  ✓ Good object-to-subject promotion (topic progression)")
            if trans['SN'] > 0.5:
                print("  ⚠ Many subjects disappear (may indicate weak coherence)")

        # Entity Grid Sample
        if detailed and results['entity_grid_sample']:
            print("\n### ENTITY GRID SAMPLE (Top 10 Entities) ###\n")
            print("Entity role across sentences (S=Subj, O=Obj, X=Other, -=Absent):\n")

            for entity, roles in results['entity_grid_sample'].items():
                # Truncate long entity names
                entity_display = entity[:30] + "..." if len(entity) > 30 else entity
                roles_str = " ".join(roles)
                print(f"  {entity_display:35} {roles_str}")

        print("\n" + "=" * 70)


def main():
    """
    Main function to analyze the srs.md file.
    """
    # Initialize analyzer
    analyzer = EntityCoherenceAnalyzer(model_name='en_core_web_sm')

    # Read the file
    file_path = 'srs.md'

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        print(f"\nAnalyzing file: {file_path}")
        print(f"File size: {len(text)} characters\n")

        # Perform analysis
        results = analyzer.analyze(text)

        # Print report
        analyzer.print_report(results, detailed=True)

        # Save results to JSON
        try:
            output_file = 'entity_coherence_results.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                # Convert numpy floats to regular floats for JSON serialization
                json_results = {
                    'basic_info': results['basic_info'],
                    'coherence_scores': {k: float(v) for k, v in results['coherence_scores'].items()},
                    'entity_transitions': {k: float(v) for k, v in results['entity_transitions'].items()},
                    'entity_statistics': results['entity_statistics'],
                    'entity_grid_sample': results['entity_grid_sample']
                }
                json.dump(json_results, f, indent=2)
            print(f"\nResults also saved to: {output_file}")
        except Exception as e:
            print(f"\nNote: Could not save JSON results: {e}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("\nUsage: You can also use this as a module:")
        print("  from entity_coherence_analyzer import EntityCoherenceAnalyzer")
        print("  analyzer = EntityCoherenceAnalyzer()")
        print("  results = analyzer.analyze('Your text here')")
        print("  analyzer.print_report(results)")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
