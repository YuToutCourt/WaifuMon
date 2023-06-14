from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxStonesurge(Move):
    def __init__(self):
        super().__init__("G-Max Stonesurge", type=TypeFactory.create_type(Types.WATER), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Drednaw-exclusive G-Max Move. Sets up Stealth Rock.
        """
        pass
