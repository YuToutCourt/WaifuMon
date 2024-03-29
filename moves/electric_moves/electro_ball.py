from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ElectroBall(Move):
    def __init__(self):
        super().__init__(
            "Electro Ball",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The faster the user, the stronger the attack.
        """
        pass
