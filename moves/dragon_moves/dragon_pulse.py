from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonPulse(Move):
    def __init__(self):
        super().__init__(
            "Dragon Pulse",
            type=TypeFactory.create_type(Types.DRAGON),
            power=85,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass
