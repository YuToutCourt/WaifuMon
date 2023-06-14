from typing import List
from .enum_types import Types


class Type:
    def __init__(
        self,
        type_name: Types,
        weaknesses: List[Types],
        resistances: List[Types],
        immunities: List[Types],
    ):
        self.type_name = type_name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities
