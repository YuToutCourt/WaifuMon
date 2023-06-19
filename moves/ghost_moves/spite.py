from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Spite(Move):
    def __init__(self):
        super().__init__(
            "Spite",
            type=TypeFactory.create_type(Types.GHOST),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The opponent's last move loses 2-5 PP.
        """
        from random import randint

        lose = randint(2, 5)
        waifu_receiver.move_to_use.pp -= lose
        log(self.name, waifu_receiver.name, "loses", lose, "PP")
