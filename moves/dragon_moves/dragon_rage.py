from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class DragonRage(Move):
    def __init__(self):
        super().__init__(
            "Dragon Rage",
            type=TypeFactory.create_type(Types.DRAGON),
            power=1,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Always inflicts 40 HP.
        """
        waifu_receiver.hp -= 40
        log(self.name, waifu_receiver.name, "lost 40 HP")

