from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison

class GunkShot(Move):
    def __init__(self):
        super().__init__(
            "Gunk Shot",
            type=TypeFactory.create_type(Types.POISON),
            power=120,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May poison opponent.
        """
        waifu_receiver.status = Poison(waifu_receiver, True)
        log("Gunk Shot", f"{waifu_receiver.name} is poisoned!")
