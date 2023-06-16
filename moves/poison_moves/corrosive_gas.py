from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CorrosiveGas(Move):
    def __init__(self):
        super().__init__(
            "Corrosive Gas",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=40,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Removes opponent's items.
        """
        pass
