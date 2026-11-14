import pygame

from settings import Settings
from screen import Screen


class StartGame:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen_class = Screen(screen)

        self.game_active = self.settings.game_active

    def game_launch(self):
        self.settings.game_active = True
        self.screen_class.handle_grid()
        print("k")

        pygame.display.flip()
