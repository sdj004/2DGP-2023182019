from pathlib import Path

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    close_canvas,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SHEET_WIDTH = 399
SHEET_HEIGHT = 525
SPRITE_SHEET_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
Frame = tuple[int, int, int, int]


def frame_rect(x: int, top: int, width: int, height: int) -> Frame:
    return (x, SHEET_HEIGHT - top - height, width, height)


FIRST_ACTION_FRAMES = (
    frame_rect(1, 39, 29, 39),
    frame_rect(31, 40, 26, 38),
    frame_rect(58, 39, 28, 39),
    frame_rect(86, 40, 30, 38),
    frame_rect(118, 40, 30, 38),
    frame_rect(150, 40, 30, 38),
    frame_rect(182, 40, 29, 38),
    frame_rect(211, 39, 29, 39),
    frame_rect(240, 39, 29, 39),
    frame_rect(270, 45, 24, 32),
    frame_rect(302, 51, 29, 26),
)

ADDITIONAL_ACTION_FRAMES = (
    (
        frame_rect(8, 80, 26, 37),
        frame_rect(37, 80, 27, 37),
        frame_rect(65, 80, 31, 38),
        frame_rect(97, 80, 37, 37),
        frame_rect(135, 80, 32, 35),
        frame_rect(170, 79, 32, 38),
        frame_rect(206, 79, 26, 38),
        frame_rect(238, 80, 24, 37),
        frame_rect(263, 80, 30, 37),
        frame_rect(295, 80, 36, 37),
        frame_rect(334, 80, 32, 36),
        frame_rect(370, 79, 29, 38),
    ),
    (
        frame_rect(1, 124, 33, 40),
        frame_rect(39, 124, 35, 39),
        frame_rect(89, 125, 35, 38),
        frame_rect(130, 121, 34, 42),
        frame_rect(181, 122, 34, 41),
        frame_rect(228, 122, 33, 40),
    ),
    (
        frame_rect(1, 169, 29, 30),
        frame_rect(35, 167, 29, 31),
        frame_rect(67, 169, 30, 29),
        frame_rect(98, 169, 31, 29),
        frame_rect(131, 168, 29, 30),
        frame_rect(162, 168, 29, 31),
        frame_rect(193, 170, 30, 29),
        frame_rect(230, 170, 31, 29),
    ),
    (
        frame_rect(1, 239, 29, 35),
        frame_rect(36, 239, 30, 35),
        frame_rect(74, 239, 31, 35),
        frame_rect(111, 238, 31, 36),
        frame_rect(149, 239, 30, 35),
        frame_rect(186, 238, 31, 36),
    ),
    (
        frame_rect(1, 283, 29, 35),
        frame_rect(36, 283, 30, 35),
        frame_rect(72, 286, 39, 31),
        frame_rect(123, 285, 39, 32),
        frame_rect(172, 286, 39, 31),
        frame_rect(218, 285, 38, 32),
    ),
    (
        frame_rect(1, 326, 24, 45),
        frame_rect(31, 327, 29, 44),
        frame_rect(65, 327, 20, 44),
        frame_rect(90, 327, 25, 43),
        frame_rect(119, 327, 25, 43),
        frame_rect(149, 327, 20, 44),
    ),
    (
        frame_rect(184, 341, 40, 28),
        frame_rect(232, 341, 39, 27),
    ),
    (
        frame_rect(1, 379, 27, 38),
        frame_rect(31, 379, 31, 36),
        frame_rect(64, 379, 31, 36),
        frame_rect(99, 377, 33, 38),
        frame_rect(136, 379, 32, 36),
        frame_rect(176, 379, 33, 36),
        frame_rect(217, 379, 33, 36),
        frame_rect(254, 378, 33, 36),
    ),
    (
        frame_rect(6, 429, 34, 40),
        frame_rect(49, 426, 34, 43),
        frame_rect(96, 427, 23, 39),
        frame_rect(125, 427, 23, 39),
    ),
)

Animation = tuple[str, tuple[Frame, ...]]
ANIMATIONS: tuple[Animation, ...] = (
    ("동작 1", FIRST_ACTION_FRAMES),
    ("동작 2", ADDITIONAL_ACTION_FRAMES[0]),
    ("동작 3", ADDITIONAL_ACTION_FRAMES[1]),
    ("동작 4", ADDITIONAL_ACTION_FRAMES[2]),
    ("동작 5", ADDITIONAL_ACTION_FRAMES[3]),
    ("동작 6", ADDITIONAL_ACTION_FRAMES[4]),
    ("동작 7", ADDITIONAL_ACTION_FRAMES[5]),
    ("동작 8", ADDITIONAL_ACTION_FRAMES[6]),
    ("동작 9", ADDITIONAL_ACTION_FRAMES[7]),
    ("동작 10", ADDITIONAL_ACTION_FRAMES[8]),
)


def main():
    try:
        sprite_sheet = load_image(str(SPRITE_SHEET_PATH))
    except Exception as error:
        raise SystemExit(
            f"스프라이트 시트를 불러올 수 없습니다: {SPRITE_SHEET_PATH}\n원인: {error}"
        ) from error

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    running = True

    while running:
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

        clear_canvas()
        source_x, source_y, frame_width, frame_height = FIRST_ACTION_FRAMES[0]
        sprite_sheet.clip_draw(
            source_x,
            source_y,
            frame_width,
            frame_height,
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
        )
        update_canvas()

    close_canvas()


if __name__ == "__main__":
    main()