from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class SpringtideStorm(Move):
    def __init__(self):
        super().__init__(
            "Springtide Storm",
            type=TypeFactory.create_type(Types.FAIRY),
            power=100,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Boosts user's stats, lowers opponent's stats.
        """

        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (2 + abs(waifu_user.stat_stage_atk)) / 2
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")

        if waifu_user.stat_stage_def >= 6:
            log("TOO HIGH", f"{waifu_user.name} Defense can't be raised anymore !")

        else:
            waifu_user.stat_stage_def += 1
            multiplier = (2 + abs(waifu_user.stat_stage_def)) / 2
            waifu_user.defense = waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")

        if waifu_user.stat_stage_spd >= 6:
            log(
                "TOO HIGH",
                f"{waifu_user.name} Special Defense can't be raised anymore !",
            )

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (2 + abs(waifu_user.stat_stage_spd)) / 2
            waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
            log("! STAT CHANGE !", f"{waifu_user.name} speed has been raised !")

        if waifu_reciver.stat_stage_atk <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Attack can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_atk -= 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_atk))
            waifu_reciver.attack = waifu_reciver.apply_stat_change(waifu_reciver.base_attack, waifu_reciver.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been lowered !")

        if waifu_reciver.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_def -= 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_def))
            waifu_reciver.defense = waifu_reciver.apply_stat_change(waifu_reciver.base_defense, waifu_reciver.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")

        if waifu_reciver.stat_stage_spd <= -6:
            log(
                "TOO LOW",
                f"{waifu_reciver.name} Special Defense can't be lowered anymore !",
            )

        else:
            waifu_reciver.stat_stage_spd -= 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_spd))
            waifu_reciver.speed = waifu_reciver.apply_stat_change(waifu_reciver.base_speed, waifu_reciver.stat_stage_spd)
            log("! STAT CHANGE !", f"{waifu_reciver.name} speed has been lowered !")
