from ..move import Move
from waifu_types.type import Type

class WorkUp(Move):
    def __init__(self):
        super().__init__("Work Up", type=Type.NORMAL, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and Special Attack.
        """
        pass