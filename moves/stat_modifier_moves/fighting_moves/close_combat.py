from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class CloseCombat(Move):
    def __init__(self):
        super().__init__(
            "Close Combat",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers user's Defense.
        """

        if waifu_user.stat_stage_def == -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_user.stat_stage_def -= 1
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_def))
            waifu_user.defense = waifu_user.defense * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Defense has been lowered !")
