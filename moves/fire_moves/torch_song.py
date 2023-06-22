from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class TorchSong(Move):
    def __init__(self):
        super().__init__(
            "Torch Song",
            type=TypeFactory.create_type(Types.FIRE),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Raises user's Attack.
        """
        if waifu_user.stat_stage_atk >= 6:
            log(waifu_user.name, "attack can't be boosted anymore")
        else:
            waifu_user.stat_stage_atk += 1
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log(waifu_user.name, "Attack was boosted by 1 stage")
