from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class RapidSpin(Move):
    def __init__(self):
        super().__init__(
            "Rapid Spin",
            type=TypeFactory.create_type(Types.NORMAL),
            power=50,
            accuracy=100,
            pp=40,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Speed and removes entry hazards and trap move effects.
        """
        

        if waifu_user.stat_stage_spd == 6:
            log("TOO HIGH", f"{waifu_user.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = 2 / (abs(waifu_user.stat_stage_spd) + 2)
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been raised !")
