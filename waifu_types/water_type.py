from .type import Type
from .enum_types import Types


class Water_Type(Type):
    def __init__(self):
        super().__init__(
            Types.WATER,
            [Types.ELECTRIC, Types.GRASS],
            [Types.FIRE, Types.WATER, Types.ICE, Types.STEEL],
            [],
        )
