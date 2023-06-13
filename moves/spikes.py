from .move import Move
from waifu_types.type import Type

class Spikes(Move):
    def __init__(self):
        super().__init__("Spikes", type=Type.GROUND, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Hurts opponents when they switch into battle.
        """
        pass
