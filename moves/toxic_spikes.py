from .move import Move
from waifu_types.type import Type

class ToxicSpikes(Move):
    def __init__(self):
        super().__init__("Toxic Spikes", type=Type.POISON, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Poisons opponents when they switch into battle.
        """
        pass
