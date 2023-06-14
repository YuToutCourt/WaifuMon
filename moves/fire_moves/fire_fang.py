from ..move import Move
from waifu_types.type import Type

class FireFang(Move):
    def __init__(self):
        super().__init__("Fire Fang", type=Type.FIRE, power=65, accuracy=95, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May cause flinching and/or burn opponent.
        """
        pass
