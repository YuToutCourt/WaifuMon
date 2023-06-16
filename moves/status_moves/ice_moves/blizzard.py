from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Blizzard(Move):
    def __init__(self):
        super().__init__("Blizzard", type=TypeFactory.create_type(Types.ICE), power=110, accuracy=70, pp=5, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
