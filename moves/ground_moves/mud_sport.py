from ..move import Move
from waifu_types.type import Type

class MudSport(Move):
    def __init__(self):
        super().__init__("Mud Sport", type=Type.GROUND, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Weakens the power of Electric-type moves.
        """
        pass
