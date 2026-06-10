from pydantic import BaseModel, ConfigDict, TypeAdapter
from typing import List

from src.misc.pydantic_exp.pydantic_exp1 import EntityIndices

def exp1():
    ei1 = EntityIndices(startIndex=1, endIndex=2)
    print(ei1.__fields__)  # {'startIndex': FieldInfo(annotation=int, required=True), 'endIndex': FieldInfo(annotation=int, required=True)}
    print(ei1.__fields__.keys())  # dict_keys(['startIndex', 'endIndex'])



class Regex(BaseModel):
    name: str
    patterns: List[str]

    @property
    def name_key(self):
        return "name"

    @property
    def patterns_key(self):
        return "patterns"


def exp2():

    r = Regex(name="abc", patterns=["abc"])

    print(r.name)
    # print(r.name_key())
    print(r.name_key)
    print(r.patterns_key)
    print(r.model_dump())

    regexes = [
        {"name": "abc", "patterns": ["abc"]},
        {"name": "def", "patterns": ["def"]},
    ]
    validated_regexes = TypeAdapter(List[Regex]).validate_python(regexes)
    print(validated_regexes)  # [Regex(name='abc', patterns=['abc']), Regex(name='def', patterns=['def'])]

    """
    abc
    name
    patterns
    {'name': 'abc', 'patterns': ['abc']}
    [Regex(name='abc', patterns=['abc']), Regex(name='def', patterns=['def'])]
    """

if __name__ == "__main__":
    # exp1()
    exp2()