from .move import Move
from waifu_types.type import Type

class FocusPunch(Move):
    def __init__(self):
        super().__init__("Focus Punch", type=Type.FIGHTING, power=150, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        If the user is hit before attacking, it flinches instead.
        """
        pass
