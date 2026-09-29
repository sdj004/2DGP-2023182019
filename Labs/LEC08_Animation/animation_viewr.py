from pico2d import *
import pico2d.pico2d as p2d  # pico2d 내부 SDL 렌더러 접근용

# 1. 화면 창 생성
open_canvas(600, 400)

# 2. 지정해주신 절대 경로로 이미지 로드
sprite_sheet = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\dongkeykong.png')

# -------------------------------------------------------------
# [스프라이트 시트 각 행(Row) 애니메이션 설정]
# -------------------------------------------------------------
ROW1_FRAME_COUNT = 9
ROW1_FRAME_WIDTH = 41
ROW1_FRAME_HEIGHT = 41
ROW1_START_Y = 4

ROW2_FRAME_COUNT = 7
ROW2_FRAME_WIDTH = 70
ROW2_FRAME_HEIGHT = 49
ROW2_START_Y = 62

ROW3_FRAME_COUNT = 9
ROW3_FRAME_WIDTH = 46
ROW3_FRAME_HEIGHT = 40
ROW3_START_Y = 125

ROW4_FRAME_COUNT = 12
ROW4_FRAME_WIDTH = 33
ROW4_FRAME_HEIGHT = 51
ROW4_START_Y = 169

ROW5_FRAME_COUNT = 12
ROW5_FRAME_WIDTH = 38
ROW5_FRAME_HEIGHT = 50
ROW5_START_Y = 230

ROW6_FRAME_COUNT = 11
ROW6_FRAME_WIDTH = 40
ROW6_FRAME_HEIGHT = 42
ROW6_START_Y = 288

# 애니메이션 제어 변수 (1 -> 2 -> 3 -> 4 -> 5 -> 6 순서로 전환)
current_row = 1
frame = 0
running = True

# -------------------------------------------------------------
# 캔버스 검정색 Fill 함수 (pico2d/SDL2 렌더러 직접 제어)
# -------------------------------------------------------------
def clear_canvas_with_color(r=0, g=0, b=0):
    clear_canvas()
    # SDL2 렌더러 색상 지정 (RGB: 0, 0, 0 = 검정색)
    p2d.SDL_SetRenderDrawColor(p2d.renderer, r, g, b, 255)
    # 전체 캔버스 윈도우 영역 채우기
    rect = p2d.SDL_Rect(0, 0, 600, 400)
    p2d.SDL_RenderFillRect(p2d.renderer, rect)


while running:
    # 캔버스 백버퍼를 검정색(0, 0, 0)으로 클리어 & 채우기
    clear_canvas_with_color(0, 0, 0)

    # 이벤트 처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    # -------------------------------------------------------------
    # 행 상태에 따른 프레임 렌더링 및 순차 전환 처리
    # -------------------------------------------------------------
    if current_row == 1:
        source_x = frame * ROW1_FRAME_WIDTH
        source_y = ROW1_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW1_FRAME_WIDTH, ROW1_FRAME_HEIGHT, 300, 200, 82, 82)
        
        frame += 1
        if frame >= ROW1_FRAME_COUNT:
            frame = 0
            current_row = 2

    elif current_row == 2:
        source_x = frame * ROW2_FRAME_WIDTH
        source_y = ROW2_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW2_FRAME_WIDTH, ROW2_FRAME_HEIGHT, 300, 200, 140, 98)
        
        frame += 1
        if frame >= ROW2_FRAME_COUNT:
            frame = 0
            current_row = 3

    elif current_row == 3:
        source_x = frame * ROW3_FRAME_WIDTH
        source_y = ROW3_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW3_FRAME_WIDTH, ROW3_FRAME_HEIGHT, 300, 200, 92, 80)
        
        frame += 1
        if frame >= ROW3_FRAME_COUNT:
            frame = 0
            current_row = 4

    elif current_row == 4:
        source_x = frame * ROW4_FRAME_WIDTH
        source_y = ROW4_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW4_FRAME_WIDTH, ROW4_FRAME_HEIGHT, 300, 200, 66, 102)
        
        frame += 1
        if frame >= ROW4_FRAME_COUNT:
            frame = 0
            current_row = 5

    elif current_row == 5:
        source_x = frame * ROW5_FRAME_WIDTH
        source_y = ROW5_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW5_FRAME_WIDTH, ROW5_FRAME_HEIGHT, 300, 200, 76, 100)
        
        frame += 1
        if frame >= ROW5_FRAME_COUNT:
            frame = 0
            current_row = 6

    elif current_row == 6:
        source_x = frame * ROW6_FRAME_WIDTH
        source_y = ROW6_START_Y
        sprite_sheet.clip_draw(source_x, source_y, ROW6_FRAME_WIDTH, ROW6_FRAME_HEIGHT, 300, 200, 80, 84)
        
        frame += 1
        if frame >= ROW6_FRAME_COUNT:
            frame = 0
            current_row = 1  # 맨 아래 행으로 순환

    update_canvas()
    
    # 애니메이션 속도 조절 (약 10 FPS)
    delay(0.1)

close_canvas()