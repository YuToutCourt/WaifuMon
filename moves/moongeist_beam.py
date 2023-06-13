from .move import Move
from waifu_types.type import Type

class MoongeistBeam(Move):
    def __init__(self):
        super().__init__("Moongeist Beam", type=Type.GHOST, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Ignores the target's ability.
        """
        pass
