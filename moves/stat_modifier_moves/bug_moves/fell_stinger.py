from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class FellStinger(Move):
    def __init__(self):
        super().__init__(
            "Fell Stinger",
            type=TypeFactory.create_type(Types.BUG),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Drastically raises user's Attack if target is KO'd.
        """


        if waifu_reciver.is_ko:
            if waifu_user.stat_stage_atk == 6:
                log("TOO HIGH", f"{waifu_user.name} Attack can't be raised anymore !")

            else:
                waifu_user.stat_stage_atk += 2
                multiplier = (abs(waifu_user.stat_stage_atk) + 2) / 2
                waifu_user.attack = waifu_user.base_attack * multiplier
                log("! STAT CHANGE !", f"{waifu_user.name} Attack has been raised !")
