from ..move import Move
from waifu_types.type import Type

class DevastatingDrake(Move):
    def __init__(self):
        super().__init__("Devastating Drake", type=Type.DRAGON, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Dragon type Z-Move.
        """
        pass
