from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Covet(Move):
    def __init__(self):
        super().__init__("Covet", type=TypeFactory.create_type(Types.NORMAL), power=60, accuracy=100, pp=25, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent's item is stolen by the user.
        """
        pass
