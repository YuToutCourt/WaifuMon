from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Cut(Move):
    def __init__(self):
        super().__init__("Cut", type=TypeFactory.create_type(Types.NORMAL), power=50, accuracy=95, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
