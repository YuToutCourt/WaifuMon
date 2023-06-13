from .move import Move
from waifu_types.type import Type

class ExtremeEvoboost(Move):
    def __init__(self):
        super().__init__("Extreme Evoboost", type=Type.NORMAL, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Eevee-exclusive Z-Move. Sharply raises all stats.
        """
        pass
