"""
Text Analysis Utilities Package
Contains all individual analyzer modules
"""

from .readability_analyzer import ReadabilityAnalyzer
from .structure_analyzer import StructureAnalyzer
from .requirements_readiness_analyzer import RequirementsReadinessAnalyzer
from .cpre_glossary_analyzer import CPREGlossaryAnalyzer

# TRUNAJOD Entity Coherence is optional (requires python3.9, TRUNAJOD, spaCy)
try:
    from .entity_coherence_analyzer import EntityCoherenceAnalyzer
    ENTITY_COHERENCE_AVAILABLE = True
except ImportError:
    EntityCoherenceAnalyzer = None
    ENTITY_COHERENCE_AVAILABLE = False

__all__ = [
    'ReadabilityAnalyzer',
    'StructureAnalyzer',
    'RequirementsReadinessAnalyzer',
    'CPREGlossaryAnalyzer',
    'EntityCoherenceAnalyzer',
    'ENTITY_COHERENCE_AVAILABLE'
]
