from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AquaTail(Move):
    def __init__(self):
        super().__init__("Aqua Tail", type=TypeFactory.create_type(Types.WATER), power=90, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
