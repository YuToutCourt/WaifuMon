from .move import Move
from waifu_types.type import Type

class MaxGeyser(Move):
    def __init__(self):
        super().__init__("Max Geyser", type=Type.WATER, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Water type Dynamax move. Summons heavy rain.
        """
        pass
