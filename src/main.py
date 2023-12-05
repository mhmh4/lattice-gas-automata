import random

import pyray

WIDTH = 600
HEIGHT = 600

PARTICLE_SIZE = 5

NUM_PARTICLES = 12000

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

    next_grid = [[[] for _ in range(N)] for _ in range(M)]

    for i in range(M):
        for j in range(N):
            temp = []

            for _ in range(min(grid[i][j].count(1), grid[i][j].count(3))):
                temp.extend([2, 4])
                grid[i][j].remove(1)
                grid[i][j].remove(3)

            for _ in range(min(grid[i][j].count(2), grid[i][j].count(4))):
                temp.extend([1, 3])
                grid[i][j].remove(2)
                grid[i][j].remove(4)

            grid[i][j].extend(temp)

            for value in grid[i][j]:
                if value == 1:
                    if i == 0:
                        next_grid[i + 1][j].append(3)
                    else:
                        next_grid[i - 1][j].append(1)

                elif value == 2:
                    if j == (N - 1):
                        next_grid[i][j - 1].append(4)
                    else:
                        next_grid[i][j + 1].append(2)

                elif value == 3:
                    if i == (M - 1):
                        next_grid[i - 1][j].append(1)
                    else:
                        next_grid[i + 1][j].append(3)

                elif value == 4:
                    if j == 0:
                        next_grid[i][j + 1].append(2)
                    else:
                        next_grid[i][j - 1].append(4)

    grid = next_grid

pyray.close_window()
