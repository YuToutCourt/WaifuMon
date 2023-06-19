from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class SilverWind(Move):
    def __init__(self):
        super().__init__(
            "Silver Wind",
            type=TypeFactory.create_type(Types.BUG),
            power=60,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May raise all stats of user at once.
        """
        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")

        if waifu_user.stat_stage_def >= 6:
            log("TOO HIGH", f"{waifu_user.name} Defense can't be raised anymore !")

        else:
            waifu_user.stat_stage_def += 1
            multiplier = (abs(waifu_user.stat_stage_def) + 2) / 2
            waifu_user.defense = waifu_user.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")

        if waifu_user.stat_stage_spd >= 6:
            log("TOO HIGH", f"{waifu_user.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been raised !")
