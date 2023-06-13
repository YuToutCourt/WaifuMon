from .type import Type
from .enum_types import Types


class Psy_Type(Type):
    def __init__(self):
        super().__init__(
            Types.PSY,
            [Types.BUG, Types.DARK, Types.GHOST],
            [Types.FIGHTING, Types.PSYCHIC],
            [],
        )
