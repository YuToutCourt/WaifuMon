from .move import Move
from waifu_types.type import Type

class SleepTalk(Move):
    def __init__(self):
        super().__init__("Sleep Talk", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User performs one of its own moves while sleeping.
        """
        pass
