import pygame

from settings import Settings
from screen import Screen
from button_active import ButtonActive
from button_inactive import ButtonInactive
from blocks import Blocks
from move_blocks import MoveBlocks
from cube import Cube
from game_active import GameActive
from game_inactive import GameInactive


class Tetris:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.screen_class = Screen(self.screen)
        self.button_active_class = ButtonActive(self.screen, "Завершить игру")
        self.button_inactive_class = ButtonInactive(self.screen, "Играть")
        self.blocks = Blocks(self.screen)
        self.move_blocks = MoveBlocks(self.screen)
        self.cube = Cube()
        self.game_active_class = GameActive(self.screen, "Завершить игру")
        self.game_inactive_class = GameInactive(self.screen, "Играть")

        self.screen_class.screen_game()

        self.USEREVENT = pygame.USEREVENT
        self.delay_time = 300
        pygame.time.set_timer(self.USEREVENT, self.delay_time)

        self.h_cell = self.settings.h_cell
        self.current_block = self.settings.current_block
        self.key_button = self.settings.key_button

        # self._draw_squares()
        pygame.display.set_caption("Тетрис")

    def run_game(self):

        while True:
            self.screen_class.screen_game()

            self.screen.fill(self.settings.background_color)
            self.screen_class.handle_state_data()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

                    if self.settings.game_active:
                        # * выход из игры при нажатии на кнопку i
                        if event.key == pygame.K_i:
                            self._exit_game()

                    else:
                        # * запуск игры при нажатии на пробел
                        if event.key == pygame.K_RETURN:
                            self._start_game()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_active_class.rect.collidepoint(event.pos):
                        mouse_pos = pygame.mouse.get_pos()
                        self._check_play_button(mouse_pos)

                    elif self.button_inactive_class.rect_inactive.collidepoint(
                        event.pos
                    ):
                        mouse_pos_inactive_button = pygame.mouse.get_pos()
                        self._check_play_inactive_button(mouse_pos_inactive_button)

            if self.settings.game_active:
                # если игра активна вызывается класс game_active
                self.game_active_class.screen_active()
                self._draw_squares()
                if event.type == self.USEREVENT and not bool(self.key_button):
                    self.game_active_class.set_timer()

            else:
                # если игра неактивна вызывается класс game_inactive
                self.game_inactive_class.screen_inactive()

            pygame.display.flip()

            # скорость цикла while
            self.clock.tick(60)

    def _exit_game(self):
        # функция выхода из игры
        self.settings.game_active = False

        self.screen_class.delete_grid()

    def _start_game(self):
        # функция запуска игры
        self.settings.game_active = True

        self.screen_class.handle_grid()

    def _check_play_button(self, mouse_pos):
        button_clicked = self.button_active_class.rect.collidepoint(mouse_pos)

        if button_clicked and self.settings.game_active:
            self._exit_game()

    def _check_play_inactive_button(self, mouse_pos_inactive_button):
        button_clicked = self.button_inactive_class.rect_inactive.collidepoint(
            mouse_pos_inactive_button
        )

        if button_clicked and not self.settings.game_active:
            self._start_game()

    def _draw_squares(self):
        if self.settings.game_active:
            self.blocks.draw_figurs()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
