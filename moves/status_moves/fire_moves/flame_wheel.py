from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class FlameWheel(Move):
    def __init__(self):
        super().__init__(
            "Flame Wheel",
            type=TypeFactory.create_type(Types.FIRE),
            power=60,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Flame Wheel", f"{waifu_receiver.name} is burned!")
