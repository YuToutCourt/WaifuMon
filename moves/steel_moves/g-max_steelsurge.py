from ..move import Move
from waifu_types.type import Type

class G-MaxSteelsurge(Move):
    def __init__(self):
        super().__init__("G-Max Steelsurge", type=Type.STEEL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Copperajah-exclusive G-Max Move. Sets up Spikes on the field.
        """
        pass
