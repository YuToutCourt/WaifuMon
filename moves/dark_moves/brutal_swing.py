from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BrutalSwing(Move):
    def __init__(self):
        super().__init__(
            "Brutal Swing",
            type=TypeFactory.create_type(Types.DARK),
            power=60,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user swings its body around violently to inflict damage on everything in its vicinity.
        """
        pass
