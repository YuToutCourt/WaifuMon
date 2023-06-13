from .move import Move
from waifu_types.type import Type

class BlazeKick(Move):
    def __init__(self):
        super().__init__("Blaze Kick", type=Type.FIRE, power=85, accuracy=90, pp=10, proba_effect=10)

    def effect(self):
        """
        High critical hit ratio. May burn opponent.
        """
        pass
