from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Telekinesis(Move):
    def __init__(self):
        super().__init__("Telekinesis", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores opponent's Evasiveness for three turns, add Ground immunity.
        """
        pass
