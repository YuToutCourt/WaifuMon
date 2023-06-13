from .move import Move
from waifu_types.type import Type

class SwordsDance(Move):
    def __init__(self):
        super().__init__("Swords Dance", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Attack.
        """
        pass
