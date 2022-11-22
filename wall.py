import pygame, sys, random

pygame.init()

class wall:
    position = pygame.Vector2(0,0)
    position.xy
    spriteNum = 0
    image = pygame.surface.Surface((1,1))
    rects = [pygame.Rect(0,0,1,1),pygame.Rect(0,0,1,1)]


    def __init__(self, pos = (1280,0)):
        self.position = pos
        self.spriteNum = random.randint(1,3)
        if self.spriteNum == 1:
            self.image = pygame.image.load("Assets/semicolon_mistake.png")
            self.rects = [pygame.Rect(pos[0] + 82, pos[1] + 2, 135, 144), pygame.Rect(pos[0] + 100, pos[1] + 404, 111, 270)]
        elif self.spriteNum == 2:
            self.image = pygame.image.load("Assets/semicolon_mistake.png")
            self.rects = [pygame.Rect(pos[0] + 82, pos[1] + 2, 135, 144), pygame.Rect(pos[0] + 100, pos[1] + 404, 111, 270)]
        elif self.spriteNum == 3:
            self.image = pygame.image.load("Assets/semicolon_mistake.png")
            self.rects = [pygame.Rect(pos[0] + 82, pos[1] + 2, 135, 144), pygame.Rect(pos[0] + 100, pos[1] + 404, 111, 270)]