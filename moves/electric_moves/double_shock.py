from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class DoubleShock(Move):
    def __init__(self):
        super().__init__(
            "Double Shock",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        After using this move, the user will no longer be Electric type.
        """
        if any(Types.ELECTRIC == type_.type_name for type_ in waifu_user.types):
            waifu_user.types.remove(TypeFactory.create_type(Types.ELECTRIC))
            log(waifu_user.name, "is no longer Electric type")
