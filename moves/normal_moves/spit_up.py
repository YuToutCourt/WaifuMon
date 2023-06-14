from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpitUp(Move):
    def __init__(self):
        super().__init__("Spit Up", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power depends on how many times the user performed Stockpile.
        """
        pass
