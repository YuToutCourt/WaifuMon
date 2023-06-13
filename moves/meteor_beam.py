from .move import Move
from waifu_types.type import Type

class MeteorBeam(Move):
    def __init__(self):
        super().__init__("Meteor Beam", type=Type.ROCK, power=120, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        User gathers space power and boosts its Sp. Atk stat, then attacks the target on the next turn.
        """
        pass
