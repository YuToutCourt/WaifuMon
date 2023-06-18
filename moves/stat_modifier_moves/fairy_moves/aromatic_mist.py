from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class AromaticMist(Move):
    def __init__(self):
        super().__init__(
            "Aromatic Mist",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Raises Defense of an ally.
        """
        

        if waifu_reciver.stat_stage_def == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Defense can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_def += 1
            multiplier = (abs(waifu_reciver.stat_stage_def) + 2) / 2
            waifu_reciver.defense = waifu_reciver.defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been raised !")
