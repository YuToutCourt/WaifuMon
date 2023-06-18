from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class FilletAway(Move):
    def __init__(self):
        super().__init__(
            "Fillet Away",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers HP but sharply boosts Attack, and Speed.
        """
        

        if waifu_reciver.stat_stage_atk == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")

        if waifu_reciver.stat_stage_spd == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Speed can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_atk += 2
            waifu_reciver.stat_stage_spd += 2
            multiplier = 2 / (abs(waifu_reciver.stat_stage_atk) + 2)
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            multiplier = 2 / (abs(waifu_reciver.stat_stage_spd) + 2)
            waifu_reciver.speed = waifu_reciver.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack and Speed have been raised !")
            waifu_reciver.hp -= waifu_reciver.hp * 0.75
            log("! STAT CHANGE !", f"{waifu_reciver.name} HP has been lowered !")
