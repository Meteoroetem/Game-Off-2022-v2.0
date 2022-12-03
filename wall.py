import pygame, sys, random

pygame.init()

class wall:
    position = pygame.Vector2(0,0)
    position.xy
    spriteNum = 0
    image = pygame.surface.Surface((1,1))
    rects = [pygame.Rect(0,0,1,1),pygame.Rect(0,0,1,1)]
    parentRect = image.get_rect()

    def Move(self, xvalue):
        self.position += pygame.Vector2(xvalue,0)
        for rect in self.rects:
            rect.left += xvalue
        self.parentRect.left += xvalue


    def __init__(self, pos = (1280,0)):
        self.position = pos
        self.spriteNum = random.randint(1,3)
        if self.spriteNum == 1:
            self.image = pygame.image.load("Assets/Sprites/semicolon_mistake.png")
            self.rects = [pygame.Rect(pos[0] + 82, pos[1] + 2, 135, 144), pygame.Rect(pos[0] + 100, pos[1] + 404, 111, 270)]
        elif self.spriteNum == 2:
            self.image = pygame.image.load("Assets/Sprites/bracketsMistake.png")
            self.rects = [pygame.Rect(pos[0], pos[1] + 10, 61, 250), pygame.Rect(pos[0] + 191, pos[1] + 459, 55, 251)]
        elif self.spriteNum == 3:
            self.image = pygame.image.load("Assets/Sprites/newIntMistake.png")
            self.rects = [pygame.Rect(pos[0] + 241, pos[1] + 20, 101, 109), pygame.Rect(pos[0] + 19, pos[1] + 294, 115, 111), pygame.Rect(pos[0] + 230, pos[1] + 593, 124, 111)]
        self.parentRect = self.image.get_rect()
        self.parentRect.topleft = pos      