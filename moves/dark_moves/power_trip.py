from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class PowerTrip(Move):
    def __init__(self):
        super().__init__(
            "Power Trip",
            type=TypeFactory.create_type(Types.DARK),
            power=20,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The user boasts its strength and attacks the target. The more the user's stats are raised, the greater the move's power.
        """
        self.power = 20 + (20 * abs(waifu_user.stat_stage_def + waifu_user.stat_stage_atk + waifu_user.stat_stage_spd))
        log(self.name, f"Power is now {self.power}")

