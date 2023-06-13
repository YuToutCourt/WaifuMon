from .move import Move
from waifu_types.type import Type

class IceHammer(Move):
    def __init__(self):
        super().__init__("Ice Hammer", type=Type.ICE, power=100, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        The user swings and hits with its strong, heavy fist. It lowers the user's Speed, however.
        """
        pass
