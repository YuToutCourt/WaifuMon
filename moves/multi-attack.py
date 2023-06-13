from .move import Move
from waifu_types.type import Type

class Multi-Attack(Move):
    def __init__(self):
        super().__init__("Multi-Attack", type=Type.NORMAL, power=120, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Type matches Memory item held.
        """
        pass
