from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn

class WillOWisp(Move):
    def __init__(self):
        super().__init__(
            "Will-O-Wisp",
            type=TypeFactory.create_type(Types.FIRE),
            power=0,
            accuracy=85,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Burns opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Will-O-Wisp", f"{waifu_receiver.name} is burned!")
