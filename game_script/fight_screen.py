import pygame
import random
import threading

from game_script.fight import Fight
from waifu.waifu import Waifu
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from wtypes.type import Type

class FightScreen:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        pygame.display.set_caption("fight")
        self.in_fight = True

    def run_fight(self, player, npc):
        """
        Lance un combat
        """
        fight = Fight(player, npc)
        self.__fill_screen()
        background_thread = threading.Thread(target=self.__load_background, args=(player, npc))
        background_thread.start()
        fight.start()

        self.in_fight = False

    def __fill_screen(self):
        """
        Remplir l'écran avec une couleur
        """
        COLOR = (0, 0, 0)
        width = self.screen.get_width()
        height = self.screen.get_height()

        cubes = []
        cubes_size = min(width, height) // 10

        # On pourrait s'amuser à faire des animations différentes :D
        for x in range(0, self.screen.get_width(), cubes_size):
            for y in range(0, self.screen.get_height(), cubes_size):
                cube = pygame.Rect(x, y, cubes_size, cubes_size)
                cubes.append(cube)

        if random.randint(0, 1):
            cubes = cubes[::-1]

        for cube in cubes:
            pygame.draw.rect(self.screen, COLOR, cube)
            pygame.display.flip()
            pygame.time.wait(5)

    def __load_background(self, player, npc):
        """
        Charge l'image de fond
        """
        background = pygame.image.load("asset/Battleground/battleground1.png")
        background_scaled = pygame.transform.scale(
            background, (self.screen.get_width(), self.screen.get_height())
        )

        while self.in_fight:
            self.screen.blit(background_scaled, (0, 0))
            self.__load_waifu(player, npc)
            pygame.display.flip()

        # Efface le background pour revenir à l'écran de jeu
        self.screen.fill((0, 0, 0))

    def __load_waifu(self, player, npc):
        """
        Charge l'image du waifu
        """
        waifu_front = player.team[0].get_front_image()
        waifu_front_scaled = pygame.transform.scale(waifu_front, (self.screen.get_width() // 5, self.screen.get_height() // 3))
        
        # Print les noms des waifus pour pouvoir corriger leur taille / position
        print(player.team[0].get_name(), npc.team[0].get_name())

        waifu_back = npc.team[0].get_back_image()
        waifu_back_scaled = pygame.transform.scale(waifu_back, (self.screen.get_width() // 3.75, self.screen.get_height() // 1.75))
        while self.in_fight:
            self.screen.blit(waifu_front_scaled, (self.screen.get_width() // 1.5, self.screen.get_height() // 2.95 ))
            self.screen.blit(waifu_back_scaled, (self.screen.get_width() // 8, self.screen.get_height() // 2.2 ))
            pygame.display.flip()