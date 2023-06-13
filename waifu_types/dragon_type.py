from .type import Type
from .enum_types import Types


class Dragon_Type(Type):
    def __init__(self):
        super().__init__(
            Types.Dragon, [Types.Ice, Types.Dragon, Types.Fairy], [Types.Dragon], []
        )
