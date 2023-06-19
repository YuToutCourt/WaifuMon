from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class NastyPlot(Move):
    def __init__(self):
        super().__init__(
            "Nasty Plot",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply raises user's Attack.
        """

        if waifu_user.stat_stage_atk >= 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 2
            multiplier = (2 + abs(waifu_user.stat_stage_atk)) / 2
            waifu_user.sp_attack = waifu_user.sp_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
