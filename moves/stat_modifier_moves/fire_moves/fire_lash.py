from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class FireLash(Move):
    def __init__(self):
        super().__init__(
            "Fire Lash",
            type=TypeFactory.create_type(Types.FIRE),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        The user strikes the target with a burning lash. This also lowers the target's Defense stat.
        """
        

        if waifu_reciver.stat_stage_def == -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_def -= 1
            multiplier = 2 / (abs(waifu_reciver.stat_stage_def) + 2)
            waifu_reciver.defense = waifu_reciver.defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")
