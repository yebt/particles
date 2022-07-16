import pygame
import colorsys
import random


class Particle:
    pos_x = 0
    pos_y = 0
    vel_x = 0
    vel_y = 0
    mass = 0
    color = 0, 0, 0
    radius = 1

    def __init__(self, pos_x, pos_y, mass=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mass = mass
        self.radius = 10;
        
        # calculate colors
        h = (random.randint(0, 360))
        s = (random.randint(50, 80))
        v = (random.randint(50, 100))
        
        # Calculate the color and convert to rgb
        (r, g, b) = colorsys.hsv_to_rgb(
            h/360,
            s/100,
            v/100,
        )
        
        # set the colors
        self.color = (
            round(r*255), round(g*255), round(b*255)
        )
        
    # draw function
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            self.color,
            (self.pos_x, self.pos_y),
            self.radius,
        )