from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class EsperWing(Move):
    def __init__(self):
        super().__init__("Esper Wing", type=TypeFactory.create_type(Types.PSYCHIC), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. Raises user's Speed.
        """
        pass
