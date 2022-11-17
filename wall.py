import pygame, sys, random

pygame.init()

class wall:
    height = 0;
    sprite = 0
    def __init__(self, h):
        self.height = h
        self.sprite = random.randint(0,5)
