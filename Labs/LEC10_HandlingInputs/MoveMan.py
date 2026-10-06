from dataclasses import dataclass
from pathlib import Path

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    SDLK_LEFT,
    SDLK_RIGHT,
    SDLK_DOWN,
    SDLK_UP,
    clear_canvas,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
SPRITE_SHEET_WIDTH = 802
SPRITE_SHEET_HEIGHT = 402
SPRITE_FRAME_SIZE = 100
SPRITE_FRAME_COUNT = 8
MOVE_STEP = 10
FRAME_INTERVAL = 0.05
ASSET_DIRECTORY = Path(__file__).resolve().parent


@dataclass
class PlayerState:
    x: int
    y: int
    facing_right: bool = True
    frame: int = 0
    moving: bool = False


def load_assets():
    background = load_image(str(ASSET_DIRECTORY / "TUK_GROUND.png"))
    character = load_image(str(ASSET_DIRECTORY / "animation_sheet.png"))
    return background, character


def open_game_window():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def create_player_state():
    return PlayerState(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)


def keep_player_on_screen(player):
    half_frame = SPRITE_FRAME_SIZE // 2
    player.x = min(max(player.x, half_frame), CANVAS_WIDTH - half_frame)
    player.y = min(max(player.y, half_frame), CANVAS_HEIGHT - half_frame)


def render_scene(background, character, player):
    clear_canvas()
    background.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    if player.moving:
        row = 2 if player.facing_right else 3
    else:
        row = 0 if player.facing_right else 1
    character.clip_draw(
        player.frame * SPRITE_FRAME_SIZE,
        SPRITE_SHEET_HEIGHT - (row + 1) * SPRITE_FRAME_SIZE,
        SPRITE_FRAME_SIZE,
        SPRITE_FRAME_SIZE,
        player.x,
        player.y,
    )
    update_canvas()


def handle_events(player):
    player.moving = False
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                player.x -= MOVE_STEP
                player.facing_right = False
                player.moving = True
            elif event.key == SDLK_RIGHT:
                player.x += MOVE_STEP
                player.facing_right = True
                player.moving = True
            elif event.key == SDLK_UP:
                player.y += MOVE_STEP
                player.moving = True
            elif event.key == SDLK_DOWN:
                player.y -= MOVE_STEP
                player.moving = True
    keep_player_on_screen(player)
    return True