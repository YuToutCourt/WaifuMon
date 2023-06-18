from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class SpicyExtract(Move):
    def __init__(self):
        super().__init__(
            "Spicy Extract",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Harshly lowers the opponent's Defense and sharply raises their Attack.
        """
        

        if waifu_reciver.stat_stage_def == -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_def -= 2
            multiplier = 2 / (abs(waifu_reciver.stat_stage_def) + 2)
            waifu_reciver.defense = waifu_reciver.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")

        if waifu_reciver.stat_stage_atk == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Attack can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_atk += 2
            multiplier = 2 / (abs(waifu_reciver.stat_stage_atk) + 2)
            waifu_reciver.attack = waifu_reciver.base_attack * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Attack has been raised !")
