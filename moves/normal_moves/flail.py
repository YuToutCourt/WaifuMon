from ..move import Move
from waifu_types.type import Type

class Flail(Move):
    def __init__(self):
        super().__init__("Flail", type=Type.NORMAL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The lower the user's HP, the higher the power.
        """
        pass
