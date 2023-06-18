from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.freeze import Freeze

class FreezeDry(Move):
    def __init__(self):
        super().__init__(
            "Freeze-Dry",
            type=TypeFactory.create_type(Types.ICE),
            power=70,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May freeze opponent.
        """
        waifu_reciver.status = Freeze(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is now freeze!")
