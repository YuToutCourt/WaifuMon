from .move import Move
from waifu_types.type import Type

class Doodle(Move):
    def __init__(self):
        super().__init__("Doodle", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Changes the abilities of the user and its teammates to that of the target.
        """
        pass
