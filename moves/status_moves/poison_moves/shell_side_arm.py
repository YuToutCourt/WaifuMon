from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log
from status.poison import Poison

class ShellSideArm(Move):
    def __init__(self):
        super().__init__(
            "Shell Side Arm",
            type=TypeFactory.create_type(Types.POISON),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May poison opponent. Inflicts either Special or Physical damage, whichever is better.
        """
        waifu_receiver.status = Poison(waifu_receiver, True)
        log("Shell Side Arm", f"{waifu_receiver.name} is poisoned!")
