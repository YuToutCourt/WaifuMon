from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class DoubleTeam(Move):
    def __init__(self):
        super().__init__(
            "Double Team",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Attack and Speed.
        """

        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")

        if waifu_user.stat_stage_spd >= 6:
            log("TOO HIGH", f"{waifu_user.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been raised !")
