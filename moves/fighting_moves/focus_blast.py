from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class FocusBlast(Move):
    def __init__(self):
        super().__init__(
            "Focus Blast",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=120,
            accuracy=70,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May lower opponent's Defense.
        """
        if waifu_receiver.stat_stage_def <= -6:
            log(waifu_receiver.name, "can't have its Defense lowered anymore")
        else:
            waifu_receiver.stat_stage_def -= 1
            multiplier = 2 / (abs(waifu_receiver.stat_stage_def) + 2)
            waifu_receiver.defense = waifu_receiver.base_defense * multiplier
            log(waifu_receiver.name, "Defense was lowered by 1 stage")
