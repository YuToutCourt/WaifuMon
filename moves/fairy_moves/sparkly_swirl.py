from ..move import Move
from waifu_types.type import Type

class SparklySwirl(Move):
    def __init__(self):
        super().__init__("Sparkly Swirl", type=Type.FAIRY, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Cures all status problems in the party Pokémon.
        """
        pass
