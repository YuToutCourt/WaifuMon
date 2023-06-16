from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PrecipiceBlades(Move):
    def __init__(self):
        super().__init__(
            "Precipice Blades",
            type=TypeFactory.create_type(Types.GROUND),
            power=120,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
