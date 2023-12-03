import pyray


WIDTH = 800
HEIGHT = 400

pyray.init_window(WIDTH, HEIGHT, "Hello")

PARTICLE_SIZE = 10

M = WIDTH // PARTICLE_SIZE
N = HEIGHT // PARTICLE_SIZE

grid = [[[] for _ in range(N)] for _ in range(M)]

print(grid)

while not pyray.window_should_close():
    pyray.begin_drawing()

    x = 0
    y = 0

    for j in range(N):
        x = 0
        for i in range(M):
            pyray.draw_rectangle(x, y, PARTICLE_SIZE, PARTICLE_SIZE, pyray.GRAY)
            x += PARTICLE_SIZE
        y += PARTICLE_SIZE

    pyray.end_drawing()

pyray.close_window()
