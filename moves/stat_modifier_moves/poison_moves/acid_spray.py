from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class AcidSpray(Move):
    def __init__(self):
        super().__init__(
            "Acid Spray",
            type=TypeFactory.create_type(Types.POISON),
            power=40,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Sharply lowers opponent's Defense.
        """

        if waifu_reciver.stat_stage_def <= -6:
            log("TOO LOW", f"{waifu_reciver.name} Defense can't be lowered anymore !")

        else:
            waifu_reciver.stat_stage_def -= 2
            multiplier = 2 / (abs(waifu_reciver.stat_stage_def) + 2)
            waifu_reciver.defense = waifu_reciver.apply_stat_change(waifu_reciver.base_defense, waifu_reciver.stat_stage_def)
            log("! STAT CHANGE !", f"{waifu_reciver.name} Defense has been lowered !")
