from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Punishment(Move):
    def __init__(self):
        super().__init__(
            "Punishment",
            type=TypeFactory.create_type(Types.DARK),
            power=10,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Power increases when opponent's stats have been raised.
        """
        self.power = 60 + (
            20
            * abs(
                waifu_receiver.stat_stage_def
                + waifu_receiver.stat_stage_atk
                + waifu_receiver.stat_stage_spd
            )
        )
        log(self.name, f"Power is now {self.power}")
