from ..move import Move
from waifu_types.type import Type

class DefenseCurl(Move):
    def __init__(self):
        super().__init__("Defense Curl", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Defense.
        """
        pass
