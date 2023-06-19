from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from status.sleep import Sleep
from utils.logger import log


class DarkVoid(Move):
    def __init__(self):
        super().__init__(
            "Dark Void",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=50,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Puts all adjacent opponents to sleep.
        """
        if not waifu_receiver.status is None:
            waifu_receiver.status = Sleep(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "fell asleep")
        else:
            log(self.name, waifu_receiver.name, "is already asleep")
