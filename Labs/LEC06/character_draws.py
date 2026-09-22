from pico2d import *

open_canvas(800, 600)
character = load_image("character.png")
def move_circle():
    print("CIRCLE")
    #캐릭터 이미지 표시
    clear_canvas()
    character.draw(400, 300)
    update_canvas()

def move_rectangle():
    print("RECTANGLE")

def move_triangle():
    print("TRIANGLE")

while True: #함수호출을 합니다.
    move_circle()
    move_rectangle()
    move_triangle()
    