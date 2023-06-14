from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxGoldRush(Move):
    def __init__(self):
        super().__init__("G-Max Gold Rush", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Meowth-exclusive G-Max Move. Confuses opponents and earns more money.
        """
        pass
