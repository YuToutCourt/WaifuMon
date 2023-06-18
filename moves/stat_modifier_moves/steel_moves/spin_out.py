from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class SpinOut(Move):
    def __init__(self):
        super().__init__(
            "Spin Out",
            type=TypeFactory.create_type(Types.STEEL),
            power=100,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Harshly lowers user's Speed.
        """
        

        if waifu_user.stat_stage_spd == -6:
            log("TOO LOW", f"{waifu_user.name} Speed can't be lowered anymore !")

        else:
            waifu_user.stat_stage_spd -= 2
            multiplier = 2 / (abs(waifu_user.stat_stage_spd) + 2)
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been lowered !")
