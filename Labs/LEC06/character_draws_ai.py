import math
from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
START_X = 600
START_Y = 300


def circle_path(character_width, character_height):
	center_x = CANVAS_WIDTH / 2
	center_y = CANVAS_HEIGHT / 2
	radius = min(
		center_x - character_width / 2,
		center_y - character_height / 2,
	)
	for degree in range(361):
		angle = math.radians(degree)
		x = center_x + radius * math.cos(angle)
		y = center_y + radius * math.sin(angle)
		yield x, y


def polygon_path(vertices, steps_per_edge=90):
	for index, start in enumerate(vertices):
		end = vertices[(index + 1) % len(vertices)]
		for step in range(steps_per_edge + 1):
			ratio = step / steps_per_edge
			x = start[0] + (end[0] - start[0]) * ratio
			y = start[1] + (end[1] - start[1]) * ratio
			yield x, y


def rectangle_path(character_width, character_height):
	left = character_width / 2
	right = CANVAS_WIDTH - character_width / 2
	bottom = character_height / 2
	top = CANVAS_HEIGHT - character_height / 2
	vertices = [
		(right, CANVAS_HEIGHT / 2),
		(right, top),
		(left, top),
		(left, bottom),
		(right, bottom),
	]
	yield from polygon_path(vertices)


def triangle_path(character_width, character_height):
	center_x = CANVAS_WIDTH / 2
	center_y = CANVAS_HEIGHT / 2
	radius = min(
		center_x - character_width / 2,
		center_y - character_height / 2,
	)
	half_height = radius * math.sqrt(3) / 2
	vertices = [
		(center_x - radius / 2, center_y + half_height),
		(center_x - radius / 2, center_y - half_height),
		(center_x + radius, center_y),
	]
	yield from polygon_path(vertices)


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	character = load_image(str(Path(__file__).resolve().with_name("character.png")))
	paths = (
		lambda: circle_path(character.w, character.h),
		lambda: rectangle_path(character.w, character.h),
		lambda: triangle_path(character.w, character.h),
	)
	running = True

	while running:
		for make_path in paths:
			for x, y in make_path():
				for event in get_events():
					if event.type == SDL_QUIT or (
						event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
					):
						running = False
						break

				if not running:
					break

				clear_canvas()
				character.draw(x, y)
				update_canvas()
				delay(0.01)

			if not running:
				break

	close_canvas()


if __name__ == "__main__":
	main()
