from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class CottonGuard(Move):
    def __init__(self):
        super().__init__(
            "Cotton Guard",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Drastically raises user's Defense.
        """
        

        if waifu_user.stat_stage_def == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Defense can't be raised anymore !")

        else:
            waifu_user.stat_stage_def += 3
            multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
            waifu_user.defense = waifu_user.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been raised !")
