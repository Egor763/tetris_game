import pygame

from settings import Settings
from screen import Screen


class ExitGame:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen_class = Screen(screen)

        self.game_active = self.settings.game_active

    def game_over(self):
        self.settings.game_active = False
        self.screen_class.delete_grid()
        print("o")

        pygame.display.flip()
