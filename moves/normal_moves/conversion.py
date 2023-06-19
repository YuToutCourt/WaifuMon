from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class Conversion(Move):
    def __init__(self):
        super().__init__(
            "Conversion",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Changes user's type to that of its first move.
        """
        waifu_user.types.clear()
        waifu_user.types.append(waifu_user.move_to_use.type)
        log(self.name, "changes", waifu_user.name, "type to", waifu_user.types[0].name)
