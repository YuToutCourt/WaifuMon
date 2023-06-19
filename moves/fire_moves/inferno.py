from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn


class Inferno(Move):
    def __init__(self):
        super().__init__(
            "Inferno",
            type=TypeFactory.create_type(Types.FIRE),
            power=100,
            accuracy=50,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Burns opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Burn(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is burned")
        else:
            log(self.name, waifu_receiver.name, "have already a status effect")
