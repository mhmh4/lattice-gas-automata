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
    pyray.clear_background(pyray.WHITE)
    pyray.draw_text("Hello world", 190, 200, 20, pyray.VIOLET)
    pyray.end_drawing()

pyray.close_window()
