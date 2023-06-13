from .move import Move
from waifu_types.type import Type

class MaxPhantasm(Move):
    def __init__(self):
        super().__init__("Max Phantasm", type=Type.GHOST, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Ghost type Dynamax move. Lowers the target's Defense.
        """
        pass
