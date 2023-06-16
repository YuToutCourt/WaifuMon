from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Charm(Move):
    def __init__(self):
        super().__init__("Charm", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Attack.
        """
        pass
