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
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load("asset/music/fight_theme.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

        fight_thread = threading.Thread(target=fight.start)
        fight_thread.start()

        # main_loop_t = threading.Thread(target=self.__main_loop, args=(player, npc, fight))
        # main_loop_t.start()

        # Display the fight
        while fight.finished is False:
            _ = pygame.event.get()
            if self.__load_waifu(player, npc):
                self.__update_display(player, npc)

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
        background = pygame.image.load("asset/Battle/battleground2.jpg")

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

    def create_text(self, text, font_size, color):
        """
        Créer un texte
        """
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        return text_surface

    def create_hp_bar(self, current_hp, max_hp, bar_width, bar_height):
            """
            Create an HP bar surface with a gradual color transition.
            """
            bar_surface = pygame.Surface((bar_width, bar_height))
            bar_surface.fill((255, 255, 255))  # Fill with white color

            # Calculate the width of the green portion of the bar
            green_width = int((current_hp / max_hp) * bar_width)

            # Calculate the RGB color based on HP percentage
            red = int((1 - current_hp / max_hp) * 255)
            green = int((current_hp / max_hp) * 255)
            color = (red, green, 0)

            # Draw the green portion of the bar
            green_rect = pygame.Rect(0, 0, green_width, bar_height)
            pygame.draw.rect(bar_surface, color, green_rect)

            return bar_surface
    
    def create_pokeball(self, width, height):
        """
        Create a pokeball surface.
        """
        pokeball = pygame.image.load("asset/Battle/icon_ball.png")
        pokeball = pygame.transform.scale(pokeball, (width, height))
        
        return pokeball



    def __update_display(self, player_waifu, npc_waifu):
        self.screen.blit(self.background, (0, 0))

        pokeball = self.create_pokeball(52, 55)
        self.screen.blit(pokeball, (self.screen.get_width() // 1.1, self.screen.get_height() // 1.1))

        # Position and dimensions calculations based on screen size
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        player_name_x = int(screen_width * 0.760)
        player_name_y = int(screen_height * 0.8195)
        player_level_x = int(screen_width * 0.8855)
        player_level_y = int(screen_height * 0.8195)
        player_hp_x = int(screen_width * 0.8855)
        player_hp_y = int(screen_height * 0.87963)
        player_hp_bar_x = int(screen_width * 0.86355)
        player_hp_bar_y = int(screen_height * 0.85)

        npc_name_x = int(screen_width * 0.0261)
        npc_name_y = int(screen_height * 0.0352)
        npc_level_x = int(screen_width * 0.1563)
        npc_level_y = int(screen_height * 0.0352)
        npc_hp_x = int(screen_width * 0.08073)
        npc_hp_y = int(screen_height * 0.09445)
        npc_hp_bar_x = int(screen_width * 0.0292)
        npc_hp_bar_y = int(screen_height * 0.0667)


        # Afficher les informations du waifu du joueur
        waifu_player_name = player_waifu.get_waifu_in_fight().name
        waifu_player_hp = player_waifu.get_waifu_in_fight().hp
        waifu_player_max_hp = player_waifu.get_waifu_in_fight().hp_max
        waifu_player_level = player_waifu.get_waifu_in_fight().level

        player_name_surface = self.create_text(waifu_player_name, 30, (0, 0, 0))
        player_hp_surface = self.create_text(f"{round(waifu_player_hp)}/{waifu_player_max_hp}", 30, (0, 0, 0))
        player_level_surface = self.create_text(f"Lv{waifu_player_level}", 30, (0, 0, 0))
        
        player_hp_bar = self.create_hp_bar(waifu_player_hp, waifu_player_max_hp, int(screen_width * 0.1063), int(screen_height * 0.013))
        self.screen.blit(player_hp_bar, (player_hp_bar_x, player_hp_bar_y))

        self.screen.blit(player_name_surface, (player_name_x, player_name_y))
        self.screen.blit(player_level_surface, (player_level_x, player_level_y))
        self.screen.blit(player_hp_surface, (player_hp_x, player_hp_y))
        
        # Afficher les informations du waifu du NPC
        waifu_npc_name = npc_waifu.get_waifu_in_fight().name
        waifu_npc_hp = npc_waifu.get_waifu_in_fight().hp
        waifu_npc_max_hp = npc_waifu.get_waifu_in_fight().hp_max
        waifu_npc_level = npc_waifu.get_waifu_in_fight().level

        npc_hp_bar = self.create_hp_bar(waifu_npc_hp, waifu_npc_max_hp, int(screen_width * 0.1063), int(screen_height * 0.013))
        self.screen.blit(npc_hp_bar, (npc_hp_bar_x, npc_hp_bar_y))

        npc_name_surface = self.create_text(waifu_npc_name, 30, (0, 0, 0))
        npc_hp_surface = self.create_text(f"{round(waifu_npc_hp)}/{waifu_npc_max_hp}", 30, (0, 0, 0))
        npc_level_surface = self.create_text(f"Lv{waifu_npc_level}", 30, (0, 0, 0))

        self.screen.blit(npc_name_surface, (npc_name_x, npc_name_y))
        self.screen.blit(npc_level_surface, (npc_level_x, npc_level_y))
        self.screen.blit(npc_hp_surface, (npc_hp_x, npc_hp_y))
       

        self.screen.blit(
            self.waifu_front,
            (self.screen.get_width() // 1.5, self.screen.get_height() * 0.42),
        )
        self.screen.blit(
            self.waifu_back,
            (self.screen.get_width() // 8, self.screen.get_height() // 2.2),
        )

        pygame.display.flip()
