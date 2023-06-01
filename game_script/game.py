import pytmx
import pygame
import pyscroll

from player_script.player import Player
from utils.coordinates import Coordinates
from game_script.npc import NPC

class Game:
    def __init__(self):

        # récupération des informations sur tous les écrans connectés
        screens = pygame.display.list_modes()

        # Choix de l'écran le plus grand
        largest_screen = max(screens, key=lambda s: s[0] * s[1])
        screen_width, screen_height = largest_screen

        # Création de la fenêtre
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

        pygame.display.set_caption("WaifuMon")

        tmx_data = pytmx.util_pygame.load_pygame("asset/Desert.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        map_layer.zoom = 2

        player_position = tmx_data.get_object_by_name("Player")
        coordinates = Coordinates(player_position.x, player_position.y)
        self.player = Player(coordinates)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        self.load_npc(tmx_data)


    def load_npc(self, tmx_data):
        for layer in tmx_data.layers:
            for obj in layer:
                if not isinstance(obj, pytmx.TiledObject): continue
                if obj.name == "Player": continue
                coordinates = Coordinates(obj.x, obj.y)
                npc = NPC(obj.name, coordinates, obj.properties["dialog"])
                self.group.add(npc)


    def handle_input(self):
        pressed = pygame.key.get_pressed()  
        # if the player press the shift key
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            # the player is running
            return self.player.move(pressed, True)
            
        return self.player.move(pressed, False)

    def handle_collisions(self):
        pressed = pygame.key.get_pressed()  
        for npc in self.group.sprites():
            if isinstance(npc, NPC):
                if pygame.sprite.collide_rect(self.player, npc) and pressed[pygame.K_RETURN] :
                    npc.handle_interaction()


    def run(self):
        # Boucle principale pour afficher la fenêtre
        running = True
        while running:
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.handle_collisions()
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Termination de pygame
        pygame.quit()