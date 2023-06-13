from .move import Move
from waifu_types.type import Type

class ArmorCannon(Move):
    def __init__(self):
        super().__init__("Armor Cannon", type=Type.FIRE, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense and Special Defense.
        """
        pass
