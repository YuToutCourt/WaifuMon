from .move import Move
from waifu_types.type import Type

class EchoedVoice(Move):
    def __init__(self):
        super().__init__("Echoed Voice", type=Type.NORMAL, power=40, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Power increases each turn.
        """
        pass
