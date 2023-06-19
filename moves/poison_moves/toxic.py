from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison


class Toxic(Move):
    def __init__(self):
        super().__init__(
            "Toxic",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Badly poisons opponent.
        """
        if waifu_receiver.status is not None:
            log("But it failed")
            return
        waifu_receiver.status = Poison(waifu_receiver, True)
        log(self.name, waifu_receiver.name, "was badly poisoned")
