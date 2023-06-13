from .move import Move
from waifu_types.type import Type

class DisarmingVoice(Move):
    def __init__(self):
        super().__init__("Disarming Voice", type=Type.FAIRY, power=40, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass
