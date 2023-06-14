from ..move import Move
from waifu_types.type import Type

class RolePlay(Move):
    def __init__(self):
        super().__init__("Role Play", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User copies the opponent's Ability.
        """
        pass
