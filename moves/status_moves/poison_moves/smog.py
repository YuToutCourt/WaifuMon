from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.poison import Poison

class Smog(Move):
    def __init__(self):
        super().__init__(
            "Smog",
            type=TypeFactory.create_type(Types.POISON),
            power=30,
            accuracy=70,
            pp=20,
            priority=0,
            proba_effect=40,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May poison opponent.
        """
        waifu_receiver.status = Poison(waifu_receiver)
        log("Smog", f"{waifu_receiver.name} is poisoned!")
