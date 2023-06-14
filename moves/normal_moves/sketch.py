from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Sketch(Move):
    def __init__(self):
        super().__init__("Sketch", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Permanently copies the opponent's last move.
        """
        pass
