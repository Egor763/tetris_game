import pygame.font


class ButtonActive:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # атрибуты кнопки
        self.button_width = 300
        self.button_height = 50
        self.text_color = (255, 255, 255)
        self.button_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 50)

        # координаты кнопки
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.midbottom = self.screen_rect.midbottom

        # сообщение кнопки
        self.button_msg(msg)

    def button_msg(self, msg):
        # преобразует rect в прямоугольник и выравнивает текст по центру
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # отрисовывает кнопку
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
