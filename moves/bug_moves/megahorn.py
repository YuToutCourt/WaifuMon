from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Megahorn(Move):
    def __init__(self):
        super().__init__("Megahorn", type=TypeFactory.create_type(Types.BUG), power=120, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
