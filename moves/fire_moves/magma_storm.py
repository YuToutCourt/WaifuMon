from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MagmaStorm(Move):
    def __init__(self):
        super().__init__(
            "Magma Storm",
            type=TypeFactory.create_type(Types.FIRE),
            power=100,
            accuracy=75,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
