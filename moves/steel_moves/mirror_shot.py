from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MirrorShot(Move):
    def __init__(self):
        super().__init__(
            "Mirror Shot",
            type=TypeFactory.create_type(Types.STEEL),
            power=65,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
