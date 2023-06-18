from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.freeze import Freeze

class Blizzard(Move):
    def __init__(self):
        super().__init__(
            "Blizzard",
            type=TypeFactory.create_type(Types.ICE),
            power=110,
            accuracy=70,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May freeze opponent.
        """
        waifu_reciver.status = Freeze(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is now freeze!")

