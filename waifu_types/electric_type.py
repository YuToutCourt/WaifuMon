from .type import Type
from .enum_types import Types


class Electric_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Electric,
            [Types.Ground],
            [Types.Electric, Types.Flying, Types.Steel],
            [],
        )
