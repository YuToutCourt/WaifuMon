from .type import Type
from .enum_types import Types


class Rock_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Rock,
            [Types.Water, Types.Grass, Types.Fighting, Types.Ground, Types.Steel],
            [Types.Normal, Types.Fire, Types.Poison, Types.Flying],
            [],
        )
