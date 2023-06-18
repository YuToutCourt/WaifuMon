from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison

class PoisonTail(Move):
    def __init__(self):
        super().__init__(
            "Poison Tail",
            type=TypeFactory.create_type(Types.POISON),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        High critical hit ratio. May poison opponent.
        """
        waifu_receiver.status = Poison(waifu_receiver, True)
        log("Poison Tail", f"{waifu_receiver.name} is poisoned!")
