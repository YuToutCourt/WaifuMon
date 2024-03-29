from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class SandAttack(Move):
    def __init__(self):
        super().__init__(
            "Sand Attack",
            type=TypeFactory.create_type(Types.GROUND),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers opponent's Speed.
        """

        if waifu_reciver.stat_stage_spd <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Speed can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_spd -= 1
            multiplier = 2 / (abs(waifu_reciver.stat_stage_spd) + 2)
            waifu_reciver.speed = waifu_reciver.apply_stat_change(waifu_reciver.base_speed, waifu_reciver.stat_stage_spd)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been lowered !")
