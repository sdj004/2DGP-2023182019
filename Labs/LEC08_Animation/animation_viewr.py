from pico2d import *

# 1. 화면 창 생성 (600x400)
open_canvas(600, 400)

# 2. 배경 지우기 색상 설정 (밝은 회색 배경으로 스프라이트 확인)
clear_canvas()

# 3. 변경한 검은색 배경 스프라이트 시트 로드
# (파일 이름은 저장한 파일명에 맞게 변경하세요)
sprite_sheet = load_image('C:\\PythonStudy\\2D_gameProgramming\\2DGP-2023182019\\Labs\\LEC08_Animation\\dongkeykong.png')

# 맨 아래 행(Row 1) 고정 프레임 정보 설정
FRAME_COUNT = 9            # 맨 아래 행 총 프레임 수
FRAME_WIDTH = 41           # 균일 가로 크기 (px)
FRAME_HEIGHT = 41          # 균일 세로 크기 (px)

# 원본 이미지 상에서 맨 아래 행(Row 1)의 위치 정보
# 원본 이미지 높이: 335px / Row 1 영역: y = 291~331 (pico2d는 좌상단/좌하단 좌표 확인 필요)
ROW1_START_X = 0           # 첫 번째 프레임 시작 X 좌표
ROW1_START_Y = 4           # pico2d(좌하단 기준 0) 기준 맨 아래 행 Y 시작 오프셋

running = True
frame = 0

# 메인 루프
while running:
    clear_canvas()
    
    # 이벤트 처리 (창 닫기, ESC 키 종료)
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    # 현재 프레임의 X, Y 좌표 계산
    # Row 1의 9개 프레임 순회
    source_x = ROW1_START_X + (frame * FRAME_WIDTH)
    source_y = ROW1_START_Y

    # pico2d의 clip_draw를 사용하여 프레임별로 정확히 잘라서 화면 중앙(300, 200)에 렌더링
    # clip_draw(left, bottom, width, height, dest_x, dest_y, [scale_w, scale_h])
    # 2배 확대(82x82)하여 선명하게 출력
    sprite_sheet.clip_draw(source_x, source_y, FRAME_WIDTH, FRAME_HEIGHT, 300, 200, 82, 82)
    
    update_canvas()
    
    # 다음 프레임으로 이동 (0 ~ 8 순환)
    frame = (frame + 1) % FRAME_COUNT
    
    # 애니메이션 속도 조절 (약 10 FPS)
    delay(0.1)

close_canvas()