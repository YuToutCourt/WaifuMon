from ..move import Move
from waifu_types.type import Type

class BlueFlare(Move):
    def __init__(self):
        super().__init__("Blue Flare", type=Type.FIRE, power=130, accuracy=85, pp=5, priority=0, proba_effect=20)

    def effect(self):
        """
        May burn opponent.
        """
        pass
