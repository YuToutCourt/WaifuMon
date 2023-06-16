from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ArmThrust(Move):
    def __init__(self):
        super().__init__(
            "Arm Thrust",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=15,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
