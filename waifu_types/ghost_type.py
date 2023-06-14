from .type import Type
from .enum_types import Types


class Ghost_Type(Type):
    def __init__(self):
        super().__init__(
            Types.GHOST,
            [Types.DARK, Types.GHOST],
            [Types.POISON, Types.BUG],
            [Types.NORMAL, Types.FIGHTING],
        )
