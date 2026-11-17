import pygame.font

from settings import Settings


class Buttons:
    # ! msg_active это "Завершить игру" а msg_inactive это "Играть"!!!
    def __init__(self, screen, msg_active, msg_inactive):
        self.settings = Settings()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_active = self.settings.game_active

        self.button_width = 300
        self.button_height = 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)
        self.button_active_color = (0, 0, 255)
        self.button_inactive_color = (0, 100, 0)

        self.rect_active = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect_inactive = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect_active.midbottom = self.screen_rect.midbottom
        self.rect_inactive.center = self.screen_rect.center

        self.button_active_msg(msg_active)
        self.button_inactive_msg(msg_inactive)

    def button_active_msg(self, msg_active):
        self.msg_active_image = self.font.render(
            msg_active, True, self.text_color, self.button_active_color
        )
        self.msg_active_image_rect = self.msg_active_image.get_rect()
        self.msg_active_image_rect.center = self.rect_active.center

    def button_inactive_msg(self, msg_inactive):
        self.msg_inactive_image = self.font.render(
            msg_inactive, True, self.text_color, self.button_inactive_color
        )
        self.msg_inactive_image_rect = self.msg_inactive_image.get_rect()
        self.msg_inactive_image_rect.center = self.rect_inactive.center

    def draw_active_button(self):
        # отрисовка кнопки "Завершить игру"
        self.screen.fill(self.button_active_color, self.rect_active)
        self.screen.blit(self.msg_active_image, self.msg_active_image_rect)

    def draw_inactive_button(self):
        # отрисовка кнопки "Играть"
        self.screen.fill(self.button_inactive_color, self.rect_inactive)
        self.screen.blit(self.msg_inactive_image, self.msg_inactive_image_rect)
