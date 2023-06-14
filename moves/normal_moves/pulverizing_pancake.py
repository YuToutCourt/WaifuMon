from ..move import Move
from waifu_types.type import Type

class PulverizingPancake(Move):
    def __init__(self):
        super().__init__("Pulverizing Pancake", type=Type.NORMAL, power=210, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Snorlax-exclusive Normal type Z-Move.
        """
        pass
