from ..move import Move
from waifu_types.type import Type

class MaxFlare(Move):
    def __init__(self):
        super().__init__("Max Flare", type=Type.FIRE, power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Fire type Dynamax move. Summons harsh sunlight.
        """
        pass
