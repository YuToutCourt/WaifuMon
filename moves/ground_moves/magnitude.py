from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from random import randint

class Magnitude(Move):
    def __init__(self):
        super().__init__(
            "Magnitude",
            type=TypeFactory.create_type(Types.GROUND),
            power=randint(10, 150),
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Hits with random power.
        """
        self.power = randint(10, 150)
