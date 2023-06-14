from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxResonance(Move):
    def __init__(self):
        super().__init__("G-Max Resonance", type=TypeFactory.create_type(Types.ICE), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lapras-exclusive G-Max Move. Reduces damage for 5 turns.
        """
        pass
