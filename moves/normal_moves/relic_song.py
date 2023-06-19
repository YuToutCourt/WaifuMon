from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.sleep import Sleep


class RelicSong(Move):
    def __init__(self):
        super().__init__(
            "Relic Song",
            type=TypeFactory.create_type(Types.NORMAL),
            power=75,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May put the target to sleep.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Sleep(waifu_receiver, False)
            log(f"{waifu_receiver.name} fell asleep!")
        else:
            log(f"{waifu_receiver.name} is already asleep!")
