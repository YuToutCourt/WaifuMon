from .type import Type
from .enum_types import Types


class Bug_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Bug,
            [Types.Fire, Types.Flying, Types.Rock],
            [Types.Fighting, Types.Grass, Types.Ground],
            [],
        )
