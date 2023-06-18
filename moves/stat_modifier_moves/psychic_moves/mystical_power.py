from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class MysticalPower(Move):
    def __init__(self):
        super().__init__(
            "Mystical Power",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=70,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Attack or Defense.
        """
        

        if waifu_user.stat_stage_atk == 6 and waifu_user.stat_stage_def == 6:
            log("TOO HIGH", f"{waifu_user.name} Attack and Defense can't be raised anymore !")

        else:
            if waifu_user.stat_stage_atk >= waifu_user.stat_stage_def:
                waifu_user.stat_stage_atk += 1
                multiplier = 2 / (abs(waifu_user.stat_stage_atk) + 2)
                waifu_user.attack = waifu_user.base_attack * multiplier
                log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
            else:
                waifu_user.stat_stage_def += 1
                multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
                waifu_user.defense = waifu_user.base_defense * multiplier
                log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")
