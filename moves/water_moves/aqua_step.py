from ..move import Move
from waifu_types.type import Type

class AquaStep(Move):
    def __init__(self):
        super().__init__("Aqua Step", type=Type.WATER, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Speed.
        """
        pass
