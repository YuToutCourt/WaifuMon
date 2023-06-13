from .move import Move
from waifu_types.type import Type

class FusionFlare(Move):
    def __init__(self):
        super().__init__("Fusion Flare", type=Type.FIRE, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Power increases if Fusion Bolt is used in the same turn.
        """
        pass
