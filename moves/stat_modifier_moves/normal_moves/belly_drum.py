from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class BellyDrum(Move):
    def __init__(self):
        super().__init__(
            "Belly Drum",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        User loses 50% of its max HP, but Attack raises to maximum.
        """

        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk = 6
            multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
            waifu_user.attack = waifu_user.apply_stat_change(waifu_user.base_attack, waifu_user.stat_stage_atk)
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")

        waifu_user.hp = waifu_user.hp / 2
        log("! STAT CHANGE !", f"{waifu_user.name} HP has been lowered !")
