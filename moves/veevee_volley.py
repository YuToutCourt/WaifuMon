from .move import Move
from waifu_types.type import Type

class VeeveeVolley(Move):
    def __init__(self):
        super().__init__("Veevee Volley", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Power increases when player's bond is stronger.
        """
        pass
