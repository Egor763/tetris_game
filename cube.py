import pygame

from settings import Settings
from blocks import Blocks


class Cube:
    def __init__(self, screen):
        self.settings = Settings()
        self.blocks = Blocks(screen)

        self.h_cell = self.settings.h_cell
        self.current_block = self.settings.current_block
        self.coords_blocks = self.settings.coords_blocks
        self.game_active = self.settings.game_active

    def move_cube(self):
        self.current_block["coord"][1] += self.h_cell

    def draw_squares(self):
        if self.game_active:
            self.blocks.draw_figurs()
