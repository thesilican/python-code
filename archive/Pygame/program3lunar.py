import pygame

pygame.init()

width = 800
height = 600
# Color definitions
BLACK = (0,0,0)
GREY = (127,127,127)
WHITE = (255,255,255)

DISPLAY = pygame.display.set_mode((width,height))
pygame.display.set_caption("Lunar Lander I think")
clock = pygame.time.Clock()

r_w = 50
r_h = 100
y = 500
y_accel = 0

def draw():
    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY, GREY, (width/2 - (r_w/2), height - y - r_h, r_w, r_h), 0)

def game_loop():
    global y, y_accel
    while True:
        space = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            space = True
        
        y_accel -= 1
        if space:
            y_accel += 2

        y += y_accel

        if y <= 0:
            y = 0
        draw()
        print(y, y_accel, space)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()