from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Reflect(Move):
    def __init__(self):
        super().__init__("Reflect", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves damage from Physical attacks for 5 turns.
        """
        pass
