from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MakeItRain(Move):
    def __init__(self):
        super().__init__(
            "Make It Rain",
            type=TypeFactory.create_type(Types.STEEL),
            power=120,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers user's Special Attack. Money is earned after the battle.
        """
        pass
