from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TerrainPulse(Move):
    def __init__(self):
        super().__init__(
            "Terrain Pulse",
            type=TypeFactory.create_type(Types.NORMAL),
            power=50,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Type and power change depending on the Terrain in effect.
        """
        pass
