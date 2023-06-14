from ..move import Move
from waifu_types.type import Type

class FusionBolt(Move):
    def __init__(self):
        super().__init__("Fusion Bolt", type=Type.ELECTRIC, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases if Fusion Flare is used in the same turn.
        """
        pass
