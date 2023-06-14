from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Nature'sMadness(Move):
    def __init__(self):
        super().__init__("Nature's Madness", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves the foe's HP.
        """
        pass
