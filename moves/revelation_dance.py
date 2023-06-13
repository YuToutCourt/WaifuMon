from .move import Move
from waifu_types.type import Type

class RevelationDance(Move):
    def __init__(self):
        super().__init__("Revelation Dance", type=Type.NORMAL, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Type changes based on Oricorio's form.
        """
        pass
