from ..move import Move
from waifu_types.type import Type

class ElectroBall(Move):
    def __init__(self):
        super().__init__("Electro Ball", type=Type.ELECTRIC, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The faster the user, the stronger the attack.
        """
        pass
