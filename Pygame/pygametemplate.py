import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption("[TITLE]")
clock = pygame.time.Clock()

def draw():
    DISPLAY.fill(WHITE) 

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pass

            if event.type == pygame.KEYUP:
                pass
        
        draw()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()