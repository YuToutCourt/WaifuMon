from .move import Move
from waifu_types.type import Type

class Submission(Move):
    def __init__(self):
        super().__init__("Submission", type=Type.FIGHTING, power=80, accuracy=80, pp=20, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
