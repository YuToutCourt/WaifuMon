from .type import Type
from .enum_types import Types


class Fire_Type(Type):
    def __init__(self):
        super().__init__(
            Types.FIRE,
            [Types.WATER, Types.GROUND, Types.ROCK],
            [Types.FIRE, Types.GRASS, Types.ICE, Types.BUG, Types.STEEL],
            [],
        )
