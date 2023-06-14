from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxVoltCrash(Move):
    def __init__(self):
        super().__init__("G-Max Volt Crash", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Pikachu-exclusive G-Max Move. Paralyzes opponents.
        """
        pass
