from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GigaDrain(Move):
    def __init__(self):
        super().__init__(
            "Giga Drain",
            type=TypeFactory.create_type(Types.GRASS),
            power=75,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass
