import pygame.font


class ButtonInactive:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        print(f"screen в button_inactive: {self.screen}")

        # атрибуты кнопки
        self.button_inactive_width = 300
        self.button_inactive_height = 50
        self.text_inactive_color = (255, 255, 255)
        self.button_inactive_color = (0, 100, 0)
        self.font_inactive = pygame.font.SysFont(None, 50)

        # координаты кнопки
        self.rect_inactive = pygame.Rect(
            0, 0, self.button_inactive_width, self.button_inactive_height
        )
        self.rect_inactive.center = self.screen_rect.center

        # сообщение кнопки
        self.button_inactive_msg(msg)

    def button_inactive_msg(self, msg):
        # преобразует rect в прямоугольник и выравнивает текст по центру
        self.msg_inactive_image = self.font_inactive.render(
            msg, True, self.text_inactive_color, self.button_inactive_color
        )
        self.msg_inactive_image_rect = self.msg_inactive_image.get_rect()
        self.msg_inactive_image_rect.center = self.rect_inactive.center

    def draw_inactive_button(self):
        # отрисовывает кнопку и текст кнопки
        self.screen.fill(self.button_inactive_color, self.rect_inactive)
        self.screen.blit(self.msg_inactive_image, self.msg_inactive_image_rect)
