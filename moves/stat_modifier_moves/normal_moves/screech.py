from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Screech(Move):
    def __init__(self):
        super().__init__(
            "Screech",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=85,
            pp=40,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply lowers opponent's Defense.
        """

        if waifu_reciver.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_def -= 2
            multiplier = 2 / (abs(waifu_reciver.stat_stage_def) + 2)
            waifu_reciver.defense = waifu_reciver.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")
