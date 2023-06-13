from .move import Move
from waifu_types.type import Type

class MaxSteelspike(Move):
    def __init__(self):
        super().__init__("Max Steelspike", type=Type.STEEL, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Steel type Dynamax move. Raises the team's Defense.
        """
        pass
