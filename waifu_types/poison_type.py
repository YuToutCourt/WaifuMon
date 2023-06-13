from .type import Type
from .enum_types import Types


class Poison_Type(Type):
    def __init__(self):
        super().__init__(
            Types.POISON,
            [Types.GROUND, Types.PSYCHIC],
            [Types.GRASS, Types.FIGHTING, Types.POISON, Types.BUG, Types.FAIRY],
            [],
        )
