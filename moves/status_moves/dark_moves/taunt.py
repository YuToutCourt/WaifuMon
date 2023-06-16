from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Taunt(Move):
    def __init__(self):
        super().__init__("Taunt", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent can only use moves that attack.
        """
        pass
