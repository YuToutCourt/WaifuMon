from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn


class Scald(Move):
    def __init__(self):
        super().__init__(
            "Scald",
            type=TypeFactory.create_type(Types.WATER),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn opponent.
        """
        waifu_receiver.status = Burn(waifu_receiver, True)
        log("Scald", f"{waifu_receiver.name} is burned!")
