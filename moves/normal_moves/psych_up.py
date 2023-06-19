from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class PsychUp(Move):
    def __init__(self):
        super().__init__(
            "Psych Up",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Copies the opponent's stat changes.
        """
        waifu_user.stat_stage_atk = waifu_receiver.stat_stage_atk
        waifu_user.stat_stage_def = waifu_receiver.stat_stage_def
        waifu_user.stat_stage_spd = waifu_receiver.stat_stage_spd

        if waifu_user.stat_stage_atk > 0:
            multiplier = (2 + waifu_user.stat_stage_atk) / 2
            waifu_user.attack = waifu_user.attack_base * multiplier
        elif waifu_user.stat_stage_atk < 0:
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_atk))
            waifu_user.attack = waifu_user.attack_base * multiplier
        
        if waifu_user.stat_stage_def > 0:
            multiplier = (2 + waifu_user.stat_stage_def) / 2
            waifu_user.defense = waifu_user.defense_base * multiplier
        elif waifu_user.stat_stage_def < 0:
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_def))
            waifu_user.defense = waifu_user.defense_base * multiplier

        if waifu_user.stat_stage_spd > 0:
            multiplier = (2 + waifu_user.stat_stage_spd) / 2
            waifu_user.speed = waifu_user.speed_base * multiplier
        elif waifu_user.stat_stage_spd < 0:
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_spd))
            waifu_user.speed = waifu_user.speed_base * multiplier
