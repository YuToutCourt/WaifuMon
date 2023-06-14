from ..move import Move
from waifu_types.type import Type

class PowerGem(Move):
    def __init__(self):
        super().__init__("Power Gem", type=Type.ROCK, power=80, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
