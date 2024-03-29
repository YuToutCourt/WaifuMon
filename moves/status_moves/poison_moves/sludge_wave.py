from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.poison import Poison


class SludgeWave(Move):
    def __init__(self):
        super().__init__(
            "Sludge Wave",
            type=TypeFactory.create_type(Types.POISON),
            power=95,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May poison opponent.
        """
        waifu_receiver.status = Poison(waifu_receiver, True)
        log("Sludge Wave", f"{waifu_receiver.name} is poisoned!")
