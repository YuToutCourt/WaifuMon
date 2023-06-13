from .type import Type
from .enum_types import Types


class Steel_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Steel,
            [Types.Fire, Types.Fight, Types.Ground],
            [
                Types.Normal,
                Types.Grass,
                Types.Ice,
                Types.Flying,
                Types.Psychic,
                Types.Bug,
                Types.Rock,
                Types.Dragon,
                Types.Fairy,
                Types.Steel,
            ],
            [Types.Poison],
        )
