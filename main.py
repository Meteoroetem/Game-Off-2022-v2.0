import sys, pygame

#def jump(rect, surf):


pygame.init()

fps = 120

size = width, height = 1280, 720
BLACK = 0, 0, 0

screen = pygame.display.set_mode(size)

player = pygame.image.load("python logo square ratio 150p.png")  #pygame.surface.Surface(size)
playerRect = player.get_rect()
playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)

isJumping = False
jumpTimer = pygame.USEREVENT + 1
#playerSprite = pygame.draw.circle(player, (255,255,255), playerRect.center, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
        elif event.type == jumpTimer: isJumping = False  

    if not isJumping:
        if(pygame.mouse.get_pressed(3)[0]):
            pygame.time.set_timer(jumpTimer, 250)
            isJumping = True
            #player = pygame.transform.rotozoom(player, 90, 1)
    if isJumping is True:
        playerRect = playerRect.move(0,-20)
    
    playerRect = playerRect.move(0,10)

    screen.fill(BLACK)
    screen.blit(player, playerRect)
    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
    

    