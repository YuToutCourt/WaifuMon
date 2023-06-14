from typing import List

from .bug_type import Bug_Type
from .dark_type import Dark_Type
from .dragon_type import Dragon_Type
from .electric_type import Electric_Type
from .fairy_type import Fairy_Type
from .fighting_type import Fighting_Type
from .fire_type import Fire_Type
from .flying_type import Flying_Type
from .ghost_type import Ghost_Type
from .grass_type import Grass_Type
from .ground_type import Ground_Type
from .ice_type import Ice_Type
from .normal_type import Normal_Type
from .poison_type import Poison_Type
from .psy_type import Psy_Type
from .rock_type import Rock_Type
from .steel_type import Steel_Type
from .water_type import Water_Type

class Type:
    def __init__(
        self,
        type_name: Types,
        weaknesses: List[Types],
        resistances: List[Types],
        immunities: List[Types],
    ):
        self.type_name = type_name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities

    def get_type_by_name(self, type_name: str):
        """
        Return the type corresponding to the name
        """
        types_map = {
            "NORMAL": Normal_Type(),
            "FIGHTING": Fighting_Type(),
            "FLYING": Flying_Type(),
            "POISON": Poison_Type(),
            "GROUND": Ground_Type(),
            "ROCK": Rock_Type(),
            "BUG": Bug_Type(),
            "GHOST": Ghost_Type(),
            "STEEL": Steel_Type(),
            "FIRE": Fire_Type(),
            "WATER": Water_Type(),
            "GRASS": Grass_Type(),
            "ELECTRIC": Electric_Type(),
            "PSYCHIC": Psy_Type(),
            "ICE": Ice_Type(),
            "DRAGON": Dragon_Type(),
            "DARK": Dark_Type(),
            "FAIRY": Fairy_Type(),
        }

        type_name = type_name.upper()

        type_to_return = types_map.get(type_name)
        if type_to_return is None:
            raise ValueError(f"Type {type_name} doesn't exist")
        
        return type_to_return
            