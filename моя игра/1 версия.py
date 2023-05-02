import pygame, sys
pygame.init()
from os import path
# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

SPEED = 30
changeX = 0
changeY = 0
changeX1 = 0
changeY1 = 0

move = False
move1 = False
collision = False


#платформы 

thorn = pygame.image.load('шипы.png') 
border = pygame.image.load('block0.png') 
platform = pygame.image.load('block0.png') 
prostr = pygame.image.load('food.png')
havat = pygame.image.load('havka.png')
bullet = pygame.image.load('ПУЛЯЯЯ.png')

gun = pygame. Surface((20,20))
gun.fill(BLACK)

bulletrect = bullet.get_rect()


#персонаж

herostand = pygame.image.load('pers3.png')
heror = pygame.image.load('pers.png')
heromover = pygame.image.load('pers2.png')

hero = herostand
herorect = hero.get_rect()
herorect.bottom = HEIGHT-150
herorect.left = WIDTH-1600
level = 1
maps =  [ 
    [
        '***************************************',
        '*//*---------------------*     *----  ^',
        '****- --      *  -      -*      -  -***',
        '*-------*-  * ***-      -*****  -  -*/*',
        '*-**    *-------*-------------------*/*',
        '*----*--*-------*---------------*  -*/*',
        '******-*     ******------*     **  -*/*',    
        '*------*--------   -    **     *   -*/*',
        '*- -*-*********---------------------*/*',
        '*- -*---------*--********************/*',
        '*---*- -*****-*--*------------------*/*',
        '*****- -*---*-*--*-****************-*/*',
        '*----- -*-***-*--*-*--------------*-*/*',
        '*-****--*-----*--*-*-************-*-*/*',
        '*---*--********--*-*------------*-*-*/*',
        '*- -*---------*--*-**************-*-*/*',
        '*- -*- -*****-*--*----------------*-*/*',
        '*- -*- -*///*- --******************-*/*',
        '*---*- -*///*-*****-----*/*-----*/*-*/*',
        '*****- -*///*-------***-***-***-***-*/*',
        '*-------*///*********/*-----*/*-----*/*',
        '***************************************',
    ],
    [
        '***************************************',
        '* *-_*----   *                        *',
        '*-* *****    *                        *',
        '*-*-*     *  *                        *',
        '*-  *      --*                        *',
        '*-  * ****   *                        *',
        '*-  *     *  *                        *',
        '**        *  *                        *',
        '*_   ---- *  *                        *',
        '********* *  *                        *',
        '* -----   *  *                        *',
        '*           -*                        *',
        '*-     ****  *                        *',
        '*-           *                        *',
        '*-    *      *         ******         *',
        '***** *      *                        *',
        '*-----   -*  *                   **** *',
        '* ****   -  ---                       *',
        '*        - *_*                        ^',
        '***************************************',
    ],
    [
        '***************************************',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                                     *',
        '*                     *******         *',
        '*                                     =',
        '*                                     *',
        '*      ******                         *',
        '*                                     *',
        '*                      ******         *',
        '*****                                 *',
        '*                                **** *',
        '*                                     *',
        '*                                     *',
        '***************************************',
    ]
]



