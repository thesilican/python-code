import pygame
import time
from random import randint

# Just don't import this module please
__all__ = []

pygame.init()

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 800

WHITE = (255,255,255)
GREY = (191,191,191)
BLACK = (0,0,0)
GREEN = (0,255,0)

normal_img = pygame.image.load("normal.gif")
font = pygame.font.SysFont("DejaVu Sans", 18)

pygame.display.set_caption('Virtual Pet')
game_display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
clock = pygame.time.Clock()

Happiness = 0
Hunger = 1
Health = 2
Weight = 3
LifePoints = 4

def start_game(pet_name):
    global var
    var = {
        Happiness:80,
        Hunger:0,
        Health:80,
        Weight:80,
        LifePoints:100}
    
    global Name
    Name = pet_name

    global total_ticks 
    total_ticks = 0

def set_var(var_type, value):
    var[var_type] = max(min(value,100),0)

def change_var(var_type, value):
    set_var(var_type, var[var_type] + value)

def get_time():
    return str.format("{:2}:{}",total_ticks // 2, "00" if total_ticks % 2 == 0 else "30")

def tick():
    global total_ticks
    total_ticks += 1
    if randint(1, 10) == 1:
        p = randint(0,1)
        if p == 0: change_var(Happiness, randint(1,2) * -5)
        else: change_var(Health, randint(1,2) * -5)
    
    if randint(1, 4) == 1:
        change_var(Hunger, 5)

def feed(food_type):
    """food_type is from 1-4, where 4 = unhealthy"""
    if food_type < 1 or food_type > 4:
        raise Exception("Invalid Range: food_type")
    change_var(Hunger, randint(8,10)*-5)
    change_var(Weight, randint(0, food_type - 1)*5)
    change_var(Health, randint(0,(food_type - 2))*-5)
    change_var(Happiness, randint(0, max(food_type - 3, 0)*5))

def play():
    change_var(Happiness, randint(4, 8)*5)
    change_var(Hunger, randint(2, 4) *5)
    if var[Weight] > 30:
        change_var(Weight, randint(0,1) * -5)
    change_var(Health, randint(0,3)*5)

def doctor():
    change_var(Health, randint(8,16)*5)
    change_var(Happiness, randint(7,10)*-5)
    if var[Weight] > 50:
        change_var(Weight, ((Weight - 50)//5+randint(-1,1))*5)
        change_var(Happiness, ((Weight - 50)//10+randint(-1,2)) * 5)

def draw_text(text, x, y):
    game_display.blit(font.render(text, True, BLACK), (x, y))

def draw_ui():
    game_display.fill(WHITE)
    


def game_loop():
    TICKEVENT = pygame.USEREVENT + 1
    # Every second for now
    pygame.time.set_timer(TICKEVENT, 1000)
    keys = {
        pygame.K_f:False,
        pygame.K_d: False,
        pygame.K_p: False }

    while True:
        do_tick = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                keys[event.key] = True
            
            if event.type == TICKEVENT:
                do_tick = True
        
        if keys[pygame.K_f] == True:
            keys[pygame.K_f] = False
            feed(4)
        
        if keys[pygame.K_d] == True:
            keys[pygame.K_d] == False
            doctor()
        
        if keys[pygame.K_p] == True:
            keys[pygame.K_p] = False
            play()

        if do_tick:
            tick()
        draw_ui()
        pygame.display.update()
        clock.tick(60)

start_game("Kirby")
game_loop()
pygame.quit()
quit()