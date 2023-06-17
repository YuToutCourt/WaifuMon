from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class SkullBash(Move):
    def __init__(self):
        super().__init__(
            "Skull Bash",
            type=TypeFactory.create_type(Types.NORMAL),
            power=130,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises Defense or Attack.
        """
        import random

        

        if random.randint(0, 1) == 0:
            if waifu_user.stat_stage_def == 6:
                log("TOO HIGH", f"{waifu_user.name} Defense can't be raised anymore !")

            else:
                waifu_user.stat_stage_def += 1
                multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
                waifu_user.defense = waifu_user.defense * multiplier
                log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")

        else:
            if waifu_user.stat_stage_atk == 6:
                log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

            else:
                waifu_user.stat_stage_atk += 1
                multiplier = 2 / (abs(waifu_user.stat_stage_atk) + 2)
                waifu_user.attack = waifu_user.attack * multiplier
                log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
        
