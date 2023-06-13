from .type import Type
from .enum_types import Types


class Ice_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Ice,
            [Types.Fire, Types.Fighting, Types.Rock, Types.Steel],
            [Types.Ice],
            [],
        )
