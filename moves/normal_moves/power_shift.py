from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class PowerShift(Move):
    def __init__(self):
        super().__init__(
            "Power Shift",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Switches offensive and defensive stats.
        """
        waifu_user.stat_stage_atk, waifu_user.stat_stage_de = (
            waifu_user.stat_stage_def,
            waifu_user.stat_stage_atk,
        )
        waifu_user.attack, waifu_user.defense = waifu_user.defense, waifu_user.attack

        log(self.name, f"{waifu_user.name} have swap his atk with his def")
