from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BrickBreak(Move):
    def __init__(self):
        super().__init__(
            "Brick Break",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=75,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Breaks through Reflect and Light Screen barriers.
        """
        pass
