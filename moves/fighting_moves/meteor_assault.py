from ..move import Move
from waifu_types.type import Type

class MeteorAssault(Move):
    def __init__(self):
        super().__init__("Meteor Assault", type=Type.FIGHTING, power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass
