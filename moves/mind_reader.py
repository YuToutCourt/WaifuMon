from .move import Move
from waifu_types.type import Type

class MindReader(Move):
    def __init__(self):
        super().__init__("Mind Reader", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User's next attack is guaranteed to hit.
        """
        pass
