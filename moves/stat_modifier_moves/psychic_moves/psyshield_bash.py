from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class PsyshieldBash(Move):
    def __init__(self):
        super().__init__(
            "Psyshield Bash",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=70,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises user's Defense.
        """
        

        if waifu_user.stat_stage_def == 6:
            log("TOO HIGH", f"{waifu_user.name} Defense can't be raised anymore !")

        else:
            waifu_user.stat_stage_def += 1
            multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
            waifu_user.defense = waifu_user.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_user.name} Defense has been raised !")
