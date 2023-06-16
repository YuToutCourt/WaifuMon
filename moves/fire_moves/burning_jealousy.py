from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BurningJealousy(Move):
    def __init__(self):
        super().__init__(
            "Burning Jealousy",
            type=TypeFactory.create_type(Types.FIRE),
            power=70,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits all opponents, and burns any that have had their stats boosted.
        """
        pass
