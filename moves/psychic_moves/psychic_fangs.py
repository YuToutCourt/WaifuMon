from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PsychicFangs(Move):
    def __init__(self):
        super().__init__("Psychic Fangs", type=TypeFactory.create_type(Types.PSYCHIC), power=85, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user bites the target with its psychic capabilities. This can also destroy Light Screen and Reflect.
        """
        pass
