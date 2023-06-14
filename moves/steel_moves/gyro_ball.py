from ..move import Move
from waifu_types.type import Type

class GyroBall(Move):
    def __init__(self):
        super().__init__("Gyro Ball", type=Type.STEEL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The slower the user, the stronger the attack.
        """
        pass
