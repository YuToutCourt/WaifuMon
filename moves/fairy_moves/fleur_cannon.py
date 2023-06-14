from ..move import Move
from waifu_types.type import Type

class FleurCannon(Move):
    def __init__(self):
        super().__init__("Fleur Cannon", type=Type.FAIRY, power=130, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers user's Special Attack.
        """
        pass
