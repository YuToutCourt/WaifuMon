from ..move import Move
from waifu_types.type import Type

class G-MaxFinale(Move):
    def __init__(self):
        super().__init__("G-Max Finale", type=Type.FAIRY, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Alcremie-exclusive G-Max Move. Heals the user's team.
        """
        pass
