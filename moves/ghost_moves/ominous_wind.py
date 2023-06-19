from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class OminousWind(Move):
    def __init__(self):
        super().__init__(
            "Ominous Wind",
            type=TypeFactory.create_type(Types.GHOST),
            power=60,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May raise all user's stats at once.
        """
        if waifu_user.stat_stage_atk >= 6:
            log(waifu_user.name, "attack can't be boosted anymore")
        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.base_attack * multiplier
            log(waifu_user.name, "Attack was boosted by 1 stage")

        if waifu_user.stat_stage_def >= 6:
            log(waifu_user.name, "defense can't be boosted anymore")
        else:
            waifu_user.stat_stage_def += 1
            multiplier = (abs(waifu_user.stat_stage_def) + 2) / 2
            waifu_user.defense = waifu_user.base_defense * multiplier
            log(waifu_user.name, "Defense was boosted by 1 stage")

        if waifu_user.stat_stage_spd >= 6:
            log(waifu_user.name, "speed can't be boosted anymore")
        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.base_speed * multiplier
            log(waifu_user.name, "Speed was boosted by 1 stage")
