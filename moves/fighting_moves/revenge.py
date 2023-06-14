from ..move import Move
from waifu_types.type import Type

class Revenge(Move):
    def __init__(self):
        super().__init__("Revenge", type=Type.FIGHTING, power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases if user was hit first.
        """
        pass
