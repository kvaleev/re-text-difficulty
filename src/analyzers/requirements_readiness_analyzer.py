#!/usr/bin/env python3
"""
Requirements Readiness Analyzer
Measures whether a text is a formal requirements document (SRS) or a narrative brief.

Based on structural/syntactic and semantic/lexical features that distinguish
formal requirements from descriptive narratives.
"""

import re
import statistics
from typing import Dict, List, Tuple, Set
import json
import sys
from collections import Counter

# Try to import spaCy for NLP-based SAO analysis
try:
    import spacy
    SPACY_AVAILABLE = True
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # Model not downloaded
        SPACY_AVAILABLE = False
        nlp = None
except ImportError:
    SPACY_AVAILABLE = False
    nlp = None


class RequirementsReadinessAnalyzer:
    """
    Analyzes text to determine its readiness as a formal requirements document.

    Uses two primary dimensions:
    1. Structuring Score: Syntactic and structural features
    2. Readiness Score: Semantic and lexical features
    """

    def __init__(self):
        """Initialize the analyzer with patterns and reference lists."""

        # Modal verbs categorized by strength
        self.strong_modals = ['shall', 'must', 'will', 'required', 'requires']
        self.weak_modals = ['should', 'could', 'might', 'may', 'can']
        self.prohibited_modals = ['shall not', 'must not', 'will not']

        # Ambiguous terms (IEEE 830 warns against these)
        self.vague_words = [
            'etc', 'and/or', 'some', 'several', 'many', 'most', 'few',
            'easy', 'difficult', 'user-friendly', 'intuitive', 'simple',
            'fast', 'slow', 'reliable', 'flexible', 'robust', 'adequate',
            'appropriate', 'reasonable', 'sufficient', 'meaningful',
            'support', 'handle', 'process', 'various', 'normally',
            'typically', 'usually', 'generally', 'often'
        ]

        # Anaphoric references (pronouns that create ambiguity)
        self.anaphora = [
            'it', 'this', 'that', 'these', 'those', 'they', 'them',
            'he', 'she', 'his', 'her', 'their', 'its'
        ]

        # Requirements-style subjects (typical actors in SRS)
        self.requirements_subjects = [
            'system', 'application', 'software', 'program', 'module',
            'component', 'interface', 'database', 'server', 'client',
            'user', 'administrator', 'operator', 'customer'
        ]

        # Action verbs common in requirements
        self.action_verbs = [
            'display', 'show', 'present', 'provide', 'allow', 'enable',
            'support', 'accept', 'validate', 'verify', 'check', 'ensure',
            'store', 'retrieve', 'save', 'load', 'send', 'receive',
            'process', 'calculate', 'generate', 'create', 'update',
            'delete', 'remove', 'add', 'modify', 'change', 'set'
        ]

    def tokenize_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        # Simple sentence splitting
        text = re.sub(r'\s+', ' ', text)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences

    def analyze_sentence_length_variation(self, text: str) -> Dict:
        """
        Analyze sentence length variation (structural feature).

        Low variation suggests consistent, deliberate style typical of technical writing.

        Args:
            text: Input text

        Returns:
            Dictionary with variation metrics
        """
        sentences = self.tokenize_sentences(text)

        if not sentences:
            return {
                'count': 0,
                'avg_length': 0,
                'std_dev': 0,
                'coefficient_of_variation': 0
            }

        # Calculate word counts per sentence
        word_counts = []
        for sent in sentences:
            words = re.findall(r'\b[a-zA-Z]+\b', sent)
            word_counts.append(len(words))

        avg_length = statistics.mean(word_counts)
        std_dev = statistics.stdev(word_counts) if len(word_counts) > 1 else 0

        # Coefficient of variation (CV)
        cv = std_dev / avg_length if avg_length > 0 else 0

        return {
            'count': len(sentences),
            'avg_length': round(avg_length, 2),
            'std_dev': round(std_dev, 2),
            'coefficient_of_variation': round(cv, 3)
        }

    def _interpret_cv(self, cv: float) -> str:
        """Interpret coefficient of variation."""
        if cv < 0.4:
            return "Very Consistent (Requirements-like)"
        elif cv < 0.6:
            return "Consistent (Technical Writing)"
        elif cv < 0.8:
            return "Moderate Variation (Mixed Style)"
        else:
            return "High Variation (Narrative Style)"

    def analyze_imperative_sentences(self, text: str) -> Dict:
        """
        Identify and count imperative sentences (structural feature).

        Requirements are fundamentally directives. High ratio indicates SRS.

        Args:
            text: Input text

        Returns:
            Dictionary with imperative analysis
        """
        sentences = self.tokenize_sentences(text)

        if not sentences:
            return {
                'total_sentences': 0,
                'imperative_count': 0,
                'imperative_ratio': 0,
                'score': 0
            }

        imperative_count = 0
        imperative_patterns = [
            r'^\s*The\s+(system|application|software|program)',
            r'\b(shall|must|will|should)\s+',
            r'^\s*[A-Z][a-z]+\s+(shall|must|will)',
            r'\b(display|provide|allow|enable|support|validate|verify)\b'
        ]

        for sent in sentences:
            sent_lower = sent.lower()
            for pattern in imperative_patterns:
                if re.search(pattern, sent_lower):
                    imperative_count += 1
                    break

        ratio = imperative_count / len(sentences)

        # Score: Higher ratio = higher score
        # Typical SRS: 60-90% imperative
        # Typical narrative: 10-30% imperative
        if ratio >= 0.6:
            score = 1.0
        elif ratio >= 0.4:
            score = 0.7
        elif ratio >= 0.2:
            score = 0.4
        else:
            score = 0.1

        return {
            'total_sentences': len(sentences),
            'imperative_count': imperative_count,
            'imperative_ratio': round(ratio, 3),
            'imperative_percentage': round(ratio * 100, 1),
            'score': round(score, 2),
            'interpretation': self._interpret_imperative_ratio(ratio)
        }

    def _interpret_imperative_ratio(self, ratio: float) -> str:
        """Interpret imperative sentence ratio."""
        if ratio >= 0.6:
            return "Very High (SRS-like)"
        elif ratio >= 0.4:
            return "High (Technical Specification)"
        elif ratio >= 0.2:
            return "Moderate (Mixed Document)"
        else:
            return "Low (Narrative/Descriptive)"

    def analyze_ambiguity(self, text: str) -> Dict:
        """
        Measure ambiguity through vague words and anaphora (semantic feature).

        Low ambiguity = requirement ready.
        Densities are calculated per sentence (not per word).

        Args:
            text: Input text

        Returns:
            Dictionary with ambiguity analysis
        """
        text_lower = text.lower()

        # Count sentences
        sentences = self.tokenize_sentences(text)
        total_sentences = len(sentences)

        if total_sentences == 0:
            return {
                'vague_words': {'counts': {}, 'total': 0, 'per_sentence': 0, 'top_offenders': []},
                'anaphora': {'counts': {}, 'total': 0, 'per_sentence': 0, 'top_offenders': []},
                'total_sentences': 0
            }

        # Count vague words
        vague_counts = {}
        total_vague = 0
        for word in self.vague_words:
            count = text_lower.count(word)
            if count > 0:
                vague_counts[word] = count
                total_vague += count

        # Count anaphoric references
        anaphora_counts = {}
        total_anaphora = 0
        for word in self.anaphora:
            # Use word boundaries to avoid false matches
            count = len(re.findall(r'\b' + word + r'\b', text_lower))
            if count > 0:
                anaphora_counts[word] = count
                total_anaphora += count

        # Calculate densities per sentence
        vague_per_sentence = total_vague / total_sentences
        anaphora_per_sentence = total_anaphora / total_sentences

        return {
            'vague_words': {
                'counts': vague_counts,
                'total': total_vague,
                'per_sentence': round(vague_per_sentence, 2),
                'top_offenders': sorted(vague_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            },
            'anaphora': {
                'counts': anaphora_counts,
                'total': total_anaphora,
                'per_sentence': round(anaphora_per_sentence, 2),
                'top_offenders': sorted(anaphora_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            },
            'total_sentences': total_sentences
        }

    def _interpret_ambiguity(self, density: float) -> str:
        """Interpret ambiguity density (legacy, per word)."""
        if density < 2.0:
            return "Very Low Ambiguity (Requirements Ready)"
        elif density < 5.0:
            return "Low Ambiguity (Acceptable for SRS)"
        elif density < 10.0:
            return "Moderate Ambiguity (Needs Refinement)"
        else:
            return "High Ambiguity (Narrative/Vague)"

    def _interpret_ambiguity_per_sentence(self, per_sentence: float) -> str:
        """Interpret ambiguity per sentence."""
        if per_sentence < 0.5:
            return "Very Low Ambiguity (Requirements Ready)"
        elif per_sentence < 1.0:
            return "Low Ambiguity (Acceptable for SRS)"
        elif per_sentence < 2.0:
            return "Moderate Ambiguity (Needs Refinement)"
        else:
            return "High Ambiguity (Narrative/Vague)"


    def analyze_subject_action_object(self, text: str) -> Dict:
        """
        Analyze Subject-Modal-Action-Object patterns (semantic feature).

        Focuses on requirements-style sentences with modal verbs (shall|must|will).
        Also tracks subject consistency (e.g., how consistently "system" is used).

        Uses NLP-based dependency parsing when spaCy is available,
        otherwise falls back to pattern matching.

        Requirements follow: "The [system] shall [action] [object]"

        Args:
            text: Input text

        Returns:
            Dictionary with SMAO analysis including subject consistency
        """
        if SPACY_AVAILABLE and nlp:
            return self._analyze_sao_nlp(text)
        else:
            return self._analyze_sao_regex(text)

    def _analyze_sao_nlp(self, text: str) -> Dict:
        """
        NLP-based SMAO analysis using spaCy dependency parsing.

        Looks ONLY for sentences with Subject-Modal-Action-Object structure:
        - Modal verb (shall|must|will) as auxiliary
        - Subject (nsubj, nsubjpass): The actor/system
        - Verb (ROOT or head of aux): The action
        - Object (dobj, pobj, attr, acomp): What is acted upon

        Also tracks subject consistency across all SMAO sentences.

        Args:
            text: Input text

        Returns:
            Dictionary with SMAO analysis including subject consistency
        """
        sentences = self.tokenize_sentences(text)

        if not sentences:
            return {
                'total_sentences': 0,
                'smao_sentences': 0,
                'smao_ratio': 0,
                'subject_consistency': {},
                'score': 0,
                'method': 'nlp',
                'examples': []
            }

        smao_count = 0
        smao_examples = []
        smao_patterns = []
        subject_counter = Counter()  # Track which subjects are used
        modal_verbs_only = ['shall', 'must', 'will']  # Only these three

        for sent in sentences:
            # Parse with spaCy
            doc = nlp(sent)

            # Look for modal + verb pattern with subject and object
            has_smao = False
            subject = None
            modal = None
            verb = None
            obj = None

            # Find modal auxiliary verbs (shall/must/will)
            for token in doc:
                if token.dep_ == "aux" and token.text.lower() in modal_verbs_only:
                    modal = token.text
                    # Find the verb this modal modifies
                    verb_token = token.head
                    if verb_token.pos_ == "VERB":
                        verb = verb_token.text

                        # Find subject of this verb
                        for child in verb_token.children:
                            if child.dep_ in ("nsubj", "nsubjpass"):
                                # Get the full subject (including "the system", not just "system")
                                subject_tokens = [child]
                                # Check for determiners and compound subjects
                                for subchild in child.children:
                                    if subchild.dep_ in ("det", "compound", "amod"):
                                        subject_tokens.append(subchild)
                                # Sort by position and join
                                subject_tokens.sort(key=lambda t: t.i)
                                subject = " ".join([t.text for t in subject_tokens])

                                # Extract the core subject noun
                                subject_core = child.text.lower()

                                # Check if it's a requirements subject
                                if subject_core in self.requirements_subjects:
                                    # Find object
                                    for obj_child in verb_token.children:
                                        if obj_child.dep_ in ("dobj", "attr", "acomp"):
                                            obj = obj_child.text
                                            has_smao = True
                                            break

                                    # Also check for prepositional objects
                                    if not has_smao:
                                        for prep in verb_token.children:
                                            if prep.dep_ == "prep":
                                                for prep_child in prep.children:
                                                    if prep_child.dep_ == "pobj":
                                                        obj = prep_child.text
                                                        has_smao = True
                                                        break
                                                if has_smao:
                                                    break

                    if has_smao:
                        break

            if has_smao:
                smao_count += 1
                if len(smao_examples) < 5:
                    smao_examples.append(sent[:100] + '...' if len(sent) > 100 else sent)
                if subject and modal and verb and obj:
                    smao_patterns.append(f"{subject} {modal} {verb} {obj}")
                    # Track the core subject for consistency analysis
                    subject_counter[subject_core] += 1

        ratio = smao_count / len(sentences) if sentences else 0

        # Calculate subject consistency
        subject_consistency = {}
        if subject_counter:
            total_smao = sum(subject_counter.values())
            most_common_subject, most_common_count = subject_counter.most_common(1)[0]
            consistency_percentage = (most_common_count / total_smao) * 100

            subject_consistency = {
                'dominant_subject': most_common_subject,
                'dominant_count': most_common_count,
                'total_smao_sentences': total_smao,
                'consistency_percentage': round(consistency_percentage, 1),
                'all_subjects': dict(subject_counter.most_common()),
                'interpretation': self._interpret_subject_consistency(consistency_percentage)
            }

        return {
            'total_sentences': len(sentences),
            'smao_sentences': smao_count,
            'smao_ratio': round(ratio, 3),
            'smao_percentage': round(ratio * 100, 1),
            'examples': smao_examples,
            'patterns': smao_patterns[:5] if smao_patterns else [],
            'subject_consistency': subject_consistency,
            'method': 'nlp'
        }

    def _analyze_sao_regex(self, text: str) -> Dict:
        """
        Fallback regex-based SMAO analysis (when spaCy unavailable).

        Looks ONLY for sentences with modal verbs (shall|must|will)
        combined with requirements subjects and action verbs.

        Args:
            text: Input text

        Returns:
            Dictionary with SMAO analysis
        """
        sentences = self.tokenize_sentences(text)

        if not sentences:
            return {
                'total_sentences': 0,
                'smao_sentences': 0,
                'smao_ratio': 0,
                'subject_consistency': {},
                'score': 0,
                'method': 'regex',
                'examples': []
            }

        smao_count = 0
        smao_examples = []
        subject_counter = Counter()
        modal_verbs_only = ['shall', 'must', 'will']

        for sent in sentences:
            sent_lower = sent.lower()

            # Check for modal verbs ONLY (not should/could/may)
            has_modal = any(modal in sent_lower for modal in modal_verbs_only)

            if has_modal:
                # Check for requirements subject
                has_subject = False
                found_subject = None
                for subj in self.requirements_subjects:
                    if subj in sent_lower:
                        has_subject = True
                        found_subject = subj
                        break

                # Check for action verb
                has_action = any(verb in sent_lower for verb in self.action_verbs)

                # Count as SMAO if it has modal + subject + action
                if has_subject and has_action:
                    smao_count += 1
                    subject_counter[found_subject] += 1
                    if len(smao_examples) < 5:
                        smao_examples.append(sent[:100] + '...' if len(sent) > 100 else sent)

        ratio = smao_count / len(sentences) if sentences else 0

        # Calculate subject consistency
        subject_consistency = {}
        if subject_counter:
            total_smao = sum(subject_counter.values())
            most_common_subject, most_common_count = subject_counter.most_common(1)[0]
            consistency_percentage = (most_common_count / total_smao) * 100

            subject_consistency = {
                'dominant_subject': most_common_subject,
                'dominant_count': most_common_count,
                'total_smao_sentences': total_smao,
                'consistency_percentage': round(consistency_percentage, 1),
                'all_subjects': dict(subject_counter.most_common()),
                'interpretation': self._interpret_subject_consistency(consistency_percentage)
            }

        return {
            'total_sentences': len(sentences),
            'smao_sentences': smao_count,
            'smao_ratio': round(ratio, 3),
            'smao_percentage': round(ratio * 100, 1),
            'examples': smao_examples,
            'subject_consistency': subject_consistency,
            'method': 'regex'
        }

    def _interpret_subject_consistency(self, consistency: float) -> str:
        """Interpret subject consistency percentage."""
        if consistency >= 80:
            return "Very High Consistency (Excellent)"
        elif consistency >= 60:
            return "High Consistency (Good)"
        elif consistency >= 40:
            return "Moderate Consistency (Acceptable)"
        else:
            return "Low Consistency (Needs Improvement)"

    def _interpret_sao(self, ratio: float) -> str:
        """Interpret SAO ratio."""
        if ratio >= 0.5:
            return "Very High (Strong Requirements Pattern)"
        elif ratio >= 0.3:
            return "High (Requirements-like)"
        elif ratio >= 0.15:
            return "Moderate (Mixed Style)"
        else:
            return "Low (Narrative/Descriptive)"

    def calculate_metrics(self, features: Dict) -> Dict:
        """
        Extract raw metrics from features.

        Args:
            features: All extracted features

        Returns:
            Dictionary with raw metrics only (no scores or thresholds)
        """
        sv = features['sentence_variation']
        amb = features['ambiguity']
        sao = features['sao_pattern']

        metrics = {
            # Sentence structure
            'sentence_count': sv['count'],
            'avg_sentence_length': sv['avg_length'],
            'sentence_length_std_dev': sv['std_dev'],
            'sentence_cv': sv['coefficient_of_variation'],
            # Ambiguity
            'vague_words_count': amb['vague_words']['total'],
            'vague_words_per_sentence': amb['vague_words']['per_sentence'],
            'anaphora_count': amb['anaphora']['total'],
            'anaphora_per_sentence': amb['anaphora']['per_sentence'],
            # SMAO pattern
            'smao_sentences_count': sao.get('smao_sentences', 0),
            'smao_percentage': sao.get('smao_percentage', 0),
        }

        # Add subject consistency if available
        if 'subject_consistency' in sao and sao['subject_consistency']:
            metrics['subject_consistency_percentage'] = sao['subject_consistency']['consistency_percentage']
            metrics['dominant_subject'] = sao['subject_consistency']['dominant_subject']

        return metrics

    def _classify_document(self, structural: float, readiness: float) -> str:
        """
        Classify document type based on scores.

        Args:
            structural: Structural score (0-1)
            readiness: Readiness score (0-1)

        Returns:
            Classification string
        """
        avg = (structural + readiness) / 2

        if avg >= 0.75:
            return "Formal SRS / Requirements Document"
        elif avg >= 0.55:
            return "Technical Specification (Requirements-like)"
        elif avg >= 0.35:
            return "Mixed Document (Part Requirements, Part Narrative)"
        elif avg >= 0.20:
            return "Informal Brief / Descriptive Document"
        else:
            return "Narrative / Non-Requirements Document"

    def _calculate_confidence(self, structural: float, readiness: float) -> str:
        """Calculate confidence in classification."""
        # If both scores agree (close to each other), confidence is high
        difference = abs(structural - readiness)

        if difference < 0.15:
            return "High (Both dimensions agree)"
        elif difference < 0.30:
            return "Moderate (Some dimension disagreement)"
        else:
            return "Low (Dimensions disagree significantly)"

    def analyze(self, text: str) -> Dict:
        """
        Perform complete requirements readiness analysis.

        Args:
            text: Input text

        Returns:
            Dictionary with all analysis results
        """
        # Extract all features
        features = {
            'sentence_variation': self.analyze_sentence_length_variation(text),
            'ambiguity': self.analyze_ambiguity(text),
            'sao_pattern': self.analyze_subject_action_object(text)
        }

        # Extract raw metrics
        metrics = self.calculate_metrics(features)

        return {
            'features': features,
            'metrics': metrics
        }

    def print_report(self, results: Dict):
        """
        Print a formatted requirements readiness report.

        Args:
            results: Results from analyze()
        """
        print("=" * 80)
        print("REQUIREMENTS READINESS ANALYSIS REPORT")
        print("=" * 80)

        metrics = results['metrics']
        features = results['features']

        # Sentence Structure
        print("\n### SENTENCE STRUCTURE ###\n")
        print(f"   Sentence count:               {metrics['sentence_count']}")
        print(f"   Avg sentence length:          {metrics['avg_sentence_length']:.1f} words")
        print(f"   Std deviation:                {metrics['sentence_length_std_dev']:.1f} words")
        print(f"   Coefficient of variation:     {metrics['sentence_cv']:.3f}")

        # Ambiguity
        print("\n### AMBIGUITY ###\n")
        print(f"   Vague words:                  {metrics['vague_words_count']} ({metrics['vague_words_per_sentence']:.2f} per sentence)")
        amb = features['ambiguity']
        if amb['vague_words']['top_offenders']:
            print(f"   Top vague words:              {', '.join([f'{w}({c})' for w, c in amb['vague_words']['top_offenders'][:3]])}")
        print(f"   Anaphora (pronouns):          {metrics['anaphora_count']} ({metrics['anaphora_per_sentence']:.2f} per sentence)")
        if amb['anaphora']['top_offenders']:
            print(f"   Top anaphora:                 {', '.join([f'{w}({c})' for w, c in amb['anaphora']['top_offenders'][:3]])}")

        # SMAO Pattern
        print("\n### SMAO PATTERN ###\n")
        sao = features['sao_pattern']
        print(f"   Analysis method:              {sao.get('method', 'regex').upper()}")
        print(f"   SMAO sentences:               {metrics['smao_sentences_count']} ({metrics['smao_percentage']:.1f}%)")
        if 'patterns' in sao and sao['patterns']:
            print(f"   Example patterns:")
            for pattern in sao['patterns'][:3]:
                print(f"      {pattern}")
        if 'subject_consistency_percentage' in metrics:
            print(f"\n   Subject consistency:          {metrics.get('dominant_subject', 'N/A')} ({metrics['subject_consistency_percentage']:.1f}%)")

        print("\n" + "=" * 80)

    def print_recommendations(self, results: Dict):
        """Print recommendations for improvement based on raw metrics."""
        metrics = results['metrics']

        print("\n### RECOMMENDATIONS FOR IMPROVEMENT ###\n")

        recommendations = []

        # High sentence length variation
        if metrics['sentence_cv'] > 0.6:
            recommendations.append(
                f"• High sentence length variation (CV={metrics['sentence_cv']:.2f}): "
                "Aim for consistent 10-15 word sentences."
            )

        # High vague words
        if metrics['vague_words_per_sentence'] > 1.0:
            recommendations.append(
                f"• High vague word density ({metrics['vague_words_per_sentence']:.1f}/sentence): "
                "Eliminate words like 'easy', 'user-friendly', 'etc.'"
            )

        # High anaphora
        if metrics['anaphora_per_sentence'] > 1.0:
            recommendations.append(
                f"• High pronoun density ({metrics['anaphora_per_sentence']:.1f}/sentence): "
                "Replace 'it', 'this', 'they' with specific nouns."
            )

        # Low SMAO percentage
        if metrics['smao_percentage'] < 30:
            recommendations.append(
                f"• Low SMAO pattern usage ({metrics['smao_percentage']:.1f}%): "
                "Use 'The [system] shall [action] [object]' structure."
            )

        # Low subject consistency
        if 'subject_consistency_percentage' in metrics and metrics['subject_consistency_percentage'] < 60:
            recommendations.append(
                f"• Low subject consistency ({metrics['subject_consistency_percentage']:.1f}%): "
                f"Use '{metrics.get('dominant_subject', 'system')}' consistently across requirements."
            )

        if recommendations:
            for rec in recommendations:
                print(rec)
        else:
            print("No major issues detected.")

        print()


def main():
    """
    Main function to analyze the srs.md file.
    """
    # Initialize analyzer
    analyzer = RequirementsReadinessAnalyzer()

    # Read the file
    file_path = 'srs.md'

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        print(f"Analyzing file: {file_path}")
        print(f"File size: {len(text)} characters\n")

        # Perform analysis
        results = analyzer.analyze(text)

        # Print report
        analyzer.print_report(results)

        # Print recommendations
        analyzer.print_recommendations(results)

        # Save results to JSON
        try:
            output_file = 'requirements_readiness_results.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"Results also saved to: {output_file}")
        except Exception as e:
            print(f"\nNote: Could not save JSON results: {e}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("\nUsage: You can also use this as a module:")
        print("  from requirements_readiness_analyzer import RequirementsReadinessAnalyzer")
        print("  analyzer = RequirementsReadinessAnalyzer()")
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
