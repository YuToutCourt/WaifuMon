from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class FlareBlitz(Move):
    def __init__(self):
        super().__init__(
            "Flare Blitz",
            type=TypeFactory.create_type(Types.FIRE),
            power=120,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User receives recoil damage. May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver)
        log("Flare Blitz", f"{waifu_receiver.name} is burned!")
        waifu_user.receive_damage(waifu_user.max_hp * 0.7)
        log("Flare Blitz", f"{waifu_user.name} is hurt by recoil!")
