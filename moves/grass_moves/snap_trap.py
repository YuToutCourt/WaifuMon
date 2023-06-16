from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SnapTrap(Move):
    def __init__(self):
        super().__init__(
            "Snap Trap",
            type=TypeFactory.create_type(Types.GRASS),
            power=35,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
