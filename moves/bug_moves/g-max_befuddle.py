from ..move import Move
from waifu_types.type import Type

class G-MaxBefuddle(Move):
    def __init__(self):
        super().__init__("G-Max Befuddle", type=Type.BUG, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Butterfree-exclusive G-Max Move. Poisons, paralyzes, or puts opponent to sleep.
        """
        pass
