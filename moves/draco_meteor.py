from .move import Move
from waifu_types.type import Type

class DracoMeteor(Move):
    def __init__(self):
        super().__init__("Draco Meteor", type=Type.DRAGON, power=130, accuracy=90, pp=5, proba_effect=100)

    def effect(self):
        """
        Sharply lowers user's Special Attack.
        """
        pass
