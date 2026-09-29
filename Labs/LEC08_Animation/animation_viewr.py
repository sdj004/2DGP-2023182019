from pico2d import *

# 1. 화면 창 생성
open_canvas(600, 400)
clear_canvas()

# 2. 지정해주신 절대 경로로 이미지 로드
sprite_sheet = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\dongkeykong.png')

# -------------------------------------------------------------
# [행 1: 맨 아래 행 애니메이션 설정] - 총 9 프레임
# -------------------------------------------------------------
ROW1_FRAME_COUNT = 9
ROW1_FRAME_WIDTH = 41
ROW1_FRAME_HEIGHT = 41
ROW1_START_Y = 4            # pico2d 좌하단 기준 Y 오프셋

# -------------------------------------------------------------
# [행 2: 아래에서 2번째 행 애니메이션 설정] - 총 7 프레임
# -------------------------------------------------------------
ROW2_FRAME_COUNT = 7
ROW2_FRAME_WIDTH = 70
ROW2_FRAME_HEIGHT = 49
ROW2_START_Y = 62           # pico2d 좌하단 기준 Y 오프셋

# -------------------------------------------------------------
# [행 3: 아래에서 3번째 행 애니메이션 설정] - 총 9 프레임 (새로 추가)
# -------------------------------------------------------------
ROW3_FRAME_COUNT = 9
ROW3_FRAME_WIDTH = 46
ROW3_FRAME_HEIGHT = 40
ROW3_START_Y = 125          # pico2d 좌하단 기준 Y 오프셋

# 애니메이션 제어 변수
current_row = 1             # 현재 재생 중인 행 (1 -> 2 -> 3 순서로 전환)
frame = 0                   # 현재 프레임 인덱스
running = True

while running:
    clear_canvas()
    
    # 키 및 창 닫기 이벤트 처리
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
        # Row 1 (맨 아래 행) 렌더링
        source_x = frame * ROW1_FRAME_WIDTH
        source_y = ROW1_START_Y
        
        # 2배 확대(82x82)
        sprite_sheet.clip_draw(source_x, source_y, ROW1_FRAME_WIDTH, ROW1_FRAME_HEIGHT, 300, 200, 82, 82)
        
        frame += 1
        if frame >= ROW1_FRAME_COUNT:
            frame = 0
            current_row = 2  # Row 1 종료 -> Row 2로 이동
            
    elif current_row == 2:
        # Row 2 (아래에서 2번째 행) 렌더링
        source_x = frame * ROW2_FRAME_WIDTH
        source_y = ROW2_START_Y
        
        # 2배 확대(140x98)
        sprite_sheet.clip_draw(source_x, source_y, ROW2_FRAME_WIDTH, ROW2_FRAME_HEIGHT, 300, 200, 140, 98)
        
        frame += 1
        if frame >= ROW2_FRAME_COUNT:
            frame = 0
            current_row = 3  # Row 2 종료 -> Row 3으로 이동

    elif current_row == 3:
        # Row 3 (아래에서 3번째 행) 렌더링
        source_x = frame * ROW3_FRAME_WIDTH
        source_y = ROW3_START_Y
        
        # 2배 확대(92x80)
        sprite_sheet.clip_draw(source_x, source_y, ROW3_FRAME_WIDTH, ROW3_FRAME_HEIGHT, 300, 200, 92, 80)
        
        frame += 1
        if frame >= ROW3_FRAME_COUNT:
            frame = 0
            current_row = 1  # Row 3 종료 -> 다시 Row 1로 순환 연결

    update_canvas()
    
    # 애니메이션 속도 조절 (약 10 FPS)
    delay(0.1)

close_canvas()