from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class FleurCannon(Move):
    def __init__(self):
        super().__init__(
            "Fleur Cannon",
            type=TypeFactory.create_type(Types.FAIRY),
            power=130,
            accuracy=90,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply lowers user's Attack.
        """
        

        if waifu_user.stat_stage_atk == -6:
            log("TOO LOW", f"{waifu_user.name} Attack can't be lowered anymore !")

        else:
            waifu_user.stat_stage_atk -= 2
            multiplier = 2 / (2 + abs(waifu_user.stat_stage_atk))
            waifu_user.attack = waifu_user.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Attack has been lowered !")
