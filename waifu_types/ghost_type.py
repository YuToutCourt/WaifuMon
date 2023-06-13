from .type import Type
from .enum_types import Types


class Ghost_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Ghost,
            [Types.Dark, Types.Ghost],
            [Types.Poison, Types.Bug],
            [Types.Normal, Types.Fighting],
        )
