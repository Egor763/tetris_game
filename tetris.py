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
from exit_game import ExitGame
from start_game import StartGame
from mousebuttondown_events import MousebuttondownEvents


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
        self.exit_game = ExitGame(self.screen)
        self.start_game = StartGame(self.screen)
        self.mousebuttondown_events = MousebuttondownEvents(self.screen)

        self.screen_class.screen_game()

        self.h_cell = self.settings.h_cell
        self.current_block = self.settings.current_block
        self.key_button = self.settings.key_button

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
                            # self._exit_game()
                            self.exit_game.game_over()

                    else:
                        # * запуск игры при нажатии на пробел
                        if event.key == pygame.K_RETURN:
                            self.start_game.game_launch()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousebuttondown_events.set_listener(event)

            if self.settings.game_active:
                # если игра активна вызывается класс game_active
                self.game_active_class.screen_active()
                self.game_active_class.draw_squares()

                self.game_active_class.set_timer(event)

            else:
                # если игра неактивна вызывается класс game_inactive
                self.game_inactive_class.screen_inactive()

            pygame.display.flip()

            # скорость цикла while
            self.clock.tick(60)


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
