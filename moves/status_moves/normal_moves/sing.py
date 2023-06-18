from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.sleep import Sleep

class Sing(Move):
    def __init__(self):
        super().__init__(
            "Sing",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=55,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        Puts opponent to sleep.
        """
        waifu_reciver.status = Sleep(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is now sleeping!")
