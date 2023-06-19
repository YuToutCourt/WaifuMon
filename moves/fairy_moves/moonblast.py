from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class Moonblast(Move):
    def __init__(self):
        super().__init__(
            "Moonblast",
            type=TypeFactory.create_type(Types.FAIRY),
            power=95,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May lower opponent's Attack.
        """
        if waifu_receiver.status is not None:
            log(waifu_receiver.name, "is already", waifu_receiver.status.status)
        else:
            waifu_receiver.status = Paralysis(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is paralyzed")
