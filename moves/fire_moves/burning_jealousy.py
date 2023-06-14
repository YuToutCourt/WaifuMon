from ..move import Move
from waifu_types.type import Type

class BurningJealousy(Move):
    def __init__(self):
        super().__init__("Burning Jealousy", type=Type.FIRE, power=70, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all opponents, and burns any that have had their stats boosted.
        """
        pass
