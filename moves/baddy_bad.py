from .move import Move
from waifu_types.type import Type

class BaddyBad(Move):
    def __init__(self):
        super().__init__("Baddy Bad", type=Type.DARK, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Reduces damage from Physical attacks.
        """
        pass
