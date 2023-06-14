from ..move import Move
from waifu_types.type import Type

class G-MaxSnooze(Move):
    def __init__(self):
        super().__init__("G-Max Snooze", type=Type.DARK, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Grimmsnarl-exclusive G-Max Move. Makes opponents drowsy.
        """
        pass
