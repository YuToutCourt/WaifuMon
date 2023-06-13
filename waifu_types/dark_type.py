from .type import Type
from .enum_types import Types


class Dark_Type(Type):
    def __init__(self):
        super().__init__(
            Types.DARK,
            [Types.BUG, Types.FAIRY, Types.FIGHTING],
            [Types.DARK, Types.GHOST],
            [Types.PSYCHIC],
        )
