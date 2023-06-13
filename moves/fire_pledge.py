from .move import Move
from waifu_types.type import Type

class FirePledge(Move):
    def __init__(self):
        super().__init__("Fire Pledge", type=Type.FIRE, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Added effects appear if combined with Grass Pledge or Water Pledge.
        """
        pass
