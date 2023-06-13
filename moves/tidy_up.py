from .move import Move
from waifu_types.type import Type

class TidyUp(Move):
    def __init__(self):
        super().__init__("Tidy Up", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Removes the effects of entry hazards and Substitute, and boosts user’s Attack and Speed.
        """
        pass
