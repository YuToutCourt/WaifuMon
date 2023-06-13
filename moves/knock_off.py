from .move import Move
from waifu_types.type import Type

class KnockOff(Move):
    def __init__(self):
        super().__init__("Knock Off", type=Type.DARK, power=65, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Removes opponent's held item for the rest of the battle.
        """
        pass
