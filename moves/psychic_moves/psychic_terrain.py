from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PsychicTerrain(Move):
    def __init__(self):
        super().__init__(
            "Psychic Terrain",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Prevents priority moves from being used for 5 turns.
        """
        pass
