from pico2d import *
import math

open_canvas(800, 600)
r = 300
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
    return x, y
        

def draw_top(x, y):
    while y < 550:
        y += 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y

def draw_half_top(x, y):
    while y < 300:
        y += 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y

def draw_left(x, y):
    while x > 50:
        x -= 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y

def draw_bottom(x, y):
    while y > 50:
        y -= 5
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y


def move_rectangle(x, y):
    print("RECTANGLE")
    x, y = draw_right(x, y)
    x, y = draw_top(x, y)
    x, y = draw_left(x, y)
    x, y = draw_bottom(x, y)

    return x, y


def draw_leftop(x, y):
    print("lefttop")
    xgap = x - 400
    ygap = 600 - y

    xmove = xgap / 100
    ymove = ygap / 100
    for _ in range(100):
        x -= xmove
        y += ymove
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y

def draw_leftbottom(x, y):
    print("leftbottom")

    xgap = x
    ygap = y - 50
    
    xmove = xgap / 100
    ymove = ygap / 100
    
    for _ in range(100):
        x -= xmove
        y -= ymove
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)
    return x, y

def move_triangle(x, y):
    print("TRIANGLE")
    x, y = draw_right(x, y)
    x, y = draw_leftop(x, y)
    x, y = draw_leftbottom(x, y)
    return x, y

def Set_circle_pos(x, y):
    return x, y

while True: #함수호출을 합니다.
    x, y = move_circle(360)
    x, y = move_rectangle(x, y)
    x, y = move_triangle(x, y)
    x, y = draw_right(x, y)
    x, y = draw_half_top(x, y)
    x, y = Set_circle_pos(x, y)
    