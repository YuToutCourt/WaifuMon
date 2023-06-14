from ..move import Move
from waifu_types.type import Type

class Feint(Move):
    def __init__(self):
        super().__init__("Feint", type=Type.NORMAL, power=30, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Only hits if opponent uses Protect or Detect in the same turn.
        """
        pass
