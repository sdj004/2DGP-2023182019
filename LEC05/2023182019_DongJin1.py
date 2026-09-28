from pico2d import *

width = 800
height = 600

open_canvas(width, height)

character_xpos = 21
character_ypos = 46 + 41

move_up = False
move_right = True
move_left = False
move_down = False

character = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\LEC05\\character.png')
Grass = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\LEC05\\grass.png')

while True:
    if move_right and character_xpos + 10 < width - 21: 
        character_xpos += 10
    elif move_right : 
        move_right = False
        move_up = True

    if move_left and character_xpos - 10 > 21: 
            character_xpos -= 10
    elif move_left : 
        move_left = False
        move_down = True

    if move_up and character_ypos + 10 < height - 46: 
            character_ypos += 10
    elif move_up : 
        move_up = False
        move_left = True

    if move_down and character_ypos - 10 > 46 + 41: 
        character_ypos -= 10
    elif move_down : 
        move_down = False
        move_right = True

   
    Grass.draw(401, 32)
    character.draw(character_xpos, character_ypos)
    update_canvas()
    clear_canvas()
    delay(0.05)

close_canvas()