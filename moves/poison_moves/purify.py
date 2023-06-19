from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Purify(Move):
    def __init__(self):
        super().__init__(
            "Purify",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The user heals the target's status condition. If the move succeeds, it also restores the user's own HP.
        """
        if waifu_receiver.status is None:
            log("But it failed")
            return
        waifu_receiver.status = None
        log(self.name, waifu_receiver.name, "was cured of its status condition")
        waifu_user.hp = waifu_user.hp_max
        log(self.name, waifu_user.name, "healed")
