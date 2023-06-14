from ..move import Move
from waifu_types.type import Type

class IceSpinner(Move):
    def __init__(self):
        super().__init__("Ice Spinner", type=Type.ICE, power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Removes effects of Terrain.
        """
        pass
