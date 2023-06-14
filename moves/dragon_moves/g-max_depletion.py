from ..move import Move
from waifu_types.type import Type

class G-MaxDepletion(Move):
    def __init__(self):
        super().__init__("G-Max Depletion", type=Type.DRAGON, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Duraludon-exclusive G-Max Move. Reduces opponent's PP.
        """
        pass
