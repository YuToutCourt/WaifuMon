from ..move import Move
from waifu_types.type import Type

class VitalThrow(Move):
    def __init__(self):
        super().__init__("Vital Throw", type=Type.FIGHTING, power=70, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User attacks last, but ignores Accuracy and Evasiveness.
        """
        pass
