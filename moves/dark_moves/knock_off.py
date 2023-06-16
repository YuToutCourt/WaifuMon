from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class KnockOff(Move):
    def __init__(self):
        super().__init__(
            "Knock Off",
            type=TypeFactory.create_type(Types.DARK),
            power=65,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Removes opponent's held item for the rest of the battle.
        """
        pass
