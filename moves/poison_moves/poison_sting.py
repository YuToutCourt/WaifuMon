from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison

class PoisonSting(Move):
    def __init__(self):
        super().__init__(
            "Poison Sting",
            type=TypeFactory.create_type(Types.POISON),
            power=15,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Poisons opponent.
        """
        if waifu_receiver.status is not None:
            log("But it failed")
            return
        waifu_receiver.status = Poison(waifu_receiver, True)
        log(self.name, waifu_receiver.name, "was poisoned")
