from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonHammer(Move):
    def __init__(self):
        super().__init__(
            "Dragon Hammer",
            type=TypeFactory.create_type(Types.DRAGON),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The user uses its body like a hammer to attack the target and inflict damage.
        """
        pass
