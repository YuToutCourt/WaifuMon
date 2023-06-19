from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class SonicBoom(Move):
    def __init__(self):
        super().__init__(
            "Sonic Boom",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=90,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Always inflicts 20 HP.
        """
        waifu_receiver.hp -= 20
        log(self.name, waifu_receiver.name, f"lost 20 HP")
