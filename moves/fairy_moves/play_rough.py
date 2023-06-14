from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PlayRough(Move):
    def __init__(self):
        super().__init__("Play Rough", type=TypeFactory.create_type(Types.FAIRY), power=90, accuracy=90, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Attack.
        """
        pass
