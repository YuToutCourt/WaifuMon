from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class FlameCharge(Move):
    def __init__(self):
        super().__init__(
            "Flame Charge",
            type=TypeFactory.create_type(Types.FIRE),
            power=50,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Speed.
        """
        

        if waifu_user.stat_stage_spd == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 1
            multiplier = (abs(waifu_user.stat_stage_spd) + 2) / 2
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been raised !")
