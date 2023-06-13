from .move import Move
from waifu_types.type import Type

class SpectralThief(Move):
    def __init__(self):
        super().__init__("Spectral Thief", type=Type.GHOST, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user hides in the target's shadow, steals the target's stat boosts, and then attacks.
        """
        pass
