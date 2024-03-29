from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PhantomForce(Move):
    def __init__(self):
        super().__init__(
            "Phantom Force",
            type=TypeFactory.create_type(Types.GHOST),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Disappears on first turn, attacks on second. Can strike through Protect/Detect.
        """
        pass
