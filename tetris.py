import pygame

from settings import Settings
from screen import Screen
from button_active import ButtonActive


class Tetris:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.screen_class = Screen(self.screen)
        self.button_active_class = ButtonActive(self.screen, "Завершить игру")

        self.screen_class.screen_game()

        # self.screen_class.handle_state_data()

        pygame.display.set_caption("Тетрис")

    def run_game(self):
        self.screen_class.screen_game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

                    elif event.key == pygame.K_i:
                        self._exit_game()
                        print("выход из игры при нажатии на i")

                        print(
                            f"состояние ключа при нажатии на i: {self.settings.game_active}"
                        )

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("выход из игры при нажатии на кнопку")
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    print(
                        f"состояние ключа при нажатии на кнопку: {self.settings.game_active}"
                    )

            if self.settings.game_active:
                self.screen_class.handle_state_data()
                self.button_active_class.draw_button()

            pygame.display.update()

    def _exit_game(self):
        print("выход из игры")
        self.settings.game_active = False

        self.screen_class.delete_grid()

        pygame.display.update()

    def _check_play_button(self, mouse_pos):
        button_clicked = self.button_active_class.rect.collidepoint(mouse_pos)

        if button_clicked and self.settings.game_active:
            self._exit_game()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
