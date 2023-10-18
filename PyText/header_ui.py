from pyray import *

header_rect_info = [0,0,900,150]

class header_ui_box:
    def __init__(self, pos_x, pos_y, size_x, size_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
    
    def draw(self):
        draw_rectangle(self.pos_x, self.pos_y, self.size_x, self.size_y, self.color)