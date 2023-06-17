from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.burn import Burn

class BlueFlare(Move):
    def __init__(self):
        super().__init__(
            "Blue Flare",
            type=TypeFactory.create_type(Types.FIRE),
            power=130,
            accuracy=85,
            pp=5,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver)
        log("Blue Flare", f"{waifu_receiver.name} is burned!")
