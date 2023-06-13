from .move import Move
from waifu_types.type import Type

class Aromatherapy(Move):
    def __init__(self):
        super().__init__("Aromatherapy", type=Type.GRASS, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Cures all status problems in your party.
        """
        pass
