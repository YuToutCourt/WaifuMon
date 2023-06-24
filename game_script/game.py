import pytmx
import pygame

from character.player import Player
from utils.coordinates import Coordinates
from character.npc import NPC
from character.dialog import Dialog
from map.map_manager import MapManager


class Game:
    def __init__(self):
        # récupération des informations sur tous les écrans connectés
        screens = pygame.display.list_modes()

        # Choix de l'écran le plus grand
        largest_screen = max(screens, key=lambda s: s[0] * s[1])
        screen_width, screen_height = largest_screen

        # Création de la fenêtre
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.FULLSCREEN
        )

        pygame.display.set_caption("WaifuMon")

        coordinates = Coordinates(0, 0)
        self.player = Player(coordinates)
        self.map_manager = MapManager(self.screen, self.player)

        enter_house = self.map_manager.get_object("enter")
        self.enter_house = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)
        self.load_npc()
        self.dialog = Dialog()
        self.contact = False

    def load_npc(self):
        """
        Charge les NPC depuis le fichier tmx de la map
        :param tmx_data: le fichier tmx de la map
        """
        for layer in self.map_manager.get_tmx_data().layers:
            for obj in layer:
                if not isinstance(obj, pytmx.TiledObject):
                    continue
                ignored_names = ["Player", "enter", "spawn_outdoor", "exit", "spawn_indoor", "second_exit", None]
                if obj.name in ignored_names: 
                    continue
                coordinates = Coordinates(obj.x, obj.y)
                npc = NPC(obj.name, coordinates, obj.properties["dialog"])
                self.map_manager.get_group().add(npc)

    def handle_input(self):
        """
        Gère les entrées clavier du joueur
        :return: True si le joueur a appuyé sur la touche SHIFT, False sinon
        """
        pressed = pygame.key.get_pressed()
        # if the player press the shift key
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            # the player is running
            return self.player.move(pressed, True)

        return self.player.move(pressed, False)

    def handle_collisions(self):
        """
        Gère les collisions entre le joueur et les autres sprites
        """
        pressed = pygame.key.get_pressed()
        for npc in self.map_manager.get_group().sprites():
            if isinstance(npc, NPC):
                if (
                    pygame.sprite.collide_rect(self.player, npc)
                    and pressed[pygame.K_RETURN]
                ):
                    self.contact = True
                elif not pygame.sprite.collide_rect(self.player, npc) and pressed[
                    pygame.K_RETURN
                ]:
                    self.contact = False
                    self.dialog.end_dialog()

    def run(self):
        """
        Boucle principale du jeu
        """
        running = True
        while running:
            self.handle_input()
            for npc in self.map_manager.get_group().sprites():
                if isinstance(npc, NPC):
                    npc.random_move()
            self.map_manager.update()
            self.map_manager.draw()
            self.handle_collisions()
            self.dialog.display(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.contact:
                        self.dialog.set_text(npc.dialog)
                        self.dialog.start_dialog()
                        if self.dialog.fight == True:
                            npc.handle_interaction(self.screen, self.player)
                        else:
                            pass

            
        pygame.quit()
