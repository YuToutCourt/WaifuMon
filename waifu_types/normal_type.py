from .type import Type
from .enum_types import Types


class Normal_Type(Type):
    def __init__(self):
        super().__init__(Types.Normal, [Types.Fighting], [], [Types.Ghost])
