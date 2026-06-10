"""
This snippet shows how a fallback value can be added to an enum class for
internal use.
The fallback value is associated with one of the actual values, and thus, it
won't be listed in the member set as this counts the values.
"""
from enum import StrEnum


class MyType(StrEnum):
    TYPE1 = "T1"
    TYPE2 = "T2"
    TYPE3 = "T3"
    FALLBACK = TYPE1  # won't be listed in member_set(), since associated with T1
    # FALLBACK = "T1"  # you can add the value directly as well


    @staticmethod
    def get_member(type_str: str) -> "MyType":
        try:
            return MyType(type_str)
        except ValueError:
            return MyType.FALLBACK

    @staticmethod
    def member_set() -> set["MyType"]:
        member_set = set(__class__)
        return member_set

    @classmethod
    def members(cls) -> list[str]:
        members = [m for m, kv in cls.__members__.items()]
        return members


def main():
    ct = MyType.get_member("T3")
    print(f"Get T3 member: {ct}")

    print(f"Member set: {ct.member_set()}")     # NOTE: does not including FALLBACK
    print(f"Member name list: {ct.members()}")  # NOTE: containing "FALLBACK"

    ct_fallback = MyType.get_member("dummy")    # NOTE: pointing to MyType.T1
    print(f"Get Fallback member: {ct_fallback}")
    print(f"Fallback name: {ct_fallback.name}, value: {ct_fallback.value}")


if __name__ == "__main__":
    main()
