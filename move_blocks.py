import pygame

from settings import Settings
from blocks import Blocks


class MoveBlocks:
    def __init__(self, screen):
        self.settings = Settings()
        self.blocks = Blocks(screen)

        self.y_start_area = self.settings.y_start_area
        self.y_end_area = self.settings.y_end_area
        self.h_cell = self.settings.h_cell
        self.current_block = self.settings.current_block

    def change_coord(self, initial_coord):
        print(initial_coord)
        # y = initial_coord + self.h_cell
        # return y

    def move_down_block(self, coords_blocks):
        self.coords_blocks = coords_blocks
        self.blocks.draw_figurs()

        print(self.current_block["coord"][1])

        # if self.current_block["coord"][1] + self.h_cell < self.y_end_area:
        #     self.current_block["coord"][1] = self.change_coord(
        #         self.current_block["coord"]
        #     )
