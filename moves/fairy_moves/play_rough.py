from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class PlayRough(Move):
    def __init__(self):
        super().__init__(
            "Play Rough",
            type=TypeFactory.create_type(Types.FAIRY),
            power=90,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May lower opponent's Attack.
        """
        if waifu_receiver.stat_stage_atk <= -6:
            log(waifu_receiver.name, "can't have its Attack lowered anymore")
        else:
            waifu_receiver.stat_stage_atk -= 1
            multiplier = 2 / (abs(waifu_receiver.stat_stage_atk) + 2)
            waifu_receiver.attack = int(waifu_receiver.base_attack * multiplier)
            log(waifu_receiver.name, "Attack was lowered by 1 stage")
