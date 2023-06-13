from .move import Move
from waifu_types.type import Type

class StompingTantrum(Move):
    def __init__(self):
        super().__init__("Stomping Tantrum", type=Type.GROUND, power=75, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Driven by frustration, the user attacks the target. If the user's previous move has failed, the power of this move doubles.
        """
        pass
