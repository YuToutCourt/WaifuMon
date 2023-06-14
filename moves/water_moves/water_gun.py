from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class WaterGun(Move):
    def __init__(self):
        super().__init__("Water Gun", type=TypeFactory.create_type(Types.WATER), power=40, accuracy=100, pp=25, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
