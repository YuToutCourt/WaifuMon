from ..move import Move
from waifu_types.type import Type

class VoltSwitch(Move):
    def __init__(self):
        super().__init__("Volt Switch", type=Type.ELECTRIC, power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User must switch out after attacking.
        """
        pass
