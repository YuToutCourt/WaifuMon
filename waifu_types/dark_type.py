from .type import Type
from .enum_types import Types


class Dark_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Dark,
            [Types.Bug, Types.Fairy, Types.Fighting],
            [Types.Dark, Types.Ghost],
            [Types.Psychic],
        )
