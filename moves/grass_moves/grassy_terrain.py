from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GrassyTerrain(Move):
    def __init__(self):
        super().__init__(
            "Grassy Terrain",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Restores a little HP of all Pokemon for 5 turns.
        """
        pass
