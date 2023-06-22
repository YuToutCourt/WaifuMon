from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class SpiritBreak(Move):
    def __init__(self):
        super().__init__(
            "Spirit Break",
            type=TypeFactory.create_type(Types.FAIRY),
            power=75,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers opponent's Attack.
        """

        if waifu_reciver.stat_stage_atk <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Attack can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_atk -= 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_atk))
            waifu_reciver.attack = waifu_reciver.apply_stat_change(waifu_reciver.base_attack, waifu_reciver.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been lowered !")
