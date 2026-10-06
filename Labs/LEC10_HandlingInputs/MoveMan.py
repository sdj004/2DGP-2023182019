from pathlib import Path

from pico2d import load_image

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
SPRITE_SHEET_WIDTH = 802
SPRITE_SHEET_HEIGHT = 402
SPRITE_FRAME_SIZE = 100
SPRITE_FRAME_COUNT = 8
MOVE_STEP = 10
FRAME_INTERVAL = 0.05
ASSET_DIRECTORY = Path(__file__).resolve().parent


def load_assets():
    background = load_image(str(ASSET_DIRECTORY / "TUK_GROUND.png"))
    character = load_image(str(ASSET_DIRECTORY / "animation_sheet.png"))
    return background, character