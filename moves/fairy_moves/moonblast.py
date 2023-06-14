from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Moonblast(Move):
    def __init__(self):
        super().__init__("Moonblast", type=TypeFactory.create_type(Types.FAIRY), power=95, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Special Attack.
        """
        pass
