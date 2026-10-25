import pygame

from settings import Settings


class Screen:
    def __init__(self, screen):
        self.settings = Settings()

        self.screen = screen

        self.color_main_lines = self.settings.color_lines

        self.vert_line_x_left = self.settings.x_start_area + 2
        self.vert_line_x_right = self.settings.x_end_area - 2
        self.x_start_area = self.settings.x_start_area
        self.y_start_area = self.settings.y_start_area
        self.x_end_area = self.settings.x_end_area
        self.y_end_area = self.settings.y_end_area
        self.background_color = self.settings.background_color
        self.w_cell = self.settings.w_cell
        self.h_cell = self.settings.h_cell
        self.font = pygame.font.SysFont("Arial", 15)
        self.text_color = "gray"

    # Функция перерисовки экрана
    def screen_game(self):
        self.screen.fill(self.background_color)
        self.handle_state_data()
        return self.screen

    # Функция отрисовки сетки
    def handle_grid(self):
        color = (59, 59, 59)
        y = self.y_start_area
        x = self.x_start_area

        while y < self.y_end_area:
            pygame.draw.line(
                self.screen,
                color,
                (self.x_start_area, y),
                (self.x_end_area + 2, y),
                1,
            )

            y = y + self.h_cell

        while x < self.x_end_area + 2:
            pygame.draw.line(
                self.screen,
                color,
                (x, self.y_start_area),
                (x, self.y_end_area),
                1,
            )

            x = x + self.w_cell

    # Функция отработки данных
    def handle_state_data(self):
        self.handle_grid()

        self.score_text = self.font.render("Счет", True, self.text_color)
        self.level_text = self.font.render("Уровень", True, self.text_color)
        self.blocks_text = self.font.render("Блоков", True, self.text_color)
        self.high_score_text = self.font.render("Лучший счет", True, self.text_color)
        self.next = self.font.render("Следующий", True, self.text_color)

        self.screen.blit(self.score_text, [550, self.y_start_area])
        self.screen.blit(self.level_text, [530, 70])
        self.screen.blit(self.blocks_text, [535, 120])
        self.screen.blit(self.high_score_text, [495, 180])
        self.screen.blit(self.next, [495, 350])

        pygame.draw.line(
            self.screen,
            self.color_main_lines,
            (self.vert_line_x_left, self.y_start_area),
            (self.vert_line_x_left, self.y_end_area),
            2,
        )

        pygame.draw.line(
            self.screen,
            self.color_main_lines,
            (self.x_start_area, self.y_end_area),
            (self.x_end_area, self.y_end_area),
            2,
        )

        pygame.draw.line(
            self.screen,
            self.color_main_lines,
            (self.vert_line_x_right, self.y_start_area),
            (self.vert_line_x_right, self.y_end_area),
            2,
        )

        pygame.display.update()
