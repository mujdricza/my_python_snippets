"""

Original copied from tv_nlu/internal_nlu/fuzzy_matcher.py and tv_nlu/internal_nlu/utils.py

Fuzzy-matching based NLU resolvers.
Fuzzy-matching is applied according to string-similarity algorithm in https://rapidfuzz.github.io/Levenshtein/
with heuristically set thresholds.
"""

import logging
import re
from time import perf_counter
from types import MappingProxyType
from typing import Any, Dict, List, Tuple

# from cvp.reporting import new_span
from Levenshtein import distance
from rapidfuzz import process, fuzz

# from tv_nlu import reporting
# from tv_nlu.internal_nlu import (
#     DEFAULT_FUZZY_ENTITY_INTENT_MAPPING,
#     DEFAULT_FUZZY_PATTERNS,
#     FALLBACK_FUZZY_PATTERNS,
#     FUZZY_MAPPING_ENTITIES_DICTIONARY,
# )
# from tv_nlu.internal_nlu.models.cvp_entity import (
from src.general_utils.external.tv_nlu.internal_nlu.models.cvp_entity import (
    EntityIndices,
    CvpEntity,
)
# from tv_nlu.internal_nlu.placeholder_utterance import (
#     placeholder_utterance,
#     update_literal,
# )
# from tv_nlu.internal_nlu.regex_models.models import Regex
# from tv_nlu.internal_nlu.simple_regex_model import run_regex_model
# from tv_nlu.internal_nlu.utils import linear_values
# from tv_nlu.reporting import NluComponent, InternalNluComponentReport


logger = logging.getLogger(__name__)


_THRESHOLD_HIGH = 80
_THRESHOLD_LOW = 78
_THRESHOLD_STEP_SIZE = -0.1




def __linear_values(
    first_value: float, second_value: float, step_size: float
) -> Tuple[float, ...]:
    value_list = [first_value]
    counter = 0
    if step_size < 0 and first_value > second_value:
        while value_list[-1] > second_value:
            value_list.append(round(value_list[-1] + step_size, 3))
            counter += 1
            if counter > 200:
                break
    elif step_size > 0 and second_value > first_value:
        while value_list[-1] < second_value:
            value_list.append(round(value_list[-1] + step_size, 3))
            counter += 1
            if counter > 200:
                break
    else:
        return tuple()
    return tuple(value_list)

DEFAULT_FUZZY_THRESHOLD_VALUES: Tuple[float, ...] = __linear_values(
    _THRESHOLD_HIGH, _THRESHOLD_LOW, _THRESHOLD_STEP_SIZE
)
# print(f"{DEFAULT_FUZZY_THRESHOLD_VALUES=}")
# DEFAULT_FUZZY_THRESHOLD_VALUES=(80, 79.9, 79.8, 79.7, 79.6, 79.5, 79.4, 79.3, 79.2, 79.1, 79.0, 78.9, 78.8, 78.7, 78.6, 78.5, 78.4, 78.3, 78.2, 78.1, 78.0)

def _is_utterance_matching(
    utterance: str,
    dynamic_threshold_values: Tuple[float, ...],
    best_match_score: float,
) -> bool:
    if len(utterance) >= len(dynamic_threshold_values):
        return best_match_score > dynamic_threshold_values[-1]
    else:
        return best_match_score > dynamic_threshold_values[len(utterance)]


def _is_utterance_close(utterance: str, entity_literal: str) -> bool:
    current_distance = distance(utterance, entity_literal)
    if len(utterance) < 7:
        return False
    elif len(utterance) < 12 and current_distance > 2:
        return False
    elif len(utterance) >= 12 and len(utterance) < 20 and current_distance > 3:
        return False
    elif len(utterance) >= 20 and len(utterance) < 28 and current_distance > 5:
        return False
    else:
        return True


def _is_small_utterance_close(utterance: str, entity_literal: str) -> bool:
    current_distance = distance(utterance, entity_literal)
    if len(utterance) <= 7 and current_distance <= 1:
        return True
    elif len(utterance) > 7 and len(utterance) < 12 and current_distance <= 2:
        return True
    else:
        return False


def _is_channel_similar(
    match_phrase_in_utterance: str,
    best_matching_entity: CvpEntity,
    best_match_score: float,
) -> bool:
    return (
        best_matching_entity.name == "channel"
        and best_match_score >= 80
        and _is_small_utterance_close(
            match_phrase_in_utterance.lower(), best_matching_entity.literal.lower()
        )
    )


def _is_general_similar(
    match_phrase_in_utterance: str,
    best_matching_entity: CvpEntity,
    best_match_score: float,
    dynamic_threshold_values: Tuple[float, ...],
):

    return _is_utterance_matching(
        match_phrase_in_utterance.lower(), dynamic_threshold_values, best_match_score
    ) and _is_utterance_close(
        match_phrase_in_utterance.lower(), best_matching_entity.literal.lower()
    )


