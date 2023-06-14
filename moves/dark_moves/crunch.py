from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Crunch(Move):
    def __init__(self):
        super().__init__("Crunch", type=TypeFactory.create_type(Types.DARK), power=80, accuracy=100, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
