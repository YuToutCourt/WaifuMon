from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Haze(Move):
    def __init__(self):
        super().__init__(
            "Haze",
            type=TypeFactory.create_type(Types.ICE),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Resets all stat changes.
        """
        waifu_user.stat_stage_atk = 0
        waifu_user.stat_stage_def = 0
        waifu_user.stat_stage_spd = 0
        waifu_user.attack = waifu_user.base_attack
        waifu_user.defense = waifu_user.base_defense
        waifu_user.speed = waifu_user.base_speed

        log(waifu_user.name, "stat changes were removed")

        waifu_receiver.stat_stage_atk = 0
        waifu_receiver.stat_stage_def = 0
        waifu_receiver.stat_stage_spd = 0
        waifu_receiver.attack = waifu_receiver.base_attack
        waifu_receiver.defense = waifu_receiver.base_defense
        waifu_receiver.speed = waifu_receiver.base_speed

        log(waifu_receiver.name, "stat changes were removed")
