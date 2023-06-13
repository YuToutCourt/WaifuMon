from .type import Type
from .enum_types import Types


class Bug_Type(Type):
    def __init__(self):
        super().__init__(
            Types.BUG,
            [Types.FIRE, Types.FLYING, Types.ROCK],
            [Types.FIGHTING, Types.GRASS, Types.GROUND],
            [],
        )
