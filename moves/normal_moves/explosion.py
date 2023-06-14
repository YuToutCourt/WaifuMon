from ..move import Move
from waifu_types.type import Type

class Explosion(Move):
    def __init__(self):
        super().__init__("Explosion", type=Type.NORMAL, power=250, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User faints.
        """
        pass
