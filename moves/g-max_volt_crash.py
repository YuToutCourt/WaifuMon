from .move import Move
from waifu_types.type import Type

class G-MaxVoltCrash(Move):
    def __init__(self):
        super().__init__("G-Max Volt Crash", type=Type.ELECTRIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Pikachu-exclusive G-Max Move. Paralyzes opponents.
        """
        pass
