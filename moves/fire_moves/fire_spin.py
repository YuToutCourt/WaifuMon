from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FireSpin(Move):
    def __init__(self):
        super().__init__(
            "Fire Spin",
            type=TypeFactory.create_type(Types.FIRE),
            power=35,
            accuracy=85,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
