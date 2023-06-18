from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class Flatter(Move):
    def __init__(self):
        super().__init__(
            "Flatter",
            type=TypeFactory.create_type(Types.DARK),
            power=120,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises the opponant's Attack.
        """
        

        if waifu_reciver.stat_stage_atk == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_atk += 1
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_atk))
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been raised !")