def _is_match_phrase_similar_to_found_entity_candidate(
    match_phrase_in_utterance: str,
    best_matching_entity: CvpEntity,
    best_match_score: float,
    dynamic_threshold_values: Tuple[float, ...],
) -> bool:

    is_similar = _is_channel_similar(
        match_phrase_in_utterance, best_matching_entity, best_match_score
    )
    if not is_similar:
        is_similar = _is_general_similar(
            match_phrase_in_utterance,
            best_matching_entity,
            best_match_score,
            dynamic_threshold_values,
        )
    return is_similar


def _get_placeholdered_entity_categories(literal: str) -> List[re.Match]:
    placeholdered_categories = re.finditer("\\{[^}]+\\}", literal)
    return list(placeholdered_categories)


def _get_fitting_replacement_item(
    replacement_list: List[Tuple[CvpEntity, str]], matched_category: str
) -> Tuple[Tuple[CvpEntity, str] | None, List[Tuple[CvpEntity, str]]]:

    last_idx = None
    last_item = None
    replacement_list = sorted(replacement_list, key=lambda x: x[0].startIndex)
    idx_list = zip(range(len(replacement_list)), replacement_list)
    for idx, replaced_entity_and_category in sorted(
        idx_list, key=lambda x: x[0], reverse=True
    ):
        _, replaced_category = replaced_entity_and_category
        if replaced_category == matched_category:
            last_idx = idx
            break
    if last_idx is not None:
        last_item = replacement_list[last_idx]
        replacement_list = replacement_list[:last_idx]
    return last_item, replacement_list


# def _reconstruct_placeholdered_entity_content(
#     utterance: str,
#     placeholdered_utterance: str,
#     entity: CvpEntity,
#     replacement_list: List[Tuple[CvpEntity, str]],
# ) -> CvpEntity:
#     """Reconstruct the entity literal and value, if the placeholdered utterance was base for a regex-match,
#     and thus, the entity contains placeholdered literal and value.
#
#     E.g. for the utterance 'Suche mir den Film in dem Luke Sky Walker seine Hande verliert'
#     there is an entity with placeholders:
#     CvpEntity(name='tv_keyword', literal='den Film in dem Luke {app} {title} seine Hande verliert', value='den Film in dem Luke {app} {title} seine Hande verliert', positions=EntityIndices(startIndex=10, endIndex=64))
#     --> after re-creation of the original:
#     CvpEntity(name='tv_keyword', literal='den Film in dem Luke Sky Walker seine Hande verliert', value='den Film in dem Luke Sky Walker seine Hande verliert', positions=EntityIndices(startIndex=10, endIndex=61))
#
#     :param placeholdered_utterance: utterance with entity placeholders
#     :param entity: the entity found according to the placeholdered_utterance;
#     thus, the literal value might contain entity placeholders
#     :param replacement_list: replacements during placeholdering the utterance
#     :return: the entity with the original entity literal instead of the one
#     containing entity placeholders
#     """
#     # search for the entity part in the original utterance, and pad it for easier matching
#     placeholdered_literal = entity.literal
#     padded_placeholdered_literal = placeholdered_literal
#     literal_match = re.search(re.escape(placeholdered_literal), placeholdered_utterance)
#     if literal_match is not None:
#         literal_start = literal_match.start()
#         padded_placeholdered_literal = "_" * literal_start + placeholdered_literal
#     category_matches = _get_placeholdered_entity_categories(
#         padded_placeholdered_literal
#     )
#     if not category_matches:  # no placeholdered part in the entity
#         return entity
#
#     # replace the placeholders to original literals
#     padded_original_literal = padded_placeholdered_literal
#     for category_match in sorted(
#         category_matches, key=lambda x: x.start(), reverse=True
#     ):
#         placeholdered_start_index = category_match.start()
#         placeholdered_end_index = category_match.end()
#         matched_category = padded_original_literal[
#             placeholdered_start_index:placeholdered_end_index
#         ].strip("{}")
#         replaced_entity_and_category, replacement_list = _get_fitting_replacement_item(
#             replacement_list, matched_category
#         )
#         if replaced_entity_and_category is None:
#             continue  # not expected
#         replaced_entity, _ = replaced_entity_and_category
#         padded_original_literal = update_literal(
#             padded_original_literal,
#             placeholdered_start_index,
#             placeholdered_end_index - 1,
#             replaced_entity.literal,
#         )
#
#     original_literal = padded_original_literal.lstrip("_")
#     if (
#         original_literal not in utterance
#     ):  # something went wrong -> return original entity
#         return entity
#     # set the re-created original literal as literal value to the entity
#     original_entity = CvpEntity(
#         name=entity.name,
#         literal=original_literal,
#         value=original_literal,
#         positions=EntityIndices(
#             startIndex=entity.startIndex,
#             endIndex=entity.startIndex + len(original_literal) - 1,
#         ),
#     )
#     return original_entity


