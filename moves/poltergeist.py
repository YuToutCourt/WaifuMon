from .move import Move
from waifu_types.type import Type

class Poltergeist(Move):
    def __init__(self):
        super().__init__("Poltergeist", type=Type.GHOST, power=110, accuracy=90, pp=5, proba_effect=100)

    def effect(self):
        """
        Fails if the target doesn’t have an item.
        """
        pass
