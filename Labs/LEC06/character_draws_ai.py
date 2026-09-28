import math
from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
START_X = 600
START_Y = 300


def circle_path():
	radius = 200
	for degree in range(361):
		angle = math.radians(degree)
		x = START_X + radius * math.cos(angle)
		y = START_Y + radius * math.sin(angle)
		yield x, y


def polygon_path(vertices, steps_per_edge=90):
	for index, start in enumerate(vertices):
		end = vertices[(index + 1) % len(vertices)]
		for step in range(steps_per_edge):
			ratio = step / steps_per_edge
			x = start[0] + (end[0] - start[0]) * ratio
			y = start[1] + (end[1] - start[1]) * ratio
			yield x, y
	yield vertices[0]


def rectangle_path():
	vertices = [
		(START_X, START_Y),
		(START_X, 500),
		(100, 500),
		(100, 100),
		(START_X, 100),
	]
	yield from polygon_path(vertices)


def triangle_path():
	vertices = [
		(START_X, START_Y),
		(350, 500),
		(100, 300),
	]
	yield from polygon_path(vertices)


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	character = load_image(str(Path(__file__).resolve().with_name("character.png")))
	paths = (circle_path, rectangle_path, triangle_path)
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
