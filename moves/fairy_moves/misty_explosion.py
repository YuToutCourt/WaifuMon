from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MistyExplosion(Move):
    def __init__(self):
        super().__init__("Misty Explosion", type=TypeFactory.create_type(Types.FAIRY), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases on Misty Terrain.
        """
        pass
