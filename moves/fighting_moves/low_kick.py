from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from random import randint

class LowKick(Move):
    def __init__(self):
        super().__init__(
            "Low Kick",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=randint(1, 120),
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The heavier the opponent, the stronger the attack.
        """
        pass
