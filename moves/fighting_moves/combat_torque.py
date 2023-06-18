from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CombatTorque(Move):
    def __init__(self):
        super().__init__(
            "Combat Torque",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=100,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ 
        No effect.
        """
        pass
