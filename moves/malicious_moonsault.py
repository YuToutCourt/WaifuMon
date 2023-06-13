from .move import Move
from waifu_types.type import Type

class MaliciousMoonsault(Move):
    def __init__(self):
        super().__init__("Malicious Moonsault", type=Type.DARK, power=180, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Incineroar-exclusive Z-Move.
        """
        pass
