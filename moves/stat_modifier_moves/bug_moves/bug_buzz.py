from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class BugBuzz(Move):
    def __init__(self):
        super().__init__(
            "Bug Buzz",
            type=TypeFactory.create_type(Types.BUG),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )


    def effect(self, waifu_user, waifu_reciver):
        """
        May lower opponent's Defense.
        """
        

        if waifu_reciver.stat_stage_def == -6 :
            log("TOO LOW",f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else :
            waifu_reciver.stat_stage_def -= 1
            multiplier  = 2/(2+abs(waifu_reciver.stat_stage_def))
            waifu_reciver.defense = waifu_reciver.base_defense * multiplier
            log("! STAT CHANGE !",f"{waifu_reciver.name} Defense has been lowered !")




