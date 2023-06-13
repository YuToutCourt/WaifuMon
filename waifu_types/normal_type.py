from .type import Type
from .enum_types import Types


class Normal_Type(Type):
    def __init__(self):
        super().__init__(Types.NORMAL, [Types.FIGHTING], [], [Types.GHOST])
