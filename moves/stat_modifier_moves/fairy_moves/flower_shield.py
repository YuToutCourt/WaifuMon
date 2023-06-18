from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class FlowerShield(Move):
    def __init__(self):
        super().__init__(
            "Flower Shield",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply raises Defense of all Grass-type Pokemon on the field.
        """
        

        if waifu_reciver.stat_stage_def == 6:
            log("TOO HIGH", f"{waifu_reciver.name} Defense can't be raised anymore !")

        else:
            waifu_reciver.stat_stage_def += 2
            multiplier = 2 / (2 + abs(waifu_reciver.stat_stage_def))
            waifu_reciver.defense = waifu_reciver.base_defense * multiplier
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been raised !")
