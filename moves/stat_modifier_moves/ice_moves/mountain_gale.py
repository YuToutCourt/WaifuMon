from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class MountainGale(Move):
    def __init__(self):
        super().__init__(
            "Mountain Gale",
            type=TypeFactory.create_type(Types.ICE),
            power=100,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers user's Speed.
        """
        

        if waifu_user.stat_stage_spd == -6:
            log("TOO LOW", f"{waifu_user.name} Speed can't be lowered anymore !")

        else:
            waifu_user.stat_stage_spd -= 1
            multiplier = 2 / (abs(waifu_user.stat_stage_spd) + 2)
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been lowered !")
