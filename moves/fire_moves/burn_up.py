from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn


class BurnUp(Move):
    def __init__(self):
        super().__init__(
            "Burn Up",
            type=TypeFactory.create_type(Types.FIRE),
            power=130,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        To inflict massive damage, the user burns itself out. After using this move, the user will no longer be Fire type.
        """
        waifu_user.status = Burn(waifu_receiver, True)
        if any(Types.FIRE == type_.type_name for type_ in waifu_user.types):
            waifu_user.types.remove(TypeFactory.create_type(Types.FIRE))
            log(self.name, waifu_user.name, "is burned and is no longer Fire type")
        log(self.name, waifu_user.name, "is burned")
