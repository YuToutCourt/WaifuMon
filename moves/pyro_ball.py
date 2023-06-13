from .move import Move
from waifu_types.type import Type

class PyroBall(Move):
    def __init__(self):
        super().__init__("Pyro Ball", type=Type.FIRE, power=120, accuracy=90, pp=5, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
