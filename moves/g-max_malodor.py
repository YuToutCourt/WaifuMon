from .move import Move
from waifu_types.type import Type

class G-MaxMalodor(Move):
    def __init__(self):
        super().__init__("G-Max Malodor", type=Type.POISON, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Garbodor-exclusive G-Max Move. Poisons opponents.
        """
        pass
