from .move import Move
from waifu_types.type import Type

class Spotlight(Move):
    def __init__(self):
        super().__init__("Spotlight", type=Type.NORMAL, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        The user shines a spotlight on the target so that only the target will be attacked during the turn.
        """
        pass
