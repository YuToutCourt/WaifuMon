from ..move import Move
from waifu_types.type import Type

class Chatter(Move):
    def __init__(self):
        super().__init__("Chatter", type=Type.FLYING, power=65, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
