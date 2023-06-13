from .type import Type
from .enum_types import Types


class Fire_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Fire,
            [Types.Water, Types.Ground, Types.Rock],
            [Types.Fire, Types.Grass, Types.Ice, Types.Bug, Types.Steel],
            [],
        )
