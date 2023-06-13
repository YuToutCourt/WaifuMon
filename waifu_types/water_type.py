from .type import Type
from .enum_types import Types


class Water_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Water,
            [Types.Electric, Types.Grass],
            [Types.Fire, Types.Water, Types.Ice, Types.Steel],
            [],
        )
