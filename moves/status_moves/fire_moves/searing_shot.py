from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn

class SearingShot(Move):
    def __init__(self):
        super().__init__(
            "Searing Shot",
            type=TypeFactory.create_type(Types.FIRE),
            power=100,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Searing Shot", f"{waifu_receiver.name} is burned!")
