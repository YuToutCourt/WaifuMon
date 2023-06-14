from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FairyWind(Move):
    def __init__(self):
        super().__init__("Fairy Wind", type=TypeFactory.create_type(Types.FAIRY), power=40, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
