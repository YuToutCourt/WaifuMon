from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MindBlown(Move):
    def __init__(self):
        super().__init__("Mind Blown", type=TypeFactory.create_type(Types.FIRE), power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
