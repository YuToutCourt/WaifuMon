from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.burn import Burn

class SandsearStorm(Move):
    def __init__(self):
        super().__init__(
            "Sandsear Storm",
            type=TypeFactory.create_type(Types.GROUND),
            power=100,
            accuracy=80,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May burn target.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Burn(waifu_receiver, True)
            log(self.name, "burns", waifu_receiver.name)
        else:
            log(self.name, "already has a status problem")
