from ..move import Move
from waifu_types.type import Type

class G-MaxChiStrike(Move):
    def __init__(self):
        super().__init__("G-Max Chi Strike", type=Type.FIGHTING, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Machamp-exclusive G-Max Move. Increases critical hit ratio.
        """
        pass
