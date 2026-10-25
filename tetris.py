import pygame

from settings import Settings
from screen import Screen


class Tetris:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.window_size)

        self.screen_class = Screen(self.screen)

        self.screen_class.screen_game()

        self.screen_class.handle_state_data()

        pygame.display.set_caption("Тетрис")

    def run_game(self):
        self.screen_class.screen_game()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
