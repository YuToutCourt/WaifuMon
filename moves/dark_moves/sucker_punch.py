from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class SuckerPunch(Move):
    def __init__(self):
        super().__init__(
            "Sucker Punch",
            type=TypeFactory.create_type(Types.DARK),
            power=70,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User attacks first, but only works if opponent is readying an attack.
        """
        pass
