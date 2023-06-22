from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class ArmorCannon(Move):
    def __init__(self):
        super().__init__(
            "Armor Cannon",
            type=TypeFactory.create_type(Types.FIRE),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Lowers user's Defense.
        """

        if waifu_user.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_user.stat_stage_def -= 1
            multiplier = 2 / (abs(waifu_user.stat_stage_def) + 2)
            waifu_user.defense = waifu_user.apply_stat_change(waifu_user.base_defense, waifu_user.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")
