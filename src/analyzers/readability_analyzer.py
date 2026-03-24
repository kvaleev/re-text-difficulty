#!/usr/bin/env python3
"""
Automated Readability Index (ARI) and Multiple Readability Metrics Analyzer
Calculates various readability scores for text assessment.
"""

import re
import statistics
from typing import Dict, List
import json
import sys


class ReadabilityAnalyzer:
    """
    Analyzes text readability using multiple established metrics.
    """

    def __init__(self):
        """Initialize the analyzer."""
        pass

    def count_syllables(self, word: str) -> int:
        """
        Count syllables in a word using a heuristic approach.

        Args:
            word: Input word

        Returns:
            Estimated syllable count
        """
        word = word.lower()

        # Remove non-alphabetic characters
        word = re.sub(r'[^a-z]', '', word)

        if len(word) == 0:
            return 0

        # Count vowel groups
        vowels = "aeiouy"
        syllable_count = 0
        previous_was_vowel = False

        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel

        # Adjust for silent e
        if word.endswith('e'):
            syllable_count -= 1

        # Adjust for 'le' endings
        if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
            syllable_count += 1

        # Every word has at least one syllable
        if syllable_count == 0:
            syllable_count = 1

        return syllable_count

    def tokenize_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)

        # Split by sentence ending punctuation
        sentences = re.split(r'[.!?]+', text)

        # Clean and filter empty sentences
        sentences = [s.strip() for s in sentences if s.strip()]

        return sentences

    def tokenize_words(self, text: str) -> List[str]:
        """
        Split text into words.

        Args:
            text: Input text

        Returns:
            List of words
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        return words

    def count_characters(self, text: str) -> int:
        """
        Count alphanumeric characters (no spaces).

        Args:
            text: Input text

        Returns:
            Character count
        """
        return len(re.sub(r'[^a-zA-Z0-9]', '', text))

    def calculate_ari(self, text: str) -> Dict:
        """
        Calculate Automated Readability Index (ARI).

        Formula: ARI = 4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43

        Args:
            text: Input text

        Returns:
            Dictionary with ARI score and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)
        characters = self.count_characters(text)

        if len(sentences) == 0 or len(words) == 0:
            return {
                'score': 0,
                'grade_level': 0,
                'age_range': '5-6',
                'interpretation': 'Insufficient text'
            }

        # Calculate ARI
        chars_per_word = characters / len(words)
        words_per_sentence = len(words) / len(sentences)

        ari_score = 4.71 * chars_per_word + 0.5 * words_per_sentence - 21.43

        # Round to one decimal place
        ari_score = round(ari_score, 1)

        # Determine grade level and interpretation
        grade_level = round(ari_score)
        age_range = self._get_age_range(grade_level)
        interpretation = self._get_ari_interpretation(grade_level)

        return {
            'score': ari_score,
            'grade_level': max(1, grade_level),  # Minimum grade 1
            'age_range': age_range,
            'interpretation': interpretation,
            'details': {
                'characters': characters,
                'words': len(words),
                'sentences': len(sentences),
                'chars_per_word': round(chars_per_word, 2),
                'words_per_sentence': round(words_per_sentence, 2)
            }
        }

    def calculate_flesch_reading_ease(self, text: str) -> Dict:
        """
        Calculate Flesch Reading Ease score.

        Formula: 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)

        Score ranges from 0-100, higher is easier to read.

        Args:
            text: Input text

        Returns:
            Dictionary with score and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)

        if len(sentences) == 0 or len(words) == 0:
            return {'score': 0, 'interpretation': 'Insufficient text'}

        # Count syllables
        total_syllables = sum(self.count_syllables(word) for word in words)

        # Calculate Flesch Reading Ease
        words_per_sentence = len(words) / len(sentences)
        syllables_per_word = total_syllables / len(words)

        score = 206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word
        score = round(score, 1)

        interpretation = self._get_flesch_interpretation(score)

        return {
            'score': score,
            'interpretation': interpretation,
            'details': {
                'total_syllables': total_syllables,
                'syllables_per_word': round(syllables_per_word, 2),
                'words_per_sentence': round(words_per_sentence, 2)
            }
        }

    def calculate_flesch_kincaid_grade(self, text: str) -> Dict:
        """
        Calculate Flesch-Kincaid Grade Level.

        Formula: 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59

        Args:
            text: Input text

        Returns:
            Dictionary with grade level and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)

        if len(sentences) == 0 or len(words) == 0:
            return {'grade_level': 0, 'interpretation': 'Insufficient text'}

        # Count syllables
        total_syllables = sum(self.count_syllables(word) for word in words)

        # Calculate Flesch-Kincaid Grade Level
        words_per_sentence = len(words) / len(sentences)
        syllables_per_word = total_syllables / len(words)

        grade = 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59
        grade = round(grade, 1)

        # Ensure minimum grade of 0
        grade = max(0, grade)

        interpretation = self._get_grade_interpretation(grade)

        return {
            'grade_level': grade,
            'interpretation': interpretation,
            'age_range': self._get_age_range(int(round(grade)))
        }

    def calculate_gunning_fog(self, text: str) -> Dict:
        """
        Calculate Gunning Fog Index.

        Formula: 0.4 * [(words/sentences) + 100 * (complex_words/words)]
        Complex words = words with 3+ syllables

        Args:
            text: Input text

        Returns:
            Dictionary with fog index and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)

        if len(sentences) == 0 or len(words) == 0:
            return {'score': 0, 'interpretation': 'Insufficient text'}

        # Count complex words (3+ syllables)
        complex_words = [w for w in words if self.count_syllables(w) >= 3]

        # Calculate Gunning Fog
        words_per_sentence = len(words) / len(sentences)
        complex_word_percentage = len(complex_words) / len(words)

        fog_index = 0.4 * (words_per_sentence + 100 * complex_word_percentage)
        fog_index = round(fog_index, 1)

        interpretation = self._get_grade_interpretation(fog_index)

        return {
            'score': fog_index,
            'grade_level': int(round(fog_index)),
            'interpretation': interpretation,
            'details': {
                'complex_words': len(complex_words),
                'complex_word_percentage': round(complex_word_percentage * 100, 2)
            }
        }

    def calculate_smog_index(self, text: str) -> Dict:
        """
        Calculate SMOG (Simple Measure of Gobbledygook) Index.

        Formula: 1.0430 * sqrt(polysyllables * 30/sentences) + 3.1291
        Polysyllables = words with 3+ syllables

        Args:
            text: Input text

        Returns:
            Dictionary with SMOG index and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)

        if len(sentences) < 30:
            # SMOG requires at least 30 sentences for accuracy
            # We'll calculate anyway but note the limitation
            pass

        if len(sentences) == 0 or len(words) == 0:
            return {'score': 0, 'interpretation': 'Insufficient text'}

        # Count polysyllables (3+ syllables)
        polysyllables = [w for w in words if self.count_syllables(w) >= 3]

        # Calculate SMOG
        import math
        smog = 1.0430 * math.sqrt(len(polysyllables) * 30 / len(sentences)) + 3.1291
        smog = round(smog, 1)

        interpretation = self._get_grade_interpretation(smog)

        return {
            'score': smog,
            'grade_level': int(round(smog)),
            'interpretation': interpretation,
            'details': {
                'polysyllables': len(polysyllables),
                'sentences_analyzed': len(sentences)
            },
            'note': 'SMOG is most accurate with 30+ sentences' if len(sentences) < 30 else None
        }

    def calculate_coleman_liau(self, text: str) -> Dict:
        """
        Calculate Coleman-Liau Index.

        Formula: 0.0588 * L - 0.296 * S - 15.8
        L = average number of letters per 100 words
        S = average number of sentences per 100 words

        Args:
            text: Input text

        Returns:
            Dictionary with index and interpretation
        """
        sentences = self.tokenize_sentences(text)
        words = self.tokenize_words(text)

        if len(sentences) == 0 or len(words) == 0:
            return {'score': 0, 'interpretation': 'Insufficient text'}

        # Count letters (characters in words)
        letters = sum(len(word) for word in words)

        # Calculate per 100 words
        L = (letters / len(words)) * 100
        S = (len(sentences) / len(words)) * 100

        # Calculate Coleman-Liau
        cli = 0.0588 * L - 0.296 * S - 15.8
        cli = round(cli, 1)

        interpretation = self._get_grade_interpretation(cli)

        return {
            'score': cli,
            'grade_level': int(round(cli)),
            'interpretation': interpretation,
            'details': {
                'letters_per_100_words': round(L, 2),
                'sentences_per_100_words': round(S, 2)
            }
        }

    def _get_age_range(self, grade: int) -> str:
        """Get age range for a grade level."""
        age_map = {
            1: '6-7', 2: '7-8', 3: '8-9', 4: '9-10', 5: '10-11',
            6: '11-12', 7: '12-13', 8: '13-14', 9: '14-15', 10: '15-16',
            11: '16-17', 12: '17-18', 13: '18-22', 14: '22+'
        }
        return age_map.get(min(grade, 14), '22+')

    def _get_ari_interpretation(self, grade: int) -> str:
        """Get interpretation for ARI grade level."""
        if grade <= 1:
            return 'Kindergarten'
        elif grade <= 6:
            return 'Elementary School'
        elif grade <= 8:
            return 'Middle School'
        elif grade <= 12:
            return 'High School'
        elif grade <= 16:
            return 'College'
        else:
            return 'Advanced/Professional'

    def _get_flesch_interpretation(self, score: float) -> str:
        """Get interpretation for Flesch Reading Ease score."""
        if score >= 90:
            return 'Very Easy (5th grade)'
        elif score >= 80:
            return 'Easy (6th grade)'
        elif score >= 70:
            return 'Fairly Easy (7th grade)'
        elif score >= 60:
            return 'Standard (8th-9th grade)'
        elif score >= 50:
            return 'Fairly Difficult (10th-12th grade)'
        elif score >= 30:
            return 'Difficult (College)'
        else:
            return 'Very Difficult (College Graduate)'

    def _get_grade_interpretation(self, grade: float) -> str:
        """Get general interpretation for grade level."""
        grade_int = int(round(grade))
        if grade_int <= 6:
            return 'Elementary School'
        elif grade_int <= 8:
            return 'Middle School'
        elif grade_int <= 12:
            return 'High School'
        elif grade_int <= 16:
            return 'College'
        else:
            return 'Advanced/Professional'

    def analyze(self, text: str) -> Dict:
        """
        Perform complete readability analysis.

        Args:
            text: Input text

        Returns:
            Dictionary containing all readability metrics
        """
        return {
            'ari': self.calculate_ari(text),
            'flesch_reading_ease': self.calculate_flesch_reading_ease(text),
            'flesch_kincaid_grade': self.calculate_flesch_kincaid_grade(text),
            'gunning_fog': self.calculate_gunning_fog(text),
            'smog_index': self.calculate_smog_index(text),
            'coleman_liau': self.calculate_coleman_liau(text)
        }

    def print_report(self, results: Dict):
        """
        Print a formatted readability report.

        Args:
            results: Results from analyze()
        """
        print("=" * 70)
        print("READABILITY ANALYSIS REPORT")
        print("=" * 70)

        # ARI
        print("\n### AUTOMATED READABILITY INDEX (ARI) ###\n")
        ari = results['ari']
        print(f"  ARI Score:                    {ari['score']}")
        print(f"  Grade Level:                  {ari['grade_level']}")
        print(f"  Age Range:                    {ari['age_range']} years")
        print(f"  Interpretation:               {ari['interpretation']}")
        print(f"\n  Text Statistics:")
        print(f"    Characters:                 {ari['details']['characters']}")
        print(f"    Words:                      {ari['details']['words']}")
        print(f"    Sentences:                  {ari['details']['sentences']}")
        print(f"    Chars per Word:             {ari['details']['chars_per_word']}")
        print(f"    Words per Sentence:         {ari['details']['words_per_sentence']}")

        # Flesch Reading Ease
        print("\n### FLESCH READING EASE ###\n")
        fre = results['flesch_reading_ease']
        print(f"  Score:                        {fre['score']}")
        print(f"  Interpretation:               {fre['interpretation']}")
        print(f"  Syllables per Word:           {fre['details']['syllables_per_word']}")

        # Flesch-Kincaid Grade Level
        print("\n### FLESCH-KINCAID GRADE LEVEL ###\n")
        fkg = results['flesch_kincaid_grade']
        print(f"  Grade Level:                  {fkg['grade_level']}")
        print(f"  Age Range:                    {fkg['age_range']} years")
        print(f"  Interpretation:               {fkg['interpretation']}")

        # Gunning Fog
        print("\n### GUNNING FOG INDEX ###\n")
        fog = results['gunning_fog']
        print(f"  Fog Index:                    {fog['score']}")
        print(f"  Grade Level:                  {fog['grade_level']}")
        print(f"  Interpretation:               {fog['interpretation']}")
        print(f"  Complex Words (3+ syllables): {fog['details']['complex_words']} ({fog['details']['complex_word_percentage']}%)")

        # SMOG
        print("\n### SMOG INDEX ###\n")
        smog = results['smog_index']
        print(f"  SMOG Score:                   {smog['score']}")
        print(f"  Grade Level:                  {smog['grade_level']}")
        print(f"  Interpretation:               {smog['interpretation']}")
        print(f"  Polysyllables:                {smog['details']['polysyllables']}")
        if smog.get('note'):
            print(f"  Note: {smog['note']}")

        # Coleman-Liau
        print("\n### COLEMAN-LIAU INDEX ###\n")
        cli = results['coleman_liau']
        print(f"  CLI Score:                    {cli['score']}")
        print(f"  Grade Level:                  {cli['grade_level']}")
        print(f"  Interpretation:               {cli['interpretation']}")

        # Summary
        print("\n### SUMMARY ###\n")
        grades = [
            ari['grade_level'],
            fkg['grade_level'],
            fog['grade_level'],
            smog['grade_level'],
            cli['grade_level']
        ]
        avg_grade = round(statistics.mean(grades), 1)
        consensus_interpretation = self._get_grade_interpretation(avg_grade)

        print(f"  Average Grade Level:          {avg_grade}")
        print(f"  Consensus Interpretation:     {consensus_interpretation}")
        print(f"  Recommended Audience:         {self._get_age_range(int(round(avg_grade)))} years")

        print("\n" + "=" * 70)


def main():
    """
    Main function to analyze the srs.md file.
    """
    # Initialize analyzer
    analyzer = ReadabilityAnalyzer()

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

        # Save results to JSON
        try:
            output_file = 'readability_results.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults also saved to: {output_file}")
        except Exception as e:
            print(f"\nNote: Could not save JSON results: {e}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("\nUsage: You can also use this as a module:")
        print("  from readability_analyzer import ReadabilityAnalyzer")
        print("  analyzer = ReadabilityAnalyzer()")
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
