from .move import Move
from waifu_types.type import Type

class G-MaxGoldRush(Move):
    def __init__(self):
        super().__init__("G-Max Gold Rush", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Meowth-exclusive G-Max Move. Confuses opponents and earns more money.
        """
        pass
