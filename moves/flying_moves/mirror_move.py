from ..move import Move
from waifu_types.type import Type

class MirrorMove(Move):
    def __init__(self):
        super().__init__("Mirror Move", type=Type.FLYING, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User performs the opponent's last move.
        """
        pass
