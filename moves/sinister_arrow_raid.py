from .move import Move
from waifu_types.type import Type

class SinisterArrowRaid(Move):
    def __init__(self):
        super().__init__("Sinister Arrow Raid", type=Type.GHOST, power=180, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Decidueye-exclusive Z-Move.
        """
        pass
