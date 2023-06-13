from .type import Type
from .enum_types import Types


class Flying_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Flying,
            [Types.Electric, Types.Ice, Types.Rock],
            [Types.Grass, Types.Fighting, Types.Bug],
            [Types.Ground],
        )
