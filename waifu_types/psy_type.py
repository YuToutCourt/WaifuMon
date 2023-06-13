from .type import Type
from .enum_types import Types


class Psy_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Psy,
            [Types.Bug, Types.Dark, Types.Ghost],
            [Types.Fighting, Types.Psychic],
            [],
        )
