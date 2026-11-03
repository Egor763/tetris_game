import pygame

from settings import Settings


class MoveBlocks:
    def __init__(self, squares):
        self.squares = squares

        self.settings = Settings()

        self.y_start_area = self.settings.y_start_area
        self.y_end_area = self.settings.y_end_area

    def change_coord(self, initial_coord):
        y = initial_coord + self.h_cell
        return y