# def _apply_category_candidate(
#     entity_category_candidate: str,
#     fuzzy_entity_intent_mapping: MappingProxyType[str, Dict[str, Any]],
#     whole_utterance_match: bool,
# ) -> bool:
#     """Restrict the application of the found entity category candidate according to the defined attribute in the Fuzzy entity-intent mapping.
#
#     :param entity_category_candidate: the found entity category candidate
#     :param fuzzy_entity_intent_mapping: mapping of entity category to intent
#     :param whole_utterance_match: whether the current candidate was found on the whole utterance
#     :return: True if the category candidate is not restricted to a whole utterance match, or the
#     category is applicable to a partial utterance match; False if the category candidate is restricted
#     to a whole utterance match, but the current match is only covering a part of the utterance
#     """
#     only_for_whole_utterance = fuzzy_entity_intent_mapping[entity_category_candidate][
#         "only_whole_utterance"
#     ]
#     if only_for_whole_utterance and not whole_utterance_match:
#         return False
#     return True


def fuzzy_match(
    utterance: str,
    candidate: str,  # ! added for the experiment
    # entity_list: List[CvpEntity],
    # fuzzy_patterns: Tuple[Regex, ...] = DEFAULT_FUZZY_PATTERNS,
    # fuzzy_entity_mappings: MappingProxyType[
    #     str, Dict[str, str]
    # ] = FUZZY_MAPPING_ENTITIES_DICTIONARY,
    # fuzzy_entity_intent_mapping: MappingProxyType[
    #     str, Dict[str, Any]
    # ] = DEFAULT_FUZZY_ENTITY_INTENT_MAPPING,
    # lowercase_utterance: bool = False,  # for placeholdering the utterance
    # restrict_to_similar: bool = True,
    dynamic_threshold_values: Tuple[float, ...] = DEFAULT_FUZZY_THRESHOLD_VALUES,
) -> Tuple[float, bool, float, float, float]:
# ) -> Tuple[str | None, CvpEntity | None]:
    """Try to find an appropriate intent and entity for an entity literal in
     the given utterance, where the assumption is that this literal value is
     a variant of a defined listed entity.
     E.g. "Roberde Niro" instead of "Robert De Niro" for entity "person"

     If the entity is similar enough to defined entity values according to some
     heuristics using the Ratcliff-Obershelp algorithm, the entity value
     with the highest similarity score will be taken as entity.

     Note that only a given number of entity types
     (defined in fuzzy_entity_intent_mapping) are considered here.

    :param utterance: input utterance
    :param entity_list: detected entities upto now
    :param fuzzy_patterns: patterns for fuzzy-match; typically,
    these patterns contain a tv_keyword entity (according to current design)
    :param fuzzy_entity_mappings: entity literals to category mappings
    :param fuzzy_entity_intent_mapping:  the considered entity types with the
    associated intent names
    :param lowercase_utterance: whether fuzzy patterns will be applied
    to lowercased utterance (for placeholdering the utterance)
    :param restrict_to_similar: whether the found tv_keyword should be restricted
    to a similar entity value defined in our entity lists
    :param dynamic threshold values: thresholds for computing similarity between
    the entity candidate and the defined entity literal values
    :return: intent and entity if any found; default value is None for both
    """

    # if not utterance:  # not typical case, but to be handled
    #     return None, None
    #
    # # search for better match_phrase
    # placeholdered_utterance, replacements = placeholder_utterance(
    #     utterance,
    #     entity_list,
    #     tuple(fuzzy_entity_intent_mapping.keys()),
    #     lowercase_utterance,
    # )
    # intent, entities = run_regex_model(
    #     placeholdered_utterance, entity_list, fuzzy_patterns
    # )
    # entities = [
    #     _reconstruct_placeholdered_entity_content(
    #         utterance, placeholdered_utterance, entity, replacements
    #     )
    #     for entity in entities
    # ]
    # if not intent:
    #     # t.i., none of the simple regexes are matching, search without the patterns again
    #     intent, entities = run_regex_model(utterance, entity_list, fuzzy_patterns)
    #
    # entity_category = (
    #     "title"  # tv_keyword entity will be interpreted as title per default
    # )
    # match_phrase = None
    # start_index = 0
    # end_index = 0
    # whole_utterance_match = False
    # if intent and entities:
    #     # the current design is that there is only one tv_keyword entity in the fuzzy-patterns
    #     tv_keyword_entity = entities[0]
    #     match_phrase = tv_keyword_entity.literal
    #     start_index = tv_keyword_entity.startIndex
    #     end_index = tv_keyword_entity.endIndex
    # elif restrict_to_similar:
    #     # get content of the potential entity with the utterance as default for the restricted case only
    #     whole_utterance_match = True
    #     match_phrase = utterance
    #     start_index = 0
    #     end_index = len(utterance) - 1  # NOTE inclusive endIndex

    # if match_phrase:
    # for similarity computation, search for the best-scored defined entity candidate
    # candidates = list(fuzzy_entity_mappings.keys())

    # Process.extractOne finds the best candidate using the scorer, here using fuzz.ratio.
    # Should be more optimized than a for loop.
    best_synonym, best_match_score, _ = process.extractOne(# type: ignore
        utterance.lower(), [candidate], scorer=fuzz.ratio
        # match_phrase.lower(), candidates, scorer=fuzz.ratio
    )
    # best_cat2can = fuzzy_entity_mappings.get(best_synonym, {})

    # entity_category_candidate, entity_value_candidate = list(best_cat2can.items())[
    #     0
    # ]  # only one entry there
    # # here, we have to make a difference between the case where the whole utterance can be an entity
    # # and the case where the tv_keyword entity is just a part of the utterance
    # # NOTE eliminate this distinction!
    # if restrict_to_similar or _apply_category_candidate(
    #     entity_category_candidate,
    #     fuzzy_entity_intent_mapping,
    #     whole_utterance_match,
    # ):
    #     entity_category = entity_category_candidate
    #     if entity_category == "title":  # for title, be more restrictive
    #         if best_match_score > _THRESHOLD_HIGH:
    #             entity_value = entity_value_candidate
    #         else:
    #             entity_value = match_phrase
    #     else:
    #         entity_value = entity_value_candidate
    # else:
    #     entity_value = match_phrase

    entity = CvpEntity(
        name="entity",
        value=best_synonym,
        literal=best_synonym,
        positions=EntityIndices(startIndex=0, endIndex=0),
    )

    # # now, get associated intent even if already given according to the detected entity category
    # int_ent_mapping: Dict[str, Any] | None = fuzzy_entity_intent_mapping.get(
    #     entity_category
    # )
    # intent = int_ent_mapping.get("intent") if int_ent_mapping else None
    is_similar = _is_match_phrase_similar_to_found_entity_candidate(
        utterance, entity, best_match_score, dynamic_threshold_values
        # match_phrase, entity, best_match_score, dynamic_threshold_values
    )
    # if restrict_to_similar and not is_similar:
    #     return None, None

    is_short_distance_similar = _is_small_utterance_close(utterance, best_synonym)
    is_utt_score_similar = _is_utterance_matching(utterance, dynamic_threshold_values,best_match_score)
    is_utt_distance_similar = _is_utterance_close(utterance, best_synonym)
    return best_match_score, is_similar, is_short_distance_similar, is_utt_score_similar, is_utt_distance_similar
    # return intent, entity
    # return None, None


