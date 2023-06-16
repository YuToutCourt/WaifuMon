from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Infestation(Move):
    def __init__(self):
        super().__init__(
            "Infestation",
            type=TypeFactory.create_type(Types.BUG),
            power=20,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
