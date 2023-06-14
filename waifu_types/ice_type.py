from .type import Type
from .enum_types import Types


class Ice_Type(Type):
    def __init__(self):
        super().__init__(
            Types.ICE,
            [Types.FIRE, Types.FIGHTING, Types.ROCK, Types.STEEL],
            [Types.ICE],
            [],
        )
