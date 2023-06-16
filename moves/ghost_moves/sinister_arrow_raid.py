from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SinisterArrowRaid(Move):
    def __init__(self):
        super().__init__(
            "Sinister Arrow Raid",
            type=TypeFactory.create_type(Types.GHOST),
            power=180,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Decidueye-exclusive Z-Move.
        """
        pass
