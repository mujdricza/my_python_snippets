from pydantic import BaseModel, ConfigDict
from typing import Tuple


class EntityIndices(BaseModel):
    startIndex: int
    endIndex: int
    model_config = ConfigDict(frozen=False, validate_assignment=True, extra="allow")

    def indices(self) -> Tuple[int, int]:
        return self.startIndex, self.endIndex

    def __eq__(self, other: "EntityIndices") -> bool:
        if other is None:
            return False
        if not isinstance(other, EntityIndices):
            return False
        return self.indices() == other.indices()

    def __hash__(self) -> int:
        return hash((self.startIndex, self.endIndex))

    def __str__(self):
        return (
            "EntityIndices(startIndex=%s, endIndex=%s)"
            % (str(self.startIndex), str(self.endIndex))
            if self is not None
            else "None"
        )

    def __repr__(self):
        return self.__str__()


class EntityIndices2(EntityIndices):
    added_info: str = "added info"


NOT_AVAILABLE_VALUE = -1
class MyEntity(BaseModel):
    name: str
    positions: EntityIndices

    def __hash__(self) -> int:
        return hash(self._relevant_attributes())

    def __eq__(self, other: "MyEntity") -> bool:
        # NOTE that equality between NoneType and other types can be checked without error
        # NOTE case-sensitive comparison for literal and value
        # NOTE that self.extensions is of type Dict[str, ExtensionPayload]
        if other is None:
            return False
        if not isinstance(other, MyEntity):
            return False
        return self._relevant_attributes() == other._relevant_attributes()

    def _relevant_attributes(
        self, replacement_for_none: int = NOT_AVAILABLE_VALUE
    ) -> Tuple[Tuple[int, int], str]:
        # NOTE set positions as first attribute
        # NOTE that comparison (beyond equality) between NoneType and other types cause TypeError
        return (
            # if positions is None, make it comparable
            self.positions.indices() if self.positions is not None else (replacement_for_none, replacement_for_none),
            #self.positions or EntityIndices(startIndex=replacement_for_none, endIndex=replacement_for_none),
            self.name,
        )

def exp1():

    ei1 = EntityIndices(startIndex=0, endIndex=8)
    ei2 = EntityIndices(startIndex=1, endIndex=8)
    print(ei1.indices())
    print(ei2.indices())
    print(ei1.indices() != ei2.indices())
    print(f"ei1 = {ei1} <{ei1==ei2}> ei2 = {ei2}")

    ei3 = EntityIndices(startIndex=0, endIndex=8)
    print(f"ei1 = {ei1} <{ei1==ei3}> ei3 = {ei3}")
    eilist = [ei1, ei2]
    print(f"ei3 in eilist? : {ei3 in eilist}")


    e1 = MyEntity(name="abc", positions=EntityIndices(startIndex=0, endIndex=9))
    e2 = MyEntity(name="abc", positions=EntityIndices(startIndex=1, endIndex=2))
    e3 = MyEntity(name="abc", positions=EntityIndices(startIndex=0, endIndex=9))
    elist = [e1, e2]

    print(e1.positions != ei1)
    print(type(e1.positions))
    print(type(ei1))
    print(f"e1: {e1}")

    e2 = None

    print(f"e3 in elist? : {e3 in elist}")


def exp2():

    ei1 = EntityIndices(startIndex=1, endIndex=2)
    ei2 = EntityIndices(startIndex=3, endIndex=4, malschauen="mal")
    ei1.model_config["additional"] = "bla"

    print(f"ei1: {ei1.model_dump()}")
    print(f"ei2: {ei2.model_dump()}")  # with extra=Extra.allow: ei2: {'startIndex': 3, 'endIndex': 4, 'malschauen': 'mal'}
    print(f"ei2.model_config: {ei2.model_config}")  # ei2.model_config: {'frozen': False, 'validate_assignment': True, 'extra': 'bla'}

    # could also include:
    # 'alias_generator': <function snake_to_camel at 0x7eff7be2be20>, 'populate_by_name': True, 'use_enum_values': True, 'extra': 'ignore'}]


def exp3():

    ei1 = EntityIndices(startIndex=1, endIndex=2)
    ei2 = EntityIndices2(**ei1.model_dump())
    ei2.endIndex=4

    print(ei1.model_dump())
    print(ei2.model_dump())



if __name__ == "__main__":
    # exp1()
    # exp2()
    exp3()
