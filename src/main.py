import random

import pyray

WIDTH = 1000
HEIGHT = 500

PARTICLE_SIZE = 25

NUM_PARTICLES = 400

M = WIDTH // PARTICLE_SIZE
N = HEIGHT // PARTICLE_SIZE

grid = [[[] for _ in range(N)] for _ in range(M)]

for _ in range(NUM_PARTICLES):
    random_i = random.randint(0, M - 1)
    random_j = random.randint(0, N - 1)
    grid[random_i][random_j].append(random.randint(1, 4))

pyray.init_window(WIDTH, HEIGHT, "")

while not pyray.window_should_close():
    pyray.begin_drawing()

    pyray.clear_background(pyray.BLACK)

    x = 0
    y = 0

    for j in range(N):
        x = 0
        for i in range(M):
            pyray.draw_rectangle(
                x,
                y,
                PARTICLE_SIZE,
                PARTICLE_SIZE,
                pyray.Color(0, 115, 207, len(grid[i][j]) * 15 + 100),
            )
            x += PARTICLE_SIZE
        y += PARTICLE_SIZE

    pyray.end_drawing()

pyray.close_window()
