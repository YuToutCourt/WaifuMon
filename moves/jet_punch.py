from .move import Move
from waifu_types.type import Type

class JetPunch(Move):
    def __init__(self):
        super().__init__("Jet Punch", type=Type.WATER, power=60, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Always goes first.
        """
        pass
