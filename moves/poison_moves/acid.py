from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Acid(Move):
    def __init__(self):
        super().__init__(
            "Acid",
            type=TypeFactory.create_type(Types.POISON),
            power=40,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May lower opponent's Defense.
        """
        if waifu_receiver.stat_stage_def <= -6:
            log(self.name, waifu_receiver.name, "cannot go lower")
            return
        waifu_receiver.stat_stage_def -= 1
        multiplier = 2 / 2 + abs(waifu_receiver.stat_stage_def)
        waifu_receiver.defense = int(waifu_receiver.base_defense * multiplier)
        log(self.name, waifu_receiver.name, "Defense fell")
