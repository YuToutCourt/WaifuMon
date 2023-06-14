from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HealingWish(Move):
    def __init__(self):
        super().__init__("Healing Wish", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user faints and the next Pokémon released is fully healed.
        """
        pass
