from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class FireFang(Move):
    def __init__(self):
        super().__init__(
            "Fire Fang",
            type=TypeFactory.create_type(Types.FIRE),
            power=65,
            accuracy=95,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May cause flinching and/or burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver)
        log("Fire Fang", f"{waifu_receiver.name} is burned!")
