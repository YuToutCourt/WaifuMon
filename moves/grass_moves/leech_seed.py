from ..move import Move
from waifu_types.type import Type

class LeechSeed(Move):
    def __init__(self):
        super().__init__("Leech Seed", type=Type.GRASS, power=0, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Drains HP from opponent each turn.
        """
        pass
