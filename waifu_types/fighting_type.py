from .type import Type
from .enum_types import Types


class Fighting_Type(Type):
    def __init__(self):
        super().__init__(
            Types.FIGHTING,
            [Types.FLYING, Types.PSYCHIC, Types.FAIRY],
            [Types.BUG, Types.DARK, Types.ROCK],
            [],
        )
