from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis

class FreezeShock(Move):
    def __init__(self):
        super().__init__(
            "Freeze Shock",
            type=TypeFactory.create_type(Types.ICE),
            power=140,
            accuracy=90,
            pp=5,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Charges on first turn, attacks on second. May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is paralyse!")