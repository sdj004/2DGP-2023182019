from pico2d import *
import pico2d.pico2d as p2d

# 1. 화면 창 생성 (600 x 400 = 240,000 px^2)
open_canvas(600, 400)

# 2. 지정해주신 절대 경로로 이미지 로드
sprite_sheet = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\dongkeykong.png')

# -------------------------------------------------------------
# [각 행별 정밀 타이트 바운딩 박스 (x, y, w, h) 세팅]
# 너비를 실제 캐릭터 영역으로 슬림화하여 좌우 이동 흔들림 방지
# -------------------------------------------------------------

# Row 1 (맨 아래 행): 구르기 동작 9프레임 (너비 38px로 축소 및 정밀 배치)
# dongkeykong.png (크기: 450 x 334 px)
# Pico2D 전용 좌표: [left_x, bottom_y, width, height]

ANIMATION_ROWS = [

    # [3행 - 위에서 3번째] (총 12 프레임)
    [
        (12, 169, 36, 52), (50, 169, 36, 52), (88, 169, 36, 52),
        (126, 169, 36, 52), (164, 169, 36, 52), (202, 169, 36, 52),
        (234, 169, 36, 52), (274, 169, 36, 52), (314, 169, 36, 52),
        (352, 169, 36, 52), (388, 169, 36, 52), (426, 169, 36, 52)
    ],

    # [4행 - 위에서 4번째] 발 부분 잘림 해결을 위해 높이 48px로 확장 및 bottom_y 120으로 다운 (총 9 프레임)
    [
        (0, 120, 52, 48), (48, 120, 52, 48), (96, 120, 52, 48),
        (144, 120, 52, 48), (194, 120, 52, 48), (245, 120, 52, 48),
        (296, 120, 52, 48), (346, 120, 52, 48), (396, 120, 52, 48)
    ],

    # [5행 - 위에서 5번째] (총 7 프레임)
    [
        (0, 62, 68, 49), (54, 62, 68, 49), (117, 62, 68, 49),
        (182, 62, 68, 49), (254, 62, 68, 49), (329, 62, 68, 49),
        (409, 62, 68, 49)
    ],

    # [6행 - 맨 아래] (총 9 프레임)
    [
        (0, 4, 47, 41), (49, 4, 47, 41), (96, 4, 47, 41),
        (144, 4, 47, 41), (193, 4, 47, 41), (242, 4, 47, 41),
        (295, 4, 47, 41), (350, 4, 47, 41), (405, 4, 47, 41)
    ]
]

# 애니메이션 전체 테이블


# 애니메이션 제어 변수
row_index = 0
frame_index = 0
running = True

# 화면 점유율 20% 계산 (48,000 px^2)
CANVAS_AREA_20PERCENT = 600 * 400 * 0.20

def get_scaled_draw_size(src_w, src_h):
    scale = (CANVAS_AREA_20PERCENT / (src_w * src_h)) ** 0.5
    return int(src_w * scale), int(src_h * scale)

# -------------------------------------------------------------
# 캔버스 검정색 Fill 함수 (pico2d/SDL2 Direct Render)
# -------------------------------------------------------------
def clear_canvas_with_color(r=0, g=0, b=0):
    clear_canvas()
    p2d.SDL_SetRenderDrawColor(p2d.renderer, r, g, b, 255)
    rect = p2d.SDL_Rect(0, 0, 600, 400)
    p2d.SDL_RenderFillRect(p2d.renderer, rect)


while running:
    # 캔버스 검정색 클리어
    clear_canvas_with_color(0, 0, 0)

    # 이벤트 처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    # 현재 프레임 정보 가져오기
    current_row_frames = ANIMATION_ROWS[row_index]
    sx, sy, sw, sh = current_row_frames[frame_index]
    
    # 20% 점유율 크기 계산
    draw_w, draw_h = get_scaled_draw_size(sw, sh)

    # (300, 200) 피벗 고정 렌더링
    sprite_sheet.clip_draw(sx, sy, sw, sh, 300, 200, draw_w, draw_h)

    # 프레임 진행
    frame_index += 1
    if frame_index >= len(current_row_frames):
        frame_index = 0
        row_index = (row_index + 1) % len(ANIMATION_ROWS)

    update_canvas()
    
    # 속도 조절 (0.1초)
    delay(0.1)

close_canvas()