from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class BlazeKick(Move):
    def __init__(self):
        super().__init__(
            "Blaze Kick",
            type=TypeFactory.create_type(Types.FIRE),
            power=85,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        High critical hit ratio. May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Blaze Kick", f"{waifu_receiver.name} is burned!")