while 1:
    # проверяем события, которые произошли (если они были)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT and move == False :
        #         changeX = -1 * SPEED
        #         move = True 
        #     if event.key == pygame.K_RIGHT and move == False:
        #         changeX = SPEED
        #         move = True
        #         hero = heromover
            
        #     if event.key == pygame.K_UP and move == False:
        #         changeY = -1 * SPEED
        #         move = True
        #         # if collision == True:
        #         #     move == False
        #     if event.key == pygame.K_DOWN and move == False:
        #         changeY = SPEED
        #         move = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        # elif event.type == pygame.KEYUP:
        #     if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,pygame.K_UP ]:
        #         move == False
                
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX1 = -1 * SPEED

    if keys[pygame.K_RIGHT]:
        changeX1 = SPEED

    if keys[pygame.K_UP]:
        changeY1 = -1 * SPEED

    if keys[pygame.K_DOWN]:
        changeY1 = SPEED

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        changeY1 = 0

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        changeX1 = 0

    herorect_old = herorect.copy()

    platforms = []
    prostranstvo = []
    havattt = []
    borders = []
    thorns = []
    guns = []
    bullets =[]

    herorect.x += changeX
    herorect.y += changeY



    #генерация платформ

    currentmap = maps[level]

    for i in range(len(currentmap)):
        for j in range(len(currentmap[i])):
            if currentmap[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 50 * j
                platformrect.y = 50 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)
            if currentmap[i][j] == '/':
               prostrRect = prostr.get_rect()
               prostrRect.x = 50 * j
               prostrRect.y = 50 * i
               prostranstvo.append(prostrRect)
               mainScreen.blit(prostr, prostrRect)
            if currentmap[i][j] == '-':
               havatRect = havat.get_rect()
               havatRect.x = 50 * j
               havatRect.y = 50 * i
               havattt.append(havatRect)
               mainScreen.blit(havat, havatRect)
            if currentmap[i][j] == '^':
                borderRect = border.get_rect()
                borderRect.x = 50 * j
                borderRect.y = 50 * i
                borders.append(borderRect)
                mainScreen.blit(border, borderRect)
            if currentmap[i][j] == '_':
                thornRect = thorn.get_rect()
                thornRect.x = 50 * j
                thornRect.y = 50 * i
                thorns.append(thornRect)
                mainScreen.blit(thorn, thornRect)
            if currentmap[i][j] == '=':
                gunRect = gun.get_rect()
                gunRect.x = 50 * j
                gunRect.y = 50 * i
                guns.append(gunRect)
                mainScreen.blit(gun, gunRect)
    
    #  генерация пуль


    # if len(bullets)==0 and time>=180  :
    
    if len(bullets)==0:
        while True:
            bulletrect = bullet.get_rect()
            bulletrect.x = gunRect
            bulletrect.y = gunRect
            bullets.append(bulletrect)  
    
    bulletrect.x += changeX1
    bulletrect.y += changeY1

    # попадание

    if len(bullets) > 0:
        for i in range(len(bullets)):
            if herorect.colliderect(bullets[i]) == True:  
                time = 0
                herorect.bottom = HEIGHT - 1000
                herorect.left = WIDTH-1900
                break

    # движение пуль 

    # if len(bullets) != 0:
    #         bulletrectMove = bullet.get_rect()
    #         bulletrectMove.x -= 10 
    # if len(bullets) != 0:
    #         bulletrectMove= bullet.get_rect()
    #         bulletrectMove.x += 10 


    score = len(havattt)

    #провера столкновения 
    
    for platformrect in platforms:
        if herorect.colliderect(platformrect) == True:

             # движемся налево
            if herorect.left < herorect_old.left:
                herorect.x -= changeX

            # движемся направо
            if herorect.right > herorect_old.right:
                herorect.x -= changeX 

            move = False
            changeX = 0

        if herorect.colliderect(platformrect) == True :
            # движемся вниз
            if herorect.bottom > herorect_old.bottom:
                herorect.bottom -= changeY
                
            if herorect.top < herorect_old.top:
                herorect.top -= changeY

            move = False
            changeY = 0

    for havatRect in havattt:
        if herorect.colliderect(havatRect) == True:
            mapx = havatRect.x // 50
            mapy = havatRect.y // 50
            havatstr = currentmap[mapy]
            havatstr = havatstr[:mapx] + ' ' + havatstr[mapx + 1:]
            currentmap[mapy] = havatstr
            score -=1

    if herorect.colliderect(borderRect) == True and score!=0:
        herorect.bottom = HEIGHT-150
        herorect.left = WIDTH-1600


    if score == 0 and herorect.colliderect(borderRect) == True:
        level +=1
        herorect.bottom = HEIGHT - 1000
        herorect.left = WIDTH-1900

    for thornRect in thorns:    
        if herorect.colliderect(thornRect) == True and level == 1:
            herorect.bottom = HEIGHT - 1000
            herorect.left = WIDTH-1900

    if len(bullets) > 0:
        for i in range(len(bullets)):
            if herorect.colliderect(bullets[i]) == True:  
                time = 0
                herorect.bottom = HEIGHT - 1000
                herorect.left = WIDTH-1900
                break


    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)
    for prostrRect in prostranstvo:
        mainScreen.blit(prostr, prostrRect)
    for havatRect in havattt:
        mainScreen.blit(havat, havatRect )
    for borderRect in borders:
        mainScreen.blit(border,borderRect)
    for thornRect in thorns:
        mainScreen.blit(thorn,thornRect)

    mainScreen.blit(hero,herorect)

    

    # print(herorect.colliderect(borderRect))
    pygame.display.flip()
    clock.tick(FPS)
