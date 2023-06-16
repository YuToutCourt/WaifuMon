from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MortalSpin(Move):
    def __init__(self):
        super().__init__(
            "Mortal Spin",
            type=TypeFactory.create_type(Types.POISON),
            power=30,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Removes entry hazards and trap move effects, and poisons opposing Pokemon.
        """
        pass
