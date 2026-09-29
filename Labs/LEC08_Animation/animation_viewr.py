from pico2d import *

open_canvas()

grass = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\grass.png')
character = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\run_animation.png')

frame = 0
x = 0

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()

    frame = (frame + 1) % 8
    x += 5
    if x > 800:
        x = 0
    delay(0.05)

close_canvas()
