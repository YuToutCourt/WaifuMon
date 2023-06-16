from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SpiritBreak(Move):
    def __init__(self):
        super().__init__(
            "Spirit Break",
            type=TypeFactory.create_type(Types.FAIRY),
            power=75,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
