import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A random game")
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
DEBUGFONT = pygame.font.SysFont("Courier New", 18)
ball_sprite = pygame.image.load("ballmed.png")
ball_radius = ball_sprite.get_width()/2
paddle_sprite = pygame.image.load("paddle.png")
paddle_width, paddle_height = paddle_sprite.get_width(), paddle_sprite.get_height()

DEBUG = False

def draw_paddle(x, y):
    """Draw the paddles"""

    gameDisplay.blit(paddle_sprite, (x,y))
    w = paddle_sprite.get_width()
    if x + w > WIDTH:
        gameDisplay.blit(paddle_sprite, (x-WIDTH,y))
    if DEBUG:
        pygame.draw.circle(gameDisplay, BLACK, (int(x), int(y)), 2)

def draw_ball(x, y):
    gameDisplay.blit(ball_sprite, (x - ball_radius, y - ball_radius))
    if DEBUG:
        pygame.draw.rect(gameDisplay, BLACK, (x - ball_radius, y - ball_radius, ball_radius * 2, ball_radius * 2), 1)
        pygame.draw.circle(gameDisplay, BLACK, (int(x), int(y)), 2)

def draw_text(textArray):
    for x in range(len(textArray)):
        textsurface = DEBUGFONT.render(textArray[x], False, (0,0,0))
        gameDisplay.blit(textsurface, (0, x * DEBUGFONT.get_height()))

def game_loop():
    """The main game loop"""

    # Init a few things
    # This is just the top left
    p_x = 0
    p_y = HEIGHT - 100
    p_x_speed = 0
    # BTW these are the centers of the ball
    b_x = WIDTH/2
    b_y = HEIGHT/2
    b_x_speed = 10
    b_y_speed = 10

    k_l_down = False
    k_r_down = False

    finished = False
    while not finished:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    k_l_down = True
                elif event.key == pygame.K_RIGHT:
                    k_r_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    k_l_down = False
                elif event.key == pygame.K_RIGHT:
                    k_r_down = False
        
        # Paddle movement code
        if k_l_down:
            p_x_speed += -1
        elif k_r_down:
            p_x_speed += 1
        else:
            p_x_speed = p_x_speed * 0.8 #deacceleration
        p_x += p_x_speed
        p_x = p_x % WIDTH

        # ---------- Ball movement ----------
        # move 1 pixel at a time
        temp_x = abs(b_x_speed)
        temp_y = abs(b_y_speed)
        while temp_x >= 1 or temp_y >= 1:
            if temp_x > temp_y:
                b_x += b_x_speed / abs(b_x_speed)
                temp_x -= 1
            else:
                b_y += b_y_speed / abs(b_y_speed)
                temp_y -= 1
            # bouncing
            if b_x - ball_radius <= 0 and b_x_speed < 0:
                b_x_speed = -b_x_speed
            if b_x + ball_radius >= WIDTH and b_x_speed > 0: 
                b_x_speed = -b_x_speed
            if b_y - ball_radius <= 0 and b_y_speed < 0:
                b_y_speed = -b_y_speed
            if b_y + ball_radius >= HEIGHT and b_y_speed > 0: 
                b_y_speed = -b_y_speed
            # paddle bouncing
            # bounce only if going down and ball intersects the top of the paddle's y hitbox
            if b_y_speed >= 0 and (b_y + ball_radius >= p_y and b_y - ball_radius < p_y):
                # calculate the outer bounds of the paddle, 
                # going beyond WIDTH if the paddle wraps around (instead of negative)
                # THIS PART IS BUGGY
                paddle_min, paddle_max = p_x, p_x + paddle_width
                ball_min, ball_max = (b_x - ball_radius if b_x - ball_radius > 0 else b_x - ball_radius + WIDTH),\
                    b_x + ball_radius
                if ball_max > paddle_min and ball_min < paddle_max:
                    b_y_speed = - b_y_speed # bounce

        # Draw
        gameDisplay.fill(WHITE)
        draw_paddle(p_x, p_y)
        draw_ball(b_x, b_y)
        if DEBUG:
            draw_text(("b_x: {:.0f} b_y: {:.0f} b_x_speed: {} b_y_speed: {}".format(b_x, b_y, b_x_speed, b_y_speed),
                      "p_x: {:.0f} p_y: {:.0f} p_x_speed: {:.1f}"
                        .format(p_x, p_y, p_x_speed)))

        pygame.display.update()
        clock.tick(60)
game_loop()