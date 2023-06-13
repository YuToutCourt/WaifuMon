from .move import Move
from waifu_types.type import Type

class PhotonGeyser(Move):
    def __init__(self):
        super().__init__("Photon Geyser", type=Type.PSYCHIC, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Uses Attack or Special Attack stat, whichever is higher.
        """
        pass
