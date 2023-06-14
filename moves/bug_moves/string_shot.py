from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class StringShot(Move):
    def __init__(self):
        super().__init__("String Shot", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=95, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Speed.
        """
        pass
