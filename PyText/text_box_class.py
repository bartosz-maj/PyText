from pyray import *
from header_ui import header_rect_info

text_box_x = 200
text_box_y = 100

text_size = 10
row_text_space = 5

row_size = 20
row_number = 5



pressed_keys = []
letter_values = []
text_positions = []

text_matrix = []


class text_box:
    def __init__(self, pos_x, pos_y, size_x, size_y, color, pressed_keys, text_positions):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.pressed_keys = []
        self.text_positions = []
    
    def draw(self):
        draw_rectangle(int(self.pos_x - ((text_box_x * 1.05)/2)), int(self.pos_y - ((text_box_y * 1.1)/2)), int(self.size_x * 1.05), int(self.size_y * 1.1), BLACK)
        draw_rectangle(int(self.pos_x - (text_box_x / 2)), int(self.pos_y - (text_box_y / 2)), self.size_x, self.size_y, self.color)
    
    def header_collide(self):
        if check_collision_recs([int(self.pos_x - ((text_box_x * 1.05)/2)), int(self.pos_y - ((text_box_y * 1.1)/2)), int(self.size_x * 1.05), int(self.size_y * 1.1)], header_rect_info):
            self.pos_y = 160 + text_box_y/2
        else:
            pass
    
    def move(self):
        if is_mouse_button_down(0) and check_collision_point_rec([get_mouse_x(), get_mouse_y()], [int(self.pos_x - (text_box_x / 2)), int(self.pos_y - (text_box_y / 2)), self.size_x, self.size_y]):
            self.pos_y = get_mouse_y()
            self.pos_x = get_mouse_x()

    
    def generate_matrix(self):
        for i in range(0,row_number):
            text_matrix.append([])
            text_positions.append([])
        
        for i in text_matrix:
            for j in range(0,row_size):
                i.append([])
            
        for i in text_positions:
            for j in range(0,row_size):
                i.append([])
        
        row_index = 0
        column_index = 0

        start_x = int(self.pos_x - self.size_x/2) + 5
        start_y = int(self.pos_y - self.size_y/2)

        for i in range(0, (row_number * row_size)):
            print(row_index, column_index)
            text_positions[row_index][column_index] = [start_x + (row_text_space * column_index), start_y + (row_text_space * row_index)]
            column_index += 1
            start_x += row_text_space
            if column_index >= row_size:
                row_index += 1
                column_index = 0
                start_y += 8
                start_x = int(self.pos_x - self.size_x/2) + 5
        
        print(text_matrix)
            
    def text_input(self):
        
        pressed_keys.append(chr(get_key_pressed()))
       
        for count, value in enumerate(pressed_keys):
            if value == '\x00':
                del pressed_keys[count]

    def fill_matrix(self):
        row_index = 0
        column_index = 0

        if len(pressed_keys) > 0:
            for key in pressed_keys:
                text_matrix[row_index][column_index] = key
                column_index += 1
                if column_index >= row_size:
                    row_index += 1
                    column_index = 0
    
    def display_text(self):
        row_index = 0
        column_index = 0

        if len(pressed_keys) > 0:
            for key in pressed_keys:
                draw_text(text_matrix[row_index][column_index], text_positions[row_index][column_index][0], text_positions[row_index][column_index][1], text_size, BLACK)
                column_index += 1
                if column_index >= row_size:
                    row_index += 1
                    column_index = 0 




