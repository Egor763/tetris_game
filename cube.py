import pygame

from settings import Settings


class Cube:
    def __init__(self):
        self.settings = Settings()

        self.h_cell = self.settings.h_cell
        self.current_block = self.settings.current_block
        self.coords_blocks = self.settings.coords_blocks

    def move_cube(self):
        self.current_block["coord"][1] += self.h_cell
