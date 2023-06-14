from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Trick(Move):
    def __init__(self):
        super().__init__("Trick", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Swaps held items with the opponent.
        """
        pass
