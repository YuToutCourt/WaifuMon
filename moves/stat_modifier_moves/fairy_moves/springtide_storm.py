from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class SpringtideStorm(Move):
    def __init__(self):
        super().__init__(
            "Springtide Storm",
            type=TypeFactory.create_type(Types.FAIRY),
            power=100,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Boosts user's stats in Incarnate Forme, or lowers opponent's stats in Therian Forme.
        """
        

        if waifu_user.stat_stage_spd == 6:
            log("TOO HIGH", f"{waifu_user.name} Speed can't be raised anymore !")

        else:
            waifu_user.stat_stage_spd += 2
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_spd))
            waifu_user.speed = waifu_user.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Speed has been raised !")
