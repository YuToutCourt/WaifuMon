from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class ChargeBeam(Move):
    def __init__(self):
        super().__init__(
            "Charge Beam",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=50,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=70,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May raise user's Attack.
        """
        if waifu_user.stat_stage_atk >= 6:
            log("Too high!", waifu_user.name, "Attack can't go any higher")

        else:
            waifu_user.stat_stage_atk += 1
            log(waifu_user.name, "Attack rose by 1 stage")
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
