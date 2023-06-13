from .move import Move
from waifu_types.type import Type

class DestinyBond(Move):
    def __init__(self):
        super().__init__("Destiny Bond", type=Type.GHOST, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        If the user faints, the opponent also faints.
        """
        pass
