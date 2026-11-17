import pygame

from settings import Settings
from screen import Screen
from buttons import Buttons
from cube import Cube


class Events:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen_class = Screen(screen)
        self.buttons = Buttons(screen, "Завершить игру", "Играть")
        self.cube = Cube(screen)

        self.current_block = self.settings.current_block
        self.h_cell = self.settings.h_cell
        self.key_button = self.settings.key_button
        self.game_active = self.settings.game_active

    def set_events(self):
        # функция установки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if self.settings.game_active:
                    if event.key == pygame.K_i:
                        self.exit_game()

                else:
                    if event.key == pygame.K_RETURN:
                        self.start_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons.rect_active.collidepoint(event.pos):
                    mouse_pos_active_button = pygame.mouse.get_pos()
                    self.exit_game_button(mouse_pos_active_button)

                elif self.buttons.rect_inactive.collidepoint(event.pos):
                    mouse_pos_inactive_button = pygame.mouse.get_pos()
                    self.start_game_button(mouse_pos_inactive_button)

    def set_conditions_active_game(self):
        # функция установки условий активности игры
        if self.settings.game_active:
            self.screen_class.handle_grid()
            self.buttons.draw_active_button()
            self.cube.draw_squares()

        else:
            self.buttons.draw_inactive_button()

    def exit_game_button(self, mouse_pos_active_button):
        # функция срабатывает когда кликаю мышью по кнопке "Завершить игру"
        button_clicked = self.buttons.rect_active.collidepoint(mouse_pos_active_button)

        if button_clicked and self.settings.game_active:
            self.exit_game()

    def start_game_button(self, mouse_pos_inactive_button):
        # функция срабатывает когда кликаю мышью по кнопке "Играть"
        button_clicked = self.buttons.rect_inactive.collidepoint(
            mouse_pos_inactive_button
        )

        if button_clicked and not self.settings.game_active:
            self.start_game()

    def exit_game(self):
        # функция выхода из игры
        self.settings.game_active = False
        self.screen_class.delete_grid()

    def start_game(self):
        # функция запуска игры
        self.settings.game_active = True
        self.screen_class.handle_grid()
