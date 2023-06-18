from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.sleep import Sleep

class Yawn(Move):
    def __init__(self):
        super().__init__(
            "Yawn",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )
        self.turn = 0

    def effect(self, waifu_user, waifu_reciver):
        """
        Puts opponent to sleep in the next turn.
        """
        if self.turn == 1:
            waifu_reciver.status = Sleep(waifu_reciver, False)
            log(self.name, f"{waifu_reciver.name} is now sleeping!")
            self.turn = 0

        else:
            log(self.name, f"{waifu_reciver.name} is feeling daisy!")
            self.turn += 1