from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class PowerUpPunch(Move):
    def __init__(self):
        super().__init__(
            "Power-Up Punch",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=40,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises Attack.
        """
        

        if waifu_user.stat_stage_atk == 6:
            log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

        else:
            waifu_user.stat_stage_atk += 1
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_atk))
            waifu_user.attack = waifu_user.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
