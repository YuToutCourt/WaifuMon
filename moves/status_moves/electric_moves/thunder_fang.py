from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class ThunderFang(Move):
    def __init__(self):
        super().__init__(
            "Thunder Fang",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=65,
            accuracy=95,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log("ThunderFang", f"{waifu_reciver.name} is paralyse!")
