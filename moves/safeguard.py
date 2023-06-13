from .move import Move
from waifu_types.type import Type

class Safeguard(Move):
    def __init__(self):
        super().__init__("Safeguard", type=Type.NORMAL, power=0, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        The user's party is protected from status conditions.
        """
        pass
