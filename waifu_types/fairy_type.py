from .type import Type
from .enum_types import Types


class Fairy_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Fairy,
            [Types.Poison, Types.Steel],
            [Types.Fight, Types.Bug, Types.Dark],
            [Types.Dragon],
        )
