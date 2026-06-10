from enum import Enum

class Environments(Enum):
    """Example Enum object.
    Adding values() method to an Enum object.
    Useful e.g. in choices parameter for argparse definitions:
    `choices=Environment.values()`
    """
    development = "development"
    staging = "staging"
    production = "production"

    @classmethod
    def values(cls) -> list[str]:
        return [kv.value for m, kv in cls.__members__.items()]
