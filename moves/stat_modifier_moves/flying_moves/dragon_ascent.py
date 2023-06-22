from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class DragonAscent(Move):
    def __init__(self):
        super().__init__(
            "Dragon Ascent",
            type=TypeFactory.create_type(Types.FLYING),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers user's Defense.
        """

        if waifu_user.stat_stage_atk <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Attack can't be lowered anymore !")

        else:
            waifu_user.stat_stage_atk -= 1
            multiplier = 2 / (abs(waifu_user.stat_stage_atk) + 2)
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been lowered !")

        if waifu_user.stat_stage_spd <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Speed can't be lowered anymore !")

        else:
            waifu_user.stat_stage_spd -= 1
            multiplier = 2 / (abs(waifu_user.stat_stage_spd) + 2)
            waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been lowered !")
