from .type import Type
from .enum_types import Types


class Grass_Type(Type):
    def __init__(self):
        super().__init__(
            Types.GRASS,
            [Types.FIRE, Types.ICE, Types.POISON, Types.FLYING, Types.BUG],
            [Types.WATER, Types.ELECTRIC, Types.GRASS, Types.GROUND],
            [],
        )
