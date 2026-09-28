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
    return x, y

def draw_right(x, y):
    while x < 750:
        x += 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
        

def draw_top(x, y):
     while y < 550:
        y += 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)

def draw_left(x, y):
    pass

def draw_bottom(x, y):
    pass


def move_rectangle(x, y):
    print("RECTANGLE")
    draw_right(x, y)
    draw_top(x, y)
    draw_left(x, y)
    draw_bottom(x, y)


def move_triangle():
    print("TRIANGLE")

while True: #함수호출을 합니다.
    x, y = move_circle(360)
    move_rectangle(x, y)
    move_triangle()
    