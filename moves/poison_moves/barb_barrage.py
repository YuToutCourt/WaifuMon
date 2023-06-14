from ..move import Move
from waifu_types.type import Type

class BarbBarrage(Move):
    def __init__(self):
        super().__init__("Barb Barrage", type=Type.POISON, power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target has a status condition.
        """
        pass
