from .type import Type
from .enum_types import Types


class Fighting_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Fighting,
            [Types.Flying, Types.Psychic, Types.Fairy],
            [Types.Bug, Types.Dark, Types.Rock],
            [],
        )
