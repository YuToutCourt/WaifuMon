from .move import Move
from waifu_types.type import Type

class FireLash(Move):
    def __init__(self):
        super().__init__("Fire Lash", type=Type.FIRE, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        The user strikes the target with a burning lash. This also lowers the target's Defense stat.
        """
        pass
