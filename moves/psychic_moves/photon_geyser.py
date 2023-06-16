from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PhotonGeyser(Move):
    def __init__(self):
        super().__init__(
            "Photon Geyser",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=100,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Uses Attack or Special Attack stat, whichever is higher.
        """
        pass
