from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FinalGambit(Move):
    def __init__(self):
        super().__init__("Final Gambit", type=TypeFactory.create_type(Types.FIGHTING), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts damage equal to the user's remaining HP. User faints.
        """
        pass
