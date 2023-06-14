from .type import Type
from .enum_types import Types


class Fairy_Type(Type):
    def __init__(self):
        super().__init__(
            Types.FAIRY,
            [Types.POISON, Types.STEEL],
            [Types.FIGHT, Types.BUG, Types.DARK],
            [Types.DRAGON],
        )
