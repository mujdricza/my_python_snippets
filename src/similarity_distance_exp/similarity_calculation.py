"""
Trying out some similarity/distance metrics in https://rapidfuzz.github.io/Levenshtein/,
and inspect the effects of specific properties of the tokens to be compared,
e.g. length of the tokens, amount and place of differences in the tokens.

"""
import os
import sys

import Levenshtein
import pandas as pd

from fuzzy_matcher import fuzzy_match
from src.general_utils.io_utils import write_excel_with_sheets


EXP_LISTE = [
    "a",
    "b",
    "ab",
    "cb",
    "abc",
    "abcd",
    "abcde",
    "cdeabc",
    "abcabcabc",
    "abcabcabb",
    "abcaacabc",
    "abcabcabcabcabc",
    "abcabcabcabcabb",
    "abcabcabcabcabca",
    "abcabcabcabcabcabc",
    "abcabcabcabcabcabcd",
]

def exp():

    records = []

    for s1 in EXP_LISTE:
        for s2 in EXP_LISTE:
            r_distance = Levenshtein.distance(s1, s2)
            r_ratio = Levenshtein.ratio(s1, s2)
            r_jaro = Levenshtein.jaro(s1, s2)
            r_opcodes = Levenshtein.opcodes(s1, s2)

            similarity_score, is_similar, is_short_distance_similar, is_utt_score_similar, is_utt_distance_similar = fuzzy_match(s1, s2)

            record = {
                "s1": s1,
                "s2": s2,
                "r_dist": r_distance,
                "r_rat": r_ratio,
                "r_jaro": r_jaro,
                "sim_score": similarity_score,
                "is_sim": is_similar,
                "is_sh_dsim": is_short_distance_similar,
                "is_utt_sim": is_utt_score_similar,
                "is_utt_dsim": is_utt_distance_similar,
                "r_ops": r_opcodes,
            }
            records.append(record)

    return records


def main(out_path: str):
    records = exp()
    dfs = {"similarity exp": pd.DataFrame.from_records(records)}
    write_excel_with_sheets(dfs, out_path, write_index=True)

if __name__ == "__main__":
    output_path = os.path.abspath(sys.argv[1])
    main(output_path)
