import pygame, sys, random

pygame.init()

class wall:
    position = pygame.Vector2()
    position.xy
    spriteNum = 0
    image = pygame.image.load("Assets/semicolon_mistake.png")

    def __init__(self, pos = (1280,0)):
        self.position = pos
        self.spriteNum = random.randint(0,5)
