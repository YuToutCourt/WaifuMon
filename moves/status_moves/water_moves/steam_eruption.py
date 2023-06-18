from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class SteamEruption(Move):
    def __init__(self):
        super().__init__(
            "Steam Eruption",
            type=TypeFactory.create_type(Types.WATER),
            power=110,
            accuracy=95,
            pp=5,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Steam Eruption", f"{waifu_receiver.name} is burned!")
