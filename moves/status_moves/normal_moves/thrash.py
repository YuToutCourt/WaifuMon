from moves.move import Move
from random import randint
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.confuse import Confusion

class Thrash(Move):
    def __init__(self):
        super().__init__(
            "Thrash",
            type=TypeFactory.create_type(Types.NORMAL),
            power=120,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )
        self.turn = 0

    def effect(self, waifu_user, waifu_reciver):
        """
        User attacks for 2-3 turns but then becomes confused.
        """
        if self.turn >= 2:
            if randint(0 ,1):
                waifu_user.status = Confusion(waifu_user, False)
                log(self.name, f"{waifu_user.name} is confuse!")
                self.turn = 0

        self.turn += 1
