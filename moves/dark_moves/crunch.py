from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Crunch(Move):
    def __init__(self):
        super().__init__(
            "Crunch",
            type=TypeFactory.create_type(Types.DARK),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May lower opponent's Defense.
        """
        if waifu_receiver.stat_stage_def > -6:
            waifu_receiver.stat_stage_def -= 1
            multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
            waifu_receiver.defense = waifu_receiver.base_defense * multiplier
            log(self.name, waifu_receiver.name, "Defense fell")
        else:
            log(self.name, waifu_receiver.name, "Defense won't go any lower")
