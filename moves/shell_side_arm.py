from .move import Move
from waifu_types.type import Type

class ShellSideArm(Move):
    def __init__(self):
        super().__init__("Shell Side Arm", type=Type.POISON, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        May poison opponent. Inflicts either Special or Physical damage, whichever is better.
        """
        pass
