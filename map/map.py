from pygame import Rect
from pyscroll.group import PyscrollGroup
from pytmx import TiledMap
from map.portal import Portal
from dataclasses import dataclass

@dataclass
class Map:
    name: str
    collisions: list[Rect]
    group: PyscrollGroup
    tmx_data: TiledMap
    portals: list[Portal]