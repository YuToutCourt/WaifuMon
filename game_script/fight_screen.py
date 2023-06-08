import pygame
import random

from game_script.fight import Fight

class FightScreen:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        pygame.display.set_caption("fight")
        self.in_fight = True

    def run_fight(self):
        """
        Lance un combat
        """
        fight = Fight()
        fight.run()

        self.in_fight = False
    
    def fill_screen(self):
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

        if random.randint(0, 1): cubes = cubes[::-1]
        
        for cube in cubes:
            pygame.draw.rect(self.screen, COLOR, cube)
            pygame.display.flip()
            pygame.time.wait(5)

    def load_background(self):
        """
        Charge l'image de fond
        """
        background = pygame.image.load("asset/Battleground/battleground1.png")
        background_scaled = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))

        while self.in_fight:
            self.screen.blit(background_scaled, (0, 0))
            pygame.display.flip()
        
        self.screen.fill((0, 0, 0))
