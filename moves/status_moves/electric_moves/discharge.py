from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.paralysis import Paralysis

class Discharge(Move):
    def __init__(self):
        super().__init__(
            "Discharge",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log("Discharge", f"{waifu_reciver.name} is paralyse!")
