from .type import Type
from .enum_types import Types


class Steel_Type(Type):
    def __init__(self):
        super().__init__(
            Types.STEEL,
            [Types.FIRE, Types.FIGHT, Types.GROUND],
            [
                Types.NORMAL,
                Types.GRASS,
                Types.ICE,
                Types.FLYING,
                Types.PSYCHIC,
                Types.BUG,
                Types.ROCK,
                Types.DRAGON,
                Types.FAIRY,
                Types.STEEL,
            ],
            [Types.POISON],
        )
