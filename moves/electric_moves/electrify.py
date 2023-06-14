from ..move import Move
from waifu_types.type import Type

class Electrify(Move):
    def __init__(self):
        super().__init__("Electrify", type=Type.ELECTRIC, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes the target's move to Electric type.
        """
        pass
