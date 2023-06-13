from .type import Type
from .enum_types import Types


class Rock_Type(Type):
    def __init__(self):
        super().__init__(
            Types.ROCK,
            [Types.WATER, Types.GRASS, Types.FIGHTING, Types.GROUND, Types.STEEL],
            [Types.NORMAL, Types.FIRE, Types.POISON, Types.FLYING],
            [],
        )
