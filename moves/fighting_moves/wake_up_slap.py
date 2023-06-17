from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WakeUpSlap(Move):
    def __init__(self):
        super().__init__(
            "Wake-Up Slap",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=70,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power doubles if opponent is asleep, but wakes it up.
        """
        pass
