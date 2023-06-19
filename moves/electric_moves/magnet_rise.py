from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class MagnetRise(Move):
    def __init__(self):
        super().__init__(
            "Magnet Rise",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User gain the fly type.
        """
        if not any(Types.FLY == type_.type_name for type_ in waifu_user.types):
            waifu_user.types.append(TypeFactory.create_type(Types.FLY))
            log(waifu_user.name, "is now Fly type")
        else:
            log(waifu_user.name, "is already Fly type")
