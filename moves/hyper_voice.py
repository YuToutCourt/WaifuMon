from .move import Move
from waifu_types.type import Type

class HyperVoice(Move):
    def __init__(self):
        super().__init__("Hyper Voice", type=Type.NORMAL, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
