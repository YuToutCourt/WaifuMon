from .move import Move
from waifu_types.type import Type

class BurnUp(Move):
    def __init__(self):
        super().__init__("Burn Up", type=Type.FIRE, power=130, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        To inflict massive damage, the user burns itself out. After using this move, the user will no longer be Fire type.
        """
        pass
