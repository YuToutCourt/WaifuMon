from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Protect(Move):
    def __init__(self):
        super().__init__(
            "Protect",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Raises the user's Defense by 2 stage.
        """

        if waifu_user.stat_stage_def >= 6:
            log(f"{waifu_user.name}'s Defense can't go any higher!")

        else:
            waifu_user.stat_stage_def += 2
            log(f"{waifu_user.name}'s Defense rose by 2 stage!")
            multiplier = (2 + abs(waifu_user.stat_stage_def)) / 2
            waifu_user.defense = waifu_user.defense_base * multiplier
