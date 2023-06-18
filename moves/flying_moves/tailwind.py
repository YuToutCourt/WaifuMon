from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Tailwind(Move):
    def __init__(self):
        super().__init__(
            "Tailwind",
            type=TypeFactory.create_type(Types.FLYING),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Doubles Speed.
        """
        if waifu_user.stat_stage_speed >= 6:
            log(waifu_user.name, "speed can't be boosted anymore")
        else:
            waifu_user.stat_stage_speed += 2
            multiplier = (abs(waifu_user.stat_stage_speed) + 2) / 2
            waifu_user.speed = waifu_user.base_speed * multiplier
            log(waifu_user.name, "Speed was boosted by 2 stage")
