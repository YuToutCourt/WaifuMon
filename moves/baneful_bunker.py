from .move import Move
from waifu_types.type import Type

class BanefulBunker(Move):
    def __init__(self):
        super().__init__("Baneful Bunker", type=Type.POISON, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the user and poisons opponent on contact.
        """
        pass
