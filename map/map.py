from pygame import Rect, key, sprite, K_RETURN
from pyscroll.group import PyscrollGroup
from pytmx import TiledMap, TiledObject
from map.portal import Portal
from character.npc import NPC
from utils.coordinates import Coordinates
class Map:
    def __init__(self, name, collisions, group, tmx_data, portals, player, screen, event):
        self.name: str = name
        self.collisions: list[Rect] = collisions
        self.group: set(PyscrollGroup) = group
        self.tmx_data: TiledMap = tmx_data
        self.portals: list[Portal] = portals
        self.player = player
        self.screen = screen
        self.event = event
        
    def load_npc(self):
        """
        Load npc from tmx file
        :param tmx_data: tmx file data
        """
        for layer in self.tmx_data.layers:
            for obj in layer:
                if not isinstance(obj, TiledObject):
                    continue
                ignored_names = ["Player", "enter", "spawn_outdoor", "exit", "spawn_indoor", "second_exit", None]
                if obj.name in ignored_names: 
                    continue
                coordinates = Coordinates(obj.x, obj.y)
                npc = NPC(obj.name, coordinates, obj.properties["dialog"])
                self.group.add(npc)

    def handle_collisions(self):
        """
        Handle collisions between player and map
        """
        pressed = key.get_pressed()
        for npc in self.group.sprites():
            if isinstance(npc, NPC):
                if not sprite.collide_rect(self.player, npc): continue
                if pressed[K_RETURN]:
                     npc.handle_interaction(self.screen, self.player)
        from game_script.fight_screen import FightScreen
        import pygame
        fight_screen = FightScreen(self.screen)
        for event in self.event:
            if pygame.Rect.colliderect(self.player.rect, event):
                return fight_screen.run_fight(self.player, npc)


    def move_npc(self):
        """
        Move npc randomly
        """
        for npc in self.group.sprites():
            if isinstance(npc, NPC):
                npc.random_move(self.collisions)
