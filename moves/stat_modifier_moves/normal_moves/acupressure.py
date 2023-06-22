from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Acupressure(Move):
    def __init__(self):
        super().__init__(
            "Acupressure",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply raises a random stat.
        """
        from random import choice

        stats = [
            waifu_user.stat_stage_atk,
            waifu_user.stat_stage_def,
            waifu_user.stat_stage_spd,
        ]
        stat = choice(stats)

        if stat >= 6:
            log("TOO HIGH", f"{waifu_user.name} {stat} can't be raised anymore !")

        else:
            stat += 2
            multiplier = (abs(stat) + 2) / 2
            if stat == waifu_user.stat_stage_atk:
                waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
                log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
            elif stat == waifu_user.stat_stage_def:
                waifu_user.defense = waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def)
                log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")
            elif stat == waifu_user.stat_stage_spd:
                waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
                log("! STAT CHANGE !", f"{waifu_user.name} Speed has been raised !")
