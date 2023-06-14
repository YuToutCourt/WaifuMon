from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FocusBlast(Move):
    def __init__(self):
        super().__init__("Focus Blast", type=TypeFactory.create_type(Types.FIGHTING), power=120, accuracy=70, pp=5, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
