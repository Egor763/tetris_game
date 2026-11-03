import pygame

from settings import Settings


class Blocks:
    def __init__(self, screen):
        self.screen = screen

        self.settings = Settings()

        self.w_cell = self.settings.w_cell
        self.h_cell = self.settings.h_cell

        self.red = (255, 0, 0)
        self.purple = (139, 0, 255)
        self.dark_blue = (0, 255, 255)
        self.yellow = (255, 255, 0)
        self.blue = (0, 191, 255)
        self.gray = (128, 128, 128)
        self.green = (0, 128, 0)

    def draw_figurs(self):
        self.square = pygame.draw.rect(
            self.screen,
            self.green,
            (
                self.settings.x_start_area + (4 * self.w_cell),
                self.settings.y_start_area,
                self.w_cell,
                self.h_cell,
            ),
        )

        pygame.display.update()
