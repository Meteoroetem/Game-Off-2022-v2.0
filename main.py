import sys, pygame
from wall import wall

pygame.init()

fps = 1000

size = width, height = 1280, 720
backgroundColor = 138, 255, 206
screen = pygame.display.set_mode(size)

mainFont = pygame.font.Font("Assets/FastinaOotsineDEMO/FastinaOotsineDEMO.otf", 120)
score = 0

background = pygame.image.load("Assets/newPyGameBackground.png")
screen.blit(background,(0,0))

player = pygame.image.load("Assets/python logo square ratio 150p.png")
playerRect = player.get_rect()
playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)
playerAngle = 0

wall1 = wall()
wall2 = wall(pos=(2560,0))
wall3 = wall(pos=(3840,0))

walls = [wall1, wall2 ,wall3]            #print(wall1.rects[0].topleft)

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
            
    
    if isJumping == True:
        vy = -5
        playerAngle -= 8.57
        
    for theWall in walls:
        for rect in theWall.rects:
            colidingRect = pygame.Rect(playerRect.topleft, [playerRect.width-20, playerRect.height-20])
            colidingRect.center = playerRect.center
            if colidingRect.colliderect(rect):
                print("Colliding!")
                score = 0

    for theWall in walls:
        if playerRect.centerx == theWall.position[0]+50:
            score += 10


    if playerRect.top > screen.get_height():
        #playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)
        playerRect.top = screen.get_height()
        vy = -15
        if score != 0: score -= 5
    if playerRect.top < 0:
        playerRect.top = 0
        if score != 0: score -= 5

    #Physics calculations
    vy += acceleration
    velocity = vx, vy
    playerRect = playerRect.move(velocity)

    for theWall in walls:
        if theWall.position[0] < -theWall.image.get_rect().width:
            walls.remove(theWall)
            walls.append(wall((3840,0)))
        theWall.position -= pygame.Vector2(10,0)
        for rect in theWall.rects:
            rect.left -= 10

        
            

    #Screen update
    screen.fill(backgroundColor)
    screen.blit(background,(0,0))
    screen.blit(pygame.transform.rotate(player, playerAngle), playerRect)
    
    for theWall in walls:
        if theWall.position[0] < 1280 or theWall.position[0] > 0:
            screen.blit(theWall.image, theWall.position)

    strScore = str("Score: " + str(score))
    screen.blit(mainFont.render(strScore, False, (255,255,100)), (0,0))

    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
    

    