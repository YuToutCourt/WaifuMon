from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class Decorate(Move):
    def __init__(self):
        super().__init__(
            "Decorate",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply raises target's Attack.
        """
        

        if waifu_reciver.stat_stage_atk == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_atk += 2
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_atk))
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been raised !")
