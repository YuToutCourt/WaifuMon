from dataclasses import dataclass

@dataclass
class Portal:
    world_origin: str
    world_destination: str
    point_origin: str
    point_destination: str