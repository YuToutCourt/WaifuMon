from .type import Type
from .enum_types import Types


class Ground_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Ground,
            [Types.Water, Types.Grass, Types.Ice],
            [Types.Poison, Types.Rock],
            [Types.Electric],
        )
