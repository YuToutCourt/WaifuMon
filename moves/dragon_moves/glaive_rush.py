from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GlaiveRush(Move):
    def __init__(self):
        super().__init__(
            "Glaive Rush",
            type=TypeFactory.create_type(Types.DRAGON),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Attacks from opposing Pokemon during the next turn cannot miss and will inflict double damage.
        """
        pass
