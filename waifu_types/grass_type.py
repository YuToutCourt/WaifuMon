from .type import Type
from .enum_types import Types


class Grass_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Grass,
            [Types.Fire, Types.Ice, Types.Poison, Types.Flying, Types.Bug],
            [Types.Water, Types.Electric, Types.Grass, Types.Ground],
            [],
        )
