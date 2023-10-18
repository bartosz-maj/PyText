from pyray import *

button_x = 75
button_y = 75

class text_box_placing_button:
    def __init__(self, pos_x, pos_y, size_x, size_y, color, status):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.status = False
    
    def draw(self):
        draw_rectangle(int(self.pos_x - (button_x / 2)), int(self.pos_y - (button_y / 2)), self.size_x, self.size_y, self.color)
    

    def detect_input(self):
        if check_collision_point_rec([get_mouse_x(), get_mouse_y()], [int(self.pos_x - (button_x / 2)), int(self.pos_y - (button_y / 2)), self.size_x, self.size_y]):
            if is_mouse_button_released(0) and self.color == BLUE:
                self.color = RED
                self.status = True
            elif is_mouse_button_released(0) and self.color == RED:
                self.color = BLUE
                self.status = False
        else:
            pass

class text_box_moving_button:
    def __init__(self, pos_x, pos_y, size_x, size_y, color, status):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.status = False
    
    def draw(self):
        draw_rectangle(int(self.pos_x - (button_x / 2)), int(self.pos_y - (button_y / 2)), self.size_x, self.size_y, self.color)
    

    def detect_input(self):
        if check_collision_point_rec([get_mouse_x(), get_mouse_y()], [int(self.pos_x - (button_x / 2)), int(self.pos_y - (button_y / 2)), self.size_x, self.size_y]):
            if is_mouse_button_released(0) and self.color == BLUE:
                self.color = RED
                self.status = True
            elif is_mouse_button_released(0) and self.color == RED:
                self.color = BLUE
                self.status = False
        else:
            pass