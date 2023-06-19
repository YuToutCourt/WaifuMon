from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class PainSplit(Move):
    def __init__(self):
        super().__init__(
            "Pain Split",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The user's and opponent's HP becomes the average of both.
        """
        average_hp = (waifu_user.hp + waifu_receiver.hp) / 2

        if waifu_user.hp_max <= average_hp:
            waifu_user.hp = waifu_user.hp_max
        else:
            waifu_user.hp = average_hp

        if waifu_receiver.hp_max <= average_hp:
            waifu_receiver.hp = waifu_receiver.hp_max
        else:
            waifu_receiver.hp = average_hp

        log(
            self.name,
            f"{waifu_user.name} and {waifu_receiver.name} set to their average hp",
        )
