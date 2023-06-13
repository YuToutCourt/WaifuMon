from .type import Type
from .enum_types import Types


class Poison_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Poison,
            [Types.Ground, Types.Psychic],
            [Types.Grass, Types.Fighting, Types.Poison, Types.Bug, Types.Fairy],
            [],
        )
