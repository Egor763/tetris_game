import pygame

from settings import Settings
from screen import Screen
from button_active import ButtonActive
from button_inactive import ButtonInactive


class Tetris:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.screen_class = Screen(self.screen)
        self.button_active_class = ButtonActive(self.screen, "Завершить игру")
        self.button_inactive_class = ButtonInactive(self.screen, "Играть")

        self.screen_class.screen_game()

        # self.screen_class.handle_state_data()

        pygame.display.set_caption("Тетрис")

    def run_game(self):
        self.screen_class.screen_game()

        while True:
            # скорость цикла while
            self.clock.tick(60)
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
                # если игра активна отрисовываются игровое поле, данные и кнопка "Завершить игру"
                self.screen_class.handle_grid()
                self.button_active_class.draw_button()

            else:
                # если игра неактивна отрисовываются данные и кнопка "Играть"
                self.button_inactive_class.draw_inactive_button()

            pygame.display.flip()

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


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
