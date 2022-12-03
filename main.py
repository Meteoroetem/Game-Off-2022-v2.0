import sys, pygame
from wall import wall

pygame.init()

fps = 60

size = width, height = 1280, 720
backgroundColor = 138, 255, 206
screen = pygame.display.set_mode(size)

mainFont = pygame.font.Font("Assets/Fonts/FastinaOotsineDEMO.otf", 120)
score = 0

background = pygame.image.load("Assets/Sprites/newPyGameBackground.png")
screen.blit(background,(0,0))

player = pygame.image.load("Assets/Sprites/python logo square ratio 150p.png")
playerRect = player.get_rect()
playerRect.center = (screen.get_rect().centerx - 150, screen.get_rect().centery)
playerAngle = 0
playerColidingRect = pygame.Rect(playerRect.topleft, [playerRect.width-20, playerRect.height-20])
newIsPassing = False
oldIsPassing = False
velocity = vx, vy = 17, 0
acceleration = 0.8
canJump = True
jumpForce = 10
jumpTime = 150

walls = [wall(), wall((2560,0)) ,wall((3840,0))]            #print(wall1.rects[0].topleft)

isJumping = False
jumpTimer = pygame.USEREVENT + 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #getting inputs (mouse, space bar and up key) and starting to jump
        elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP])): 
            if not isJumping:
                pygame.time.set_timer(jumpTimer, jumpTime)
                isJumping = True
                
        elif event.type == jumpTimer: 
            isJumping = False
            if playerAngle < -270:
                playerAngle = 0
            elif playerAngle > -270 and playerAngle != 0:
                playerAngle = -180
            
    
    if isJumping == True:
        vy = -jumpForce
        #calculate the required amount of rotation to rotate 180 degrees
        playerAngle -= 180/(fps*(jumpTime/1000))
    print(playerAngle)
        
    #for theWall in walls:
        #for rect in theWall.rects:
            #colidingRect = pygame.Rect(playerRect.topleft, [playerRect.width-20, playerRect.height-20])
            #colidingRect.center = playerRect.center
            #if colidingRect.colliderect(rect):
                #score = 0

    #for theWall in walls:
        #if playerRect.centerx == theWall.position[0]+50:
            #score += 10

    #If player exits screen
    if playerRect.top > screen.get_height():
        playerRect.top = screen.get_height()
        vy = -20
        if score != 0: score -= 5
    if playerRect.top < 0:
        playerRect.top = 0
        if score != 0: score -= 5

    #Physics calculations
    vy += acceleration
    velocity = vx, vy
    playerRect = playerRect.move((0, vy))
    playerColidingRect.center = playerRect.center

    #Screen update
    screen.fill(backgroundColor)
    screen.blit(background,(0,0))
    screen.blit(pygame.transform.rotate(player, playerAngle), playerRect)
    
    for theWall in walls:
        #When theWall exits screen instanciate a new one in the front
        if theWall.position[0] < -theWall.image.get_rect().width:
            walls.remove(theWall)
            walls.append(wall((3840,0)))

        theWall.Move(-vx)
        #print(walls[0].parentRect,walls[0].position,playerRect)

        for rect in theWall.rects:
            if playerColidingRect.colliderect(rect):
                score = 0

        newIsPassing = playerRect.colliderect(walls[0].parentRect) or playerRect.colliderect(walls[1].parentRect) or playerRect.colliderect(walls[2].parentRect)
        #print(newIsPassing, oldIsPassing)
        if newIsPassing and not oldIsPassing:
            score += 10
        
        oldIsPassing = newIsPassing
            
        if theWall.position[0] < 1280 or theWall.position[0] > 0:
            screen.blit(theWall.image, theWall.position)

    strScore = str("Score: " + str(score))
    screen.blit(mainFont.render(strScore, False, (255,255,100)), (0,0))

    pygame.display.flip()
    pygame.time.wait(int(1000/fps))
    

    