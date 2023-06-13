from .move import Move
from waifu_types.type import Type

class Bide(Move):
    def __init__(self):
        super().__init__("Bide", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User takes damage for two turns then strikes back double.
        """
        pass
