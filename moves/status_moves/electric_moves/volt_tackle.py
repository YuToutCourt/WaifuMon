from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class VoltTackle(Move):
    def __init__(self):
        super().__init__(
            "Volt Tackle",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=120,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        User receives recoil damage. May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is paralyse!")

        waifu_user.hp *= 0.8
        log(self.name, f"{waifu_user.name} receives recoil damage!")
