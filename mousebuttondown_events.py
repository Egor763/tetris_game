import pygame

from button_active import ButtonActive
from button_inactive import ButtonInactive
from settings import Settings
from exit_game import ExitGame
from start_game import StartGame


class MousebuttondownEvents:
    def __init__(self, screen):
        self.button_active_class = ButtonActive(screen, "Завершить игру")
        self.button_inactive_class = ButtonInactive(screen, "Играть")
        self.settings = Settings()
        self.exit_game = ExitGame(screen)
        self.start_game = StartGame(screen)

        self.game_active = self.settings.game_active

    def set_listener(self, event):
        if self.button_active_class.rect.collidepoint(event.pos):
            mouse_pos = pygame.mouse.get_pos()
            self.check_play_button(mouse_pos)

        elif self.button_inactive_class.rect_inactive.collidepoint(event.pos):
            mouse_pos_inactive_button = pygame.mouse.get_pos()
            self.check_play_inactive_button(mouse_pos_inactive_button)

    def check_play_button(self, mouse_pos):
        button_clicked = self.button_active_class.rect.collidepoint(mouse_pos)

        if button_clicked and self.game_active:
            self.exit_game.game_over()

    def check_play_inactive_button(self, mouse_pos_inactive_button):
        button_clicked = self.button_inactive_class.rect_inactive.collidepoint(
            mouse_pos_inactive_button
        )

        if button_clicked and not self.game_active:
            self.start_game.game_launch()
