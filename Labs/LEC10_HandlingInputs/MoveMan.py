from dataclasses import dataclass
from pathlib import Path

from pico2d import load_image, open_canvas

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


def load_assets():
    background = load_image(str(ASSET_DIRECTORY / "TUK_GROUND.png"))
    character = load_image(str(ASSET_DIRECTORY / "animation_sheet.png"))
    return background, character


def open_game_window():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)


def create_player_state():
    return PlayerState(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)