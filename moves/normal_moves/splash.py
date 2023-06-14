from ..move import Move
from waifu_types.type import Type

class Splash(Move):
    def __init__(self):
        super().__init__("Splash", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Doesn't do ANYTHING.
        """
        pass
