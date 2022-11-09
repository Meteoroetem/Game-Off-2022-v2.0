import sys, pygame

#def jump(rect, surf):


pygame.init()

fps = 120

size = width, height = 1280, 720
BLACK = 0, 0, 0

screen = pygame.display.set_mode(size)
msPressed = False

player = pygame.image.load("Assets/python logo square ratio 150p.png")  #pygame.surface.Surface(size)
playerRect = player.get_rect()
playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)
playerAngle = 0

velocity = vx, vy = 0, 0
acceleration = 0.3
canJump = True

isJumping = False
jumpTimer = pygame.USEREVENT + 1
#playerSprite = pygame.draw.circle(player, (255,255,255), playerRect.center, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP: msPressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            msPressed = True
            if not isJumping:
                pygame.time.set_timer(jumpTimer, 200)
                isJumping = True
                
        elif event.type == jumpTimer: 
            isJumping = False
            
    
    if isJumping is True:
        vy = -5
        playerAngle += -8.57
    
    #player = pygame.transform.rotate(player, playerAngle)
    vy += acceleration
    velocity = vx, vy
    playerRect = playerRect.move(velocity)
    
   

    screen.fill(BLACK)
    screen.blit(pygame.transform.rotate(player, playerAngle), playerRect)
    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
    

    