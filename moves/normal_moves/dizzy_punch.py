from ..move import Move
from waifu_types.type import Type

class DizzyPunch(Move):
    def __init__(self):
        super().__init__("Dizzy Punch", type=Type.NORMAL, power=70, accuracy=100, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
