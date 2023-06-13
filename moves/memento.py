from .move import Move
from waifu_types.type import Type

class Memento(Move):
    def __init__(self):
        super().__init__("Memento", type=Type.DARK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User faints, sharply lowers opponent's Attack and Special Attack.
        """
        pass
