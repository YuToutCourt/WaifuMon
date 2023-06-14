from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GrassyGlide(Move):
    def __init__(self):
        super().__init__("Grassy Glide", type=TypeFactory.create_type(Types.GRASS), power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        High priority during Grassy Terrain.
        """
        pass
