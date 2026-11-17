import pygame

from settings import Settings
from screen import Screen
from events import Events


class Tetris:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.screen_class = Screen(self.screen)
        self.events = Events(self.screen)

        self.screen_class.screen_game()

        pygame.display.set_caption("Тетрис")

    def run_game(self):
        while True:
            self.screen_class.screen_game()

            self.screen.fill(self.settings.background_color)
            self.screen_class.handle_state_data()
            self.events.set_events()
            self.events.set_conditions_active_game()

            pygame.display.flip()

            # скорость цикла while
            self.clock.tick(60)


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
