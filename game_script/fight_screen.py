import pygame
import random
import threading

from game_script.fight import Fight

# from utils.my_thread import MyThread


class FightScreen:
    def __init__(self, screen):
        pygame.init()
        pygame.display.set_caption("fight")
        self.screen = screen
        self.background = None
        self.waifu_front = None
        self.waifu_back = None

    def run_fight(self, player, npc):
        """
        Lance un combat
        """
        fight = Fight(player, npc)
        self.__fill_screen()
        self.__load_background()

        fight_thread = threading.Thread(target=fight.start)
        fight_thread.start()

        # main_loop_t = threading.Thread(target=self.__main_loop, args=(player, npc, fight))
        # main_loop_t.start()

        # def __main_loop(self, player, npc, fight):
        while fight.finished is False:
            _ = pygame.event.get()
            if self.__load_waifu(player, npc):
                self.__update_display()

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

    def __load_background(self):
        """
        Charge l'image de fond
        """
        background = pygame.image.load("asset/Battleground/battleground1.png")

        self.background = pygame.transform.scale(
            background, (self.screen.get_width(), self.screen.get_height())
        )

    def __load_waifu(self, player, npc):
        """
        Charge l'image des waifu
        """

        waifu_ = None
        waifu__ = None

        for waifu in npc.team:
            if waifu.in_fight:
                waifu_ = waifu

        if waifu_ is not None:
            self.waifu_front = pygame.transform.scale(
                waifu_.get_front_image(),
                (self.screen.get_width() // 5, self.screen.get_height() // 3),
            )

        for waifu in player.team:
            if waifu.in_fight:
                waifu__ = waifu

        if waifu__ is not None:
            self.waifu_back = pygame.transform.scale(
                waifu__.get_back_image(),
                (self.screen.get_width() // 3.75, self.screen.get_height() // 1.75),
            )

        return waifu_ is not None and waifu__ is not None

    def __update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(
            self.waifu_front,
            (self.screen.get_width() // 1.5, self.screen.get_height() // 2.95),
        )
        self.screen.blit(
            self.waifu_back,
            (self.screen.get_width() // 8, self.screen.get_height() // 2.2),
        )

        pygame.display.flip()
