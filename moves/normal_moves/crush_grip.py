from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class CrushGrip(Move):
    def __init__(self):
        super().__init__("Crush Grip", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        More powerful when opponent has higher HP.
        """
        pass
