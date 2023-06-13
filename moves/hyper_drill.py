from .move import Move
from waifu_types.type import Type

class HyperDrill(Move):
    def __init__(self):
        super().__init__("Hyper Drill", type=Type.NORMAL, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Can strike through Protect/Detect.
        """
        pass
