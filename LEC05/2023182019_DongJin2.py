from pico2d import *
import math

width = int(800)
height = int(600)
xmove = 10
gap = 0
open_canvas(width, height)

character_xpos = width // 2
character_ypos = height // 2
half_R = math.sqrt(math.pow(height // 2 - 32 + 42, 2)) - 100



move_right = True
move_left = False

character = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\LEC05\\character.png')
Grass = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\LEC05\\grass.png')

while True:

    if move_right and math.pow(width // 2 - character_xpos - xmove, 2) <= math.pow(half_R, 2) :
        character_xpos += xmove
        character_ypos = height // 2 + math.sqrt(math.pow(half_R, 2) - math.pow(width // 2 - character_xpos, 2))

    elif move_right:
        move_right = False
        move_left = True
        gap = character_xpos - width // 2
        character_xpos + xmove

    if move_left and  character_xpos - xmove >= width // 2 - gap:
        character_xpos -= xmove
        character_ypos = height // 2 -math.sqrt(math.pow(half_R, 2) - math.pow(width // 2 - character_xpos, 2))

    elif move_left:
        move_right = True
        move_left = False
        character_xpos - xmove

   
    Grass.draw(401, 32)
    character.draw(character_xpos, character_ypos)
    update_canvas()
    clear_canvas()
    delay(0.1)

