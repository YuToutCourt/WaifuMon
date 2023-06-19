from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison

class ToxicThread(Move):
    def __init__(self):
        super().__init__(
            "Toxic Thread",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Poisons opponent and lowers its Speed.
        """
            
        if waifu_reciver.status is not None:
            log("Already get status", f"{waifu_reciver.name} already get status !")

        else:
            waifu_reciver.status = Poison
            log("! STATUS CHANGE !", f"{waifu_reciver.name} has been poisoned !")

        if waifu_reciver.stat_stage_spd <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Speed can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_spd -= 1
            multiplier = 2 / (abs(waifu_reciver.stat_stage_spd) + 2)
            waifu_reciver.speed = waifu_reciver.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been lowered !")
