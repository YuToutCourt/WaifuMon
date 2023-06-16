from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpringtideStorm(Move):
    def __init__(self):
        super().__init__("Springtide Storm", type=TypeFactory.create_type(Types.FAIRY), power=100, accuracy=80, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Boosts user's stats in Incarnate Forme, or lowers opponent's stats in Therian Forme.
        """
        pass
