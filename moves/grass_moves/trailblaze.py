from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Trailblaze(Move):
    def __init__(self):
        super().__init__(
            "Trailblaze",
            type=TypeFactory.create_type(Types.GRASS),
            power=50,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Raises user's Speed.
        """
        if waifu_user.stat_stage_spd < 6:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
            log(waifu_user.name, "Speed rose")
        else:
            log(waifu_user.name, "Speed can't be raised anymore")
