from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_damage

class SeismicToss(Move):
    def __init__(self):
        super().__init__(
            "Seismic Toss",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Inflicts damage equal to user's level.
        """
        animation_damage(waifu_receiver, waifu_user.level)
        log(
            "Seismic Toss",
            f"{waifu_user.name} inflicted {waifu_user.level} damage to {waifu_receiver.name}",
        )
