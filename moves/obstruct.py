from .move import Move
from waifu_types.type import Type

class Obstruct(Move):
    def __init__(self):
        super().__init__("Obstruct", type=Type.DARK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the user and sharply lowers Defence on contact.
        """
        pass
