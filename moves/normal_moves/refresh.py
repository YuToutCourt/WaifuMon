from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.status_enum import StatusE


class Refresh(Move):
    def __init__(self):
        super().__init__(
            "Refresh",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Cures paralysis, poison, and burns.
        """
        if waifu_user.status == StatusE.PARALYSIS:
            waifu_user.status = None
            log(f"{waifu_user.name} is no longer paralyzed!")
        elif waifu_user.status == StatusE.POISON:
            waifu_user.status = None
            log(f"{waifu_user.name} is no longer poisoned!")
        elif waifu_user.status == StatusE.BURN:
            waifu_user.status = None
            log(f"{waifu_user.name} is no longer burned!")
