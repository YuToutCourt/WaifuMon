from .move import Move
from waifu_types.type import Type

class OrderUp(Move):
    def __init__(self):
        super().__init__("Order Up", type=Type.DRAGON, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
