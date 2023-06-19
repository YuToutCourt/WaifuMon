from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from random import randint
from utils.logger import log
from status.burn import Burn
from status.paralysis import Paralysis
from status.freeze import Freeze


class TriAttack(Move):
    def __init__(self):
        super().__init__(
            "Tri Attack",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May paralyze, burn or freeze opponent.
        """
        number = randint(1, 3)

        match number:
            case 1:
                waifu_reciver.status = Burn(waifu_reciver, True)
                log(self.name, f"{waifu_reciver.name} is now burned")
            case 2:
                waifu_reciver.status = Paralysis(waifu_reciver, False)
                log(self.name, f"{waifu_reciver.name} is now paralyse")

            case 3:
                waifu_reciver.status = Freeze(waifu_reciver, False)
                log(self.name, f"{waifu_reciver.name} is now freeze")

            case _:
                log(self.name + "Error")
