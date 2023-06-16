from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LightScreen(Move):
    def __init__(self):
        super().__init__(
            "Light Screen",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Halves damage from Special attacks for 5 turns.
        """
        pass
