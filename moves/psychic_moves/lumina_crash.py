from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class LuminaCrash(Move):
    def __init__(self):
        super().__init__("Lumina Crash", type=TypeFactory.create_type(Types.PSYCHIC), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Harshly lowers target’s Special Defense.
        """
        pass
