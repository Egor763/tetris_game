from button_inactive import ButtonInactive


class GameInactive:
    def __init__(self, screen, msg):
        self.button_inactive_class = ButtonInactive(screen, msg)

    def screen_inactive(self):
        self.button_inactive_class.draw_inactive_button()
