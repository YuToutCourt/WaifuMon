from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RevivalBlessing(Move):
    def __init__(self):
        super().__init__(
            "Revival Blessing",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Revives a fainted party Pokemon to half HP.
        """
        pass
