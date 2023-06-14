from ..move import Move
from waifu_types.type import Type

class G-MaxCannonade(Move):
    def __init__(self):
        super().__init__("G-Max Cannonade", type=Type.WATER, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Blastoise-exclusive G-Max Move. Damages non-Water types for 4 turns.
        """
        pass
