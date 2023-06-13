from .move import Move
from waifu_types.type import Type

class SurgingStrikes(Move):
    def __init__(self):
        super().__init__("Surging Strikes", type=Type.WATER, power=25, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit and ignores stat changes.
        """
        pass
