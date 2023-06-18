from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class SilkTrap(Move):
    def __init__(self):
        super().__init__(
            "Silk Trap",
            type=TypeFactory.create_type(Types.BUG),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Protects the user and lowers opponent's Speed on contact.
        """
        

        if waifu_reciver.stat_stage_spd == -6:
            log("TOO LOW", f"{waifu_reciver.name} Speed can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_spd -= 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_spd))
            waifu_reciver.speed = waifu_reciver.base_speed * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Speed has been lowered !")
