# python main src/main.py
# IMPORTS
from curses.ascii import NUL
import os
import sys
import pygame
from Particle import Particle
import Utils

#
pygame.init()

# CONSTANTS
size = WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()  # create a clock object
TICK = 60

# COLORS
BLACK1 = 4, 4, 4
BLACK2 = 9, 10, 10
BLACK3 = 15, 14, 14
BLACK4 = 16, 15, 23
BLACK5 = 28, 29, 30

COLOR_LINE = 59,61,63

WHITE1 = 255, 255, 255
WHITE2 = 255, 242, 241
WHITE3 = 238, 229, 233

# Instance screen
screen = pygame.display.set_mode(size)

##
# ...
# particles arr
particlesLisr = []

# FLAGS
pressed = False

# TRAP POSITION
trap_x = 0
trap_ax = 0
trap_dx = 0
trap_y = 0
trap_ay = 0
trap_dy = 0

# selected force
actual_force = 0
# ...
##


fontd = pygame.font.get_default_font()
font1 = pygame.font.SysFont(fontd, 20);
font2 = pygame.font.Font(os.path.join(
    "../resources/fonts/a_goblin_appears/a_goblini_appers.otf"), 10)
# font3 = pygame.font.Font(os.path.join("../resources/fonts/BIT typeface/BIT.otf"), 10)
font4 = pygame.font.Font(os.path.join(
    "../resources/fonts/pixeled/pixeled.ttf"), 10)
font5 = pygame.font.Font(os.path.join(
    "../resources/fonts/symtext/Symtext.ttf"), 14)


# game loop
while 1:
    # get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEWHEEL:
            print(event)
            print(event.x, event.y)
            print(event.flipped)
            print(event.which)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            trap_ax = trap_x = event.pos[0]
            trap_ay = trap_y = event.pos[1]
            pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            trap_dx = event.pos[0]
            trap_dy = event.pos[1]
            pressed = False
            # print(event)
        elif event.type == pygame.MOUSEMOTION:
            if pressed:
                trap_ax = event.pos[0]
                trap_ay = event.pos[1]

            # print(event)
            # particlesLisr.append(Particle(event.pos[0], event.pos[1]))
            
    # get the force
    if pressed:
        actual_force = Utils.getForceFromDistance(trap_x, trap_y, trap_ax, trap_ay)
        
    # ...

    # draw
    screen.fill(BLACK5)  # clear screen
    
    for p in particlesLisr:
        p.draw(screen)
    if pressed:
        # draw trap
        pygame.draw.line(screen, COLOR_LINE, (trap_x, trap_y),
                         (trap_ax, trap_ay), 1)
        textsurface = font2.render("Force: "+str(actual_force)+" " , False, WHITE1)
        screen.blit(textsurface, (10, HEIGHT - 30))
        
        # draw force
        

    # ...
    # display  flip
    pygame.display.flip()
    # wait
    clock.tick(TICK)
