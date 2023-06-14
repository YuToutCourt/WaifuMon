from ..move import Move
from waifu_types.type import Type

class Baby-DollEyes(Move):
    def __init__(self):
        super().__init__("Baby-Doll Eyes", type=Type.FAIRY, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Always goes first. Lowers the target's attack.
        """
        pass
