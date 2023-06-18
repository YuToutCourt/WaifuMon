from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class ThunderousKick(Move):
    def __init__(self):
        super().__init__(
            "Thunderous Kick",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Lowers opponent's Defense.
        """
        if waifu_receiver.stat_stage_def <= -6:
            log(waifu_receiver.name, "defense can't be lowered anymore")
        else:
            waifu_receiver.stat_stage_def -= 1
            multiplier = 2 / (abs(waifu_receiver.stat_stage_def) + 2)
            waifu_receiver.defense = waifu_receiver.base_defense * multiplier
            log(waifu_receiver.name, "Defense was lowered by 1 stage")

