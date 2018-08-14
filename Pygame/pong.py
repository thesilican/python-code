import pygame


pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption("A really stupid pong game")
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 30)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((15,15))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = DISPLAY_WIDTH / 2
        self.rect.centery = DISPLAY_HEIGHT / 2
        self.x_vel = 5
        self.y_vel = 5
        self.touching_paddle = False

    def update(self):
        self.rect.x += self.x_vel

        if self.rect.x < 0 or self.rect.x > DISPLAY_WIDTH - self.rect.width:
            self.rect.x = min(max(0, self.rect.x), DISPLAY_WIDTH - self.rect.width)
            self.x_vel = -self.x_vel

        self.rect.y += self.y_vel

        if self.rect.y < 0:
            self.rect.y = min(max(0, self.rect.y), DISPLAY_HEIGHT - self.rect.width)
            self.y_vel = -self.y_vel
        
        if self.rect.y > DISPLAY_HEIGHT - self.rect.width:
            global Game_Over
            Game_Over = True
        
        if pygame.sprite.collide_rect(self, paddle):
            if not self.touching_paddle:
                self.y_vel = -self.y_vel
                self.touching_paddle = True
                global Score
                Score += 1
        else: self.touching_paddle = False
        

class Paddle(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((100,15))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = DISPLAY_WIDTH / 2
        self.rect.y = DISPLAY_HEIGHT - 50

        self.x_vel = 0
    
    def change_speed(self, speed):
        self.x_vel += speed
    
    def update(self):
        self.x_vel *= 0.8
        if abs(self.x_vel) < 0.5: self.x_vel = 0
        self.rect.x += self.x_vel

        if self.rect.x < 0 or self.rect.x > DISPLAY_WIDTH - self.rect.width:
            self.rect.x = min(max(0, self.rect.x), DISPLAY_WIDTH - self.rect.width)

def draw_text(text, x, y):
    DISPLAY.blit(FONT.render(text, False, (0, 0, 0)), (x,y))

def draw():
    DISPLAY.fill(WHITE)
    sprites.draw(DISPLAY)
    if Score > 0: draw_text(str(Score), 10, 10)

sprites = pygame.sprite.Group()
ball = Ball(0,0)
paddle = Paddle()
sprites.add(paddle)
sprites.add(ball)

def game_loop():
    global Game_Over, Score
    Game_Over = False
    Score = 0
    right = left = False
    while not Game_Over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    right = True
                elif event.key == pygame.K_RIGHT:
                    left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    right = False
                elif event.key == pygame.K_RIGHT:
                    left = False
        
        if left:
            paddle.change_speed(5)
        if right:
            paddle.change_speed(-5)
        
        sprites.update()
        
        draw()
        pygame.display.update()
        clock.tick(60)
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
        clock.tick(60)

game_loop()
pygame.quit()
quit()