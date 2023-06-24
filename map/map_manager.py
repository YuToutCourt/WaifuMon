import pygame, pytmx, pyscroll
from map.portal import Portal
from map.map import Map


class MapManager:
    def __init__(self, screen, player):
        self.maps = dict()
        self.current_map = "Desert"
        self.screen = screen
        self.player = player
        self.register_map("Desert", portals=[Portal("Desert", "House", "enter", "spawn_indoor")])
        self.register_map("House", portals=[Portal("House", "Desert", "exit", "spawn_outdoor")])
        self.spawn_player("Player")

    def get_tmx_data(self):
        return self.get_map().tmx_data

    def get_map(self):
        return self.maps[self.current_map]
    
    def get_collisions(self):
        return self.get_map().collisions
    
    def get_group(self):
        return self.get_map().group
    
    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def register_map(self, name, portals=[]):
        tmx_data = pytmx.util_pygame.load_pygame(f"./asset/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size()
        )

        map_layer.zoom = 2

        collisions = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        pygame.mixer.init()
        pygame.mixer.fadeout(1000)

        pygame.mixer.music.load("asset/music/main_theme.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        self.direction_map = {
            (pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT): "down",
            (pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT): "up",
            (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN): "right",
            (pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN): "left",
            (pygame.K_UP, pygame.K_LEFT): "down_right",
            (pygame.K_UP, pygame.K_RIGHT): "down_left",
            (pygame.K_DOWN, pygame.K_LEFT): "up_right",
            (pygame.K_DOWN, pygame.K_RIGHT): "up_left",
            (pygame.K_UP,): "down",
            (pygame.K_DOWN,): "up",
            (pygame.K_LEFT,): "right",
            (pygame.K_RIGHT,): "left",
        }

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        self.maps[name] = Map(name, collisions, self.group, tmx_data, portals)

    def spawn_player(self, name):
        point = self.get_object(name)
        self.player.position = (point.x, point.y)

    def check_collision(self):
        for portal in self.get_map().portals:
            if portal.world_origin == self.current_map:
                point = self.get_object(portal.point_origin)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)
                if self.player.rect.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.world_destination
                    self.spawn_player(portal.point_destination)

        pressed = pygame.key.get_pressed()
                    
        for collision in self.get_collisions():
            if pygame.Rect.colliderect(self.player.rect, collision):
                for keys, direction in self.direction_map.items():
                    if all(pressed[key] for key in keys):
                        return self.player.move_back(direction)



    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
    
    def update(self):
        self.get_group().update()
        self.check_collision()