# @new_span(NluComponent.INLU_FUZZY_MATCH)
def run_fuzzy_match(
    utterance: str,
    entity_list: List[CvpEntity],
) -> Tuple[str | None, CvpEntity | None]:
    # Invoke and measure
    start = perf_counter()
    intent, entity = fuzzy_match(utterance, entity_list)
    if intent and entity:
        logger.debug("Fuzzy matcher found an intent: %s; entity: %s", intent, entity)
    else:
        logger.debug("Fuzzy matcher did not find an intent or entity")
    duration = perf_counter() - start

    # Report
    # fuzzy_entities = [entity] if entity is not None else []
    # report = InternalNluComponentReport(
    #     NluComponent.INLU_FUZZY_MATCH, intent, fuzzy_entities, duration
    # )
    # reporting.add_report(report)

    return intent, entity


# @new_span(NluComponent.INLU_FALLBACK_FUZZY_MATCH)
# def run_fallback_fuzzy_match(
#     utterance: str,
#     entity_list: List[CvpEntity],
# ) -> Tuple[str | None, CvpEntity | None]:
#     # Invoke and measure
#     start = perf_counter()
#     intent, entity = fuzzy_match(
#         utterance,
#         entity_list,
#         fuzzy_patterns=FALLBACK_FUZZY_PATTERNS,
#         restrict_to_similar=False,
#     )
#     if intent and entity:
#         logger.debug(
#             "Fallback Fuzzy matcher found an intent: %s; entity: %s", intent, entity
#         )
#     else:
#         logger.debug("Fallback Fuzzy matcher did not find an intent or entity")
#     duration = perf_counter() - start
#
#     # Report
#     fuzzy_entities = [entity] if entity is not None else []
#     report = InternalNluComponentReport(
#         NluComponent.INLU_FUZZY_MATCH, intent, fuzzy_entities, duration
#     )
#     reporting.add_report(report)
#
#     return intent, entity
