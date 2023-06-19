from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Grudge(Move):
    def __init__(self):
        super().__init__(
            "Grudge",
            type=TypeFactory.create_type(Types.GHOST),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        If the users faints after using this move, the PP for the opponent's last move is depleted.
        """
        waifu_user.hp = 0
        waifu_receiver.move_to_use.pp = 0
        log(
            self.name,
            waifu_user.name,
            "faints and depletes",
            waifu_receiver.name,
            "last move PP",
        )
