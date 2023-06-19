from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn


class BurningJealousy(Move):
    def __init__(self):
        super().__init__(
            "Burning Jealousy",
            type=TypeFactory.create_type(Types.FIRE),
            power=70,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Burns any that have had their stats boosted.
        """
        if (
            waifu_receiver.stat_stage_atk > 0
            or waifu_receiver.stat_stage_def > 0
            or waifu_receiver.stat_stage_spd > 0
        ):
            waifu_receiver.status = Burn(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is burned")
