from ..move import Move
from waifu_types.type import Type

class MountainGale(Move):
    def __init__(self):
        super().__init__("Mountain Gale", type=Type.ICE, power=100, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Speed.
        """
        pass
