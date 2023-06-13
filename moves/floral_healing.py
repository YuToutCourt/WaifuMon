from .move import Move
from waifu_types.type import Type

class FloralHealing(Move):
    def __init__(self):
        super().__init__("Floral Healing", type=Type.FAIRY, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user restores the target's HP by up to half of its max HP. It restores more HP when the terrain is grass.
        """
        pass
