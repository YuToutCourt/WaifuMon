from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class BoltStrike(Move):
    def __init__(self):
        super().__init__(
            "Bolt Strike",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=130,
            accuracy=85,
            pp=5,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log("BoltStrike", f"{waifu_reciver.name} is paralyse!")
