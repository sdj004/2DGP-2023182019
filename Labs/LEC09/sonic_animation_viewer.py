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
SPRITE_SHEET_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")


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
        update_canvas()

    close_canvas()


if __name__ == "__main__":
    main()