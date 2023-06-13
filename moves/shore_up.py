from .move import Move
from waifu_types.type import Type

class ShoreUp(Move):
    def __init__(self):
        super().__init__("Shore Up", type=Type.GROUND, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        The user regains up to half of its max HP. It restores more HP in a sandstorm.
        """
        pass
