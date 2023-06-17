from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class FireBlast(Move):
    def __init__(self):
        super().__init__(
            "Fire Blast",
            type=TypeFactory.create_type(Types.FIRE),
            power=110,
            accuracy=85,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver)
        log("Fire Blast", f"{waifu_receiver.name} is burned!")
