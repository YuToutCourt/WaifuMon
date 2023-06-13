from .move import Move
from waifu_types.type import Type

class Facade(Move):
    def __init__(self):
        super().__init__("Facade", type=Type.NORMAL, power=70, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Power doubles if user is burned, poisoned, or paralyzed.
        """
        pass
