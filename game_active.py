import pygame

from settings import Settings
from screen import Screen
from button_active import ButtonActive
from blocks import Blocks


class GameActive:
    # класс вызывается только тогда когда игра активна
    def __init__(self, screen, msg):
        self.settings = Settings()
        self.screen_class = Screen(screen)
        self.button_active_class = ButtonActive(screen, msg)
        self.blocks = Blocks(screen)

        self.current_block = self.settings.current_block
        self.h_cell = self.settings.h_cell
        self.key_button = self.settings.key_button

    def screen_active(self):
        self.screen_class.handle_grid()
        self.button_active_class.draw_button()
        self.draw_squares()

    def set_timer(self):
        self.current_block["coord"][1] += self.h_cell
        print(self.current_block["coord"][1])

    def draw_squares(self):
        if self.settings.game_active:
            self.blocks.draw_figurs()
