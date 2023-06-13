from .move import Move
from waifu_types.type import Type

class SkillSwap(Move):
    def __init__(self):
        super().__init__("Skill Swap", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user swaps Abilities with the opponent.
        """
        pass
