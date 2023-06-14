from ..move import Move
from waifu_types.type import Type

class DragonHammer(Move):
    def __init__(self):
        super().__init__("Dragon Hammer", type=Type.DRAGON, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The user uses its body like a hammer to attack the target and inflict damage.
        """
        pass
