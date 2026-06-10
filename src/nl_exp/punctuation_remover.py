import re
import sys
from typing import Dict, List

from src.general_utils.io_utils import read_text_lines, write_text


# string.punctuation
PUNCTUATION_CHARS_STRING_MODULE = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
PUNCTUATION_CHARS = "!\",-.:;?`'"

# key: input, value: expected output
CASES = {
    "No. No.": "No No",
    "The temperature in the O'Reilly & Arbuthnot-Smythe server's main rack is 40.5 degrees at 18:00 - don't you know? No.": "The temperature in the O'Reilly & Arbuthnot-Smythe server's main rack is 40.5 degrees at 18:00 don't you know No",
    "'abc' said, he - 'not a matter'.": "abc said he not a matter",
}


PATTERNS = [
    re.compile("(?P<to_be_removed>[!?.,:;]+)(\s|$)"),
    re.compile("(?P<to_be_removed>['`\"])(\s|$)"),
    re.compile("(\s|^)(?P<to_be_removed>['`\"])"),
    re.compile("(?P<to_be_removed>\s-)\s"),
]


def remove_punctuation(text: str, pattern_list: List[re.Pattern]) -> str:
    result = text.strip()
    for pattern in pattern_list:
        founds = pattern.finditer(result)
        for found in sorted(founds, key=lambda x: x.span(), reverse=True):
            idx_start, idx_end = found.span("to_be_removed")
            result = result[:idx_start] + result[idx_end:]
    return result


def main_exp(cases: Dict[str, str], pattern_list: List[re.Pattern]) -> None:

    for case_orig, case_res in cases.items():
        result = case_orig
        for pattern in pattern_list:
            founds = pattern.finditer(result)
            for found in sorted(founds, key=lambda x: x.span(), reverse=True):
                idx_start, idx_end = found.span("to_be_removed")
                result = result[:idx_start] + result[idx_end:]
        print(f"{case_orig} -> {result} == {case_res == result}")


def main(input_path: str, patterns: List[str], output_path: str) -> None:
    utterances = read_text_lines(input_path)
    print(f"Read {len(utterances)} utterances from '{input_path}'")
    utterances_wo_punctuation = []
    for utterance in utterances:
        utt_wo_punct = remove_punctuation(utterance, patterns)
        utterances_wo_punctuation.append(utt_wo_punct)
    print(f"Writing {len(utterances_wo_punctuation)} utterances to '{output_path}'")
    write_text(utterances_wo_punctuation, output_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        main(sys.argv[1], PATTERNS, sys.argv[2])
    else:
        main_exp(CASES, PATTERNS)
