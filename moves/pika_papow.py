from .move import Move
from waifu_types.type import Type

class PikaPapow(Move):
    def __init__(self):
        super().__init__("Pika Papow", type=Type.ELECTRIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Power increases when player's bond is stronger.
        """
        pass
