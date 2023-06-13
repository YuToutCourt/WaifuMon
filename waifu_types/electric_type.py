from .type import Type
from .enum_types import Types


class Electric_Type(Type):
    def __init__(self):
        super().__init__(
            Types.ELECTRIC,
            [Types.GROUND],
            [Types.ELECTRIC, Types.FLYING, Types.STEEL],
            [],
        )
