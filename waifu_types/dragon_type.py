from .type import Type
from .enum_types import Types


class Dragon_Type(Type):
    def __init__(self):
        super().__init__(
            Types.DRAGON, [Types.ICE, Types.DRAGON, Types.FAIRY], [Types.DRAGON], []
        )
