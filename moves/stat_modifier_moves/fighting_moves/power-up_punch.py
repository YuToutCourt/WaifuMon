from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PowerUpPunch(Move):
    def __init__(self):
        super().__init__(
            "Power-Up Punch",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=40,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises Attack.
        """
        pass
