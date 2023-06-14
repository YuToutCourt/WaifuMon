from ..move import Move
from waifu_types.type import Type

class SecretPower(Move):
    def __init__(self):
        super().__init__("Secret Power", type=Type.NORMAL, power=70, accuracy=100, pp=20, priority=0, proba_effect=30)

    def effect(self):
        """
        Effects of the attack vary with the location.
        """
        pass
