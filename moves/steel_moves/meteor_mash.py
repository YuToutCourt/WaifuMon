from ..move import Move
from waifu_types.type import Type

class MeteorMash(Move):
    def __init__(self):
        super().__init__("Meteor Mash", type=Type.STEEL, power=90, accuracy=90, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May raise user's Attack.
        """
        pass
