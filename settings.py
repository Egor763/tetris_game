class Settings:
    def __init__(self):
        self.W = 600
        self.H = 700
        self.window_size = (self.W, self.H)
        self.color_lines = (255, 255, 255)

        # Границы игровой области
        self.y_start_area = 10
        self.x_start_area = 50
        self.y_end_area = 610
        self.x_end_area = 350

        # Размеры ячеек
        self.w_cell = 30
        self.h_cell = 30

        self.background_color = (0, 0, 0)
