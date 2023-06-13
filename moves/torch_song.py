from .move import Move
from waifu_types.type import Type

class TorchSong(Move):
    def __init__(self):
        super().__init__("Torch Song", type=Type.FIRE, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises user's Special Attack.
        """
        pass
