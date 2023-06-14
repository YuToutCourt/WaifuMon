from ..move import Move
from waifu_types.type import Type

class G-MaxSmite(Move):
    def __init__(self):
        super().__init__("G-Max Smite", type=Type.FAIRY, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Hatterene-exclusive G-Max Move. Confuses opponents.
        """
        pass
