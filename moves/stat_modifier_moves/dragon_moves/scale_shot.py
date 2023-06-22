from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class ScaleShot(Move):
    def __init__(self):
        super().__init__(
            "Scale Shot",
            type=TypeFactory.create_type(Types.DRAGON),
            power=25,
            accuracy=90,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Boosts user's Speed but lowers its Defense.
        """

        if waifu_user.stat_stage_spd >= 6:
            log("TOO HIGH", f"{waifu_user.name} Speed can't be boosted anymore !")

        elif waifu_user.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_user.name} Defense can't be lowered anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            waifu_user.stat_stage_def -= 1
            multiplier_spd = (2 + abs(waifu_user.stat_stage_spd)) / 2
            multiplier_def = 2 / (2 + abs(waifu_user.stat_stage_def))
            waifu_user.speed = waifu_user.apply_stat_change(waifu_user.base_speed, waifu_user.stat_stage_spd)
            waifu_user.defense = waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been boosted !")
            log("! STAT CHANGE !", f"{waifu_user.name} Defense has been lowered !")
