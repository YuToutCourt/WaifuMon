from .move import Move
from waifu_types.type import Type

class StrangeSteam(Move):
    def __init__(self):
        super().__init__("Strange Steam", type=Type.FAIRY, power=90, accuracy=95, pp=10, proba_effect=20)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
