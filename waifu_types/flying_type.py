from .type import Type
from .enum_types import Types


class Flying_Type(Type):
    def __init__(self):
        super().__init__(
            Types.FLYING,
            [Types.ELECTRIC, Types.ICE, Types.ROCK],
            [Types.GRASS, Types.FIGHTING, Types.BUG],
            [Types.GROUND],
        )
