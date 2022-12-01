import sys, pygame
from wall import wall

pygame.init()

fps = 120

size = width, height = 1280, 720
backgroundColor = 138, 255, 206
screen = pygame.display.set_mode(size)

background = pygame.image.load("Assets/PyGameBackground.png")
screen.blit(background,(0,0))

player = pygame.image.load("Assets/python logo square ratio 150p.png")
playerRect = player.get_rect()
playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)
playerAngle = 0

wall1 = wall()
wall1Rect = wall1.image.get_rect()              #print(wall1.rects[0].topleft)

velocity = vx, vy = 0, 0
acceleration = 0.3
canJump = True

isJumping = False
jumpTimer = pygame.USEREVENT + 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #getting inputs (mouse, space bar and up key) and starting to jump
        elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP])): 
            if not isJumping:
                pygame.time.set_timer(jumpTimer, 200)
                isJumping = True
                
        elif event.type == jumpTimer: 
            isJumping = False
            if playerAngle < -270:
                playerAngle = 0
            elif playerAngle > -270 and playerAngle != 0:
                playerAngle = -180
            
    
    if isJumping is True:
        vy = -5
        playerAngle -= 8.57
        
    
    if playerRect.colliderect(wall1.rects[0]) or playerRect.colliderect(wall1.rects[1]):
        pygame.quit()
        sys.exit()


    #Physics calculations
    vy += acceleration
    velocity = vx, vy
    playerRect = playerRect.move(velocity)
    wall1.position -= pygame.Vector2(10,0)
    wall1.rects[0].left -= 10
    wall1.rects[1].left -= 10
    wall1Rect.topleft = wall1.position
    
   
    #Screen update
    screen.fill(backgroundColor)
    screen.blit(background,(0,0))
    screen.blit(pygame.transform.rotate(player, playerAngle), playerRect)
    screen.blit(wall1.image, wall1Rect)
    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
    

    