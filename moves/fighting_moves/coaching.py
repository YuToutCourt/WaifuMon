from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Coaching(Move):
    def __init__(self):
        super().__init__(
            "Coaching",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Boosts Attack and Defense.
        """
        if waifu_user.stat_stage_atk >= 6:
            log(waifu_user.name, "attack can't be boosted anymore")
        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = int(waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk))
            log(waifu_user.name, "Attack was boosted by 1 stage")

        if waifu_user.stat_stage_def >= 6:
            log(waifu_user.name, "defense can't be boosted anymore")

        else:
            waifu_user.stat_stage_def += 1
            multiplier = (abs(waifu_user.stat_stage_def) + 2) / 2
            waifu_user.defense = int(waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def))
            log(waifu_user.name, "Defense was boosted by 1 stage")
