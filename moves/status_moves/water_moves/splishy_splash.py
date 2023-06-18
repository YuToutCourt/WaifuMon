from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.paralysis import Paralysis

class SplishySplash(Move):
    def __init__(self):
        super().__init__(
            "Splishy Splash",
            type=TypeFactory.create_type(Types.WATER),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        May paralyze opponent.
        """
        waifu_reciver.status = Paralysis(waifu_reciver, False)
        log(self.name, f"{waifu_reciver.name} is now paralysis!")
