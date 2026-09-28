from pico2d import *
import math

open_canvas(800, 600)
r = 100
character = load_image("C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\LEC05\\character.png")
def move_circle(degree):
    print("CIRCLE")
    #캐릭터 이미지 표시
    for Degree in range(degree):
        clear_canvas()
        theta = math.radians(Degree)
        x = 400 + r * math.cos(theta)
        y = 300 + r * math.sin(theta) 
        character.draw(x, y)
        update_canvas()
        delay(0.005)

def draw_right():
    pass

def draw_top():
    pass

def draw_left():
    pass

def draw_bottom():
    pass


def move_rectangle():
    print("RECTANGLE")
    draw_right()
    draw_top()
    draw_left()
    draw_bottom()


def move_triangle():
    print("TRIANGLE")

while True: #함수호출을 합니다.
    move_circle(360)
    move_rectangle()
    move_triangle()
    