from .type import Type
from .enum_types import Types


class Ground_Type(Type):
    def __init__(self):
        super().__init__(
            Types.GROUND,
            [Types.WATER, Types.GRASS, Types.ICE],
            [Types.POISON, Types.ROCK],
            [Types.ELECTRIC],
        )
