from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AuraWheel(Move):
    def __init__(self):
        super().__init__(
            "Aura Wheel",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=110,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Changes type based on Morpeko's Mode.
        """
        pass
