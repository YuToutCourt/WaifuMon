from .move import Move
from waifu_types.type import Type

class WickedBlow(Move):
    def __init__(self):
        super().__init__("Wicked Blow", type=Type.DARK, power=75, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit and ignores stat changes.
        """
        pass
