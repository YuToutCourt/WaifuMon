from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Psystrike(Move):
    def __init__(self):
        super().__init__("Psystrike", type=TypeFactory.create_type(Types.PSYCHIC), power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts damage based on the target's Defense, not Special Defense.
        """
        pass
