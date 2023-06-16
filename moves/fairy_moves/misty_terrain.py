from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MistyTerrain(Move):
    def __init__(self):
        super().__init__(
            "Misty Terrain",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Protects the field from status conditions for 5 turns.
        """
        pass
