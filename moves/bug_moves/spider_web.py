from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpiderWeb(Move):
    def __init__(self):
        super().__init__("Spider Web", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot escape/switch.
        """
        pass
