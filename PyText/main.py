from pyray import *
from text_box_class import text_box, text_box_x, text_box_y
from header_ui import header_ui_box, header_rect_info
from buttons import text_box_placing_button, text_box_moving_button
from pynput.keyboard import Key

text_box_list = []
buttons = [text_box_placing_button(100, 75, 75, 75, BLUE, False),
           text_box_moving_button(200, 75, 75, 75, BLUE, False)]




init_window(800, 900, "PyText")

header_ui = header_ui_box(0,0,900,150,WHITE)



while not window_should_close():

    begin_drawing()

    clear_background(GRAY)

    if buttons[0].status == True:
        if is_mouse_button_released(0) == True and check_collision_point_rec([get_mouse_x(), get_mouse_y()], header_rect_info) == False:
            generated_text_box = text_box(get_mouse_x(), get_mouse_y(), text_box_x, text_box_y, WHITE, [], [])
            text_box_list.append(generated_text_box)
            generated_text_box.generate_matrix()
    
    if buttons[1].status == True:
        for text_box_item in text_box_list:
            text_box_item.move()

    header_ui.draw()

    for text_box_item in text_box_list:
        text_box_item.draw()
        text_box_item.header_collide()
        text_box_item.text_input()
        text_box_item.fill_matrix()
        text_box_item.display_text()
        
    
    for button in buttons:
        button.draw()
        button.detect_input()
    
    end_drawing()

close_window()