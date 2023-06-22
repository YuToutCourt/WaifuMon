from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Superpower(Move):
    def __init__(self):
        super().__init__(
            "Superpower",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers user's Attack and Defense.
        """

        if waifu_user.stat_stage_atk <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Attack can't be lowered anymore !")

        else:
            waifu_user.stat_stage_atk -= 1
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_atk))
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been lowered !")

        if waifu_user.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_user.stat_stage_def -= 1
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_def))
            waifu_user.defense = waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")
