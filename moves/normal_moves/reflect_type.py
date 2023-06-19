from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class ReflectType(Move):
    def __init__(self):
        super().__init__(
            "Reflect Type",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User becomes the target's type.
        """
        waifu_user.types = waifu_receiver.types
        log(f"{waifu_user.name} became {waifu_receiver.name}'s type!")
