from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ThunderCage(Move):
    def __init__(self):
        super().__init__(
            "Thunder Cage",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=80,
            accuracy=90,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Deals damage and traps opponent, damaging them for 4-5 turns.
        """
        pass
