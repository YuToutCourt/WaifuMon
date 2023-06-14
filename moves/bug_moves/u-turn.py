from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class U-turn(Move):
    def __init__(self):
        super().__init__("U-turn", type=TypeFactory.create_type(Types.BUG), power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User switches out immediately after attacking.
        """
        pass
