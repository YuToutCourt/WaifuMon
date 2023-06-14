from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Snarl(Move):
    def __init__(self):
        super().__init__("Snarl", type=TypeFactory.create_type(Types.DARK), power=55, accuracy=95, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
