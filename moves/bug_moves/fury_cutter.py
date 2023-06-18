from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FuryCutter(Move):
    def __init__(self):
        super().__init__(
            "Fury Cutter",
            type=TypeFactory.create_type(Types.BUG),
            power=40,
            accuracy=95,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Power increases each turn.
        """
        if self.power < 160:
            self.power *= 2
