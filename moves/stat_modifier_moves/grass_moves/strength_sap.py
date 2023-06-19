from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class StrengthSap(Move):
    def __init__(self):
        super().__init__(
            "Strength Sap",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        The user restores its HP by the same amount as the target's Attack stat. It also lowers the target's Attack stat.
        """

        attack_stat = waifu_reciver.attack
        if waifu_user.hp + attack_stat > waifu_user.hp_max:
            waifu_user.hp = waifu_user.hp_max
        else:
            waifu_user.hp += attack_stat

        if waifu_reciver.stat_stage_atk <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Attack can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_atk -= 1
            multiplier = 2 / (abs(waifu_reciver.stat_stage_atk) + 2)
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been lowered !")
