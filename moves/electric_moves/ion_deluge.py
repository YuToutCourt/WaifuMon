from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class IonDeluge(Move):
    def __init__(self):
        super().__init__(
            "Ion Deluge",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=0,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Changes Normal-type moves to Electric-type.
        """
        pass
