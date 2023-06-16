from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SunnyDay(Move):
    def __init__(self):
        super().__init__(
            "Sunny Day",
            type=TypeFactory.create_type(Types.FIRE),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Makes it sunny for 5 turns.
        """
        pass
