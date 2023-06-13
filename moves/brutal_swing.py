from .move import Move
from waifu_types.type import Type

class BrutalSwing(Move):
    def __init__(self):
        super().__init__("Brutal Swing", type=Type.DARK, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        The user swings its body around violently to inflict damage on everything in its vicinity.
        """
        pass
