from .move import Move
from waifu_types.type import Type

class AromaticMist(Move):
    def __init__(self):
        super().__init__("Aromatic Mist", type=Type.FAIRY, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Raises Special Defense of an ally.
        """
        pass
