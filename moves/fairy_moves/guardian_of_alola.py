from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class GuardianofAlola(Move):
    def __init__(self):
        super().__init__(
            "Guardian of Alola",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Tapu-exclusive Z-move. Cuts opponent's HP by 75%.
        """
        waifu_receiver.hp -= waifu_receiver.hp_max * 0.25
        log(waifu_receiver.name, "has lost 75% of its HP")
