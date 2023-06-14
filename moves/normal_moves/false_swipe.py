from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FalseSwipe(Move):
    def __init__(self):
        super().__init__("False Swipe", type=TypeFactory.create_type(Types.NORMAL), power=40, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Always leaves opponent with at least 1 HP.
        """
        pass
