from ..move import Move
from waifu_types.type import Type

class JawLock(Move):
    def __init__(self):
        super().__init__("Jaw Lock", type=Type.DARK, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents user and opponent from switching out.
        """
        pass
