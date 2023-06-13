from .move import Move
from waifu_types.type import Type

class G-MaxResonance(Move):
    def __init__(self):
        super().__init__("G-Max Resonance", type=Type.ICE, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Lapras-exclusive G-Max Move. Reduces damage for 5 turns.
        """
        pass
