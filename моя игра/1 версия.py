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

move = False
move1 = False
collision = False
#платформы 

border = pygame.image.load('block0.png') 
platform = pygame.image.load('block0.png') 
prostr = pygame.image.load('food.png')
havat = pygame.image.load('havka.png')

#персонаж

herostand = pygame.image.load('pers3.png')
heror = pygame.image.load('pers.png')
heromover = pygame.image.load('pers2.png')

hero = herostand
herorect = hero.get_rect()
herorect.bottom = HEIGHT-150
herorect.left = WIDTH-1600

maps =  [
    '***************************************',
    '*//*---------------------*     *---- ^ ',
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
]



while 1:
    # проверяем события, которые произошли (если они были)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and move == False :
                changeX = -1 * SPEED
                move = True 
            if event.key == pygame.K_RIGHT and move == False:
                changeX = SPEED
                move = True
                hero = heromover
            
            if event.key == pygame.K_UP and move == False:
                changeY = -1 * SPEED
                move = True
                # if collision == True:
                #     move == False
            if event.key == pygame.K_DOWN and move == False:
                changeY = SPEED
                move = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,pygame.K_UP ]:
                move == False
                

    herorect_old = herorect.copy()

    platforms = []
    prostranstvo = []
    havattt = []
    borders = []

    herorect.x += changeX
    herorect.y += changeY

    #генерация платформ

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 50 * j
                platformrect.y = 50 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)
            if maps[i][j] == '/':
               prostrRect = prostr.get_rect()
               prostrRect.x = 50 * j
               prostrRect.y = 50 * i
               prostranstvo.append(prostrRect)
               mainScreen.blit(prostr, prostrRect)
            if maps[i][j] == '-':
               havatRect = havat.get_rect()
               havatRect.x = 50 * j
               havatRect.y = 50 * i
               havattt.append(havatRect)
               mainScreen.blit(havat, havatRect)
            if maps[i][j] == '^':
                borderRect = border.get_rect()
                borderRect.x = 50 * j
                borderRect.y = 50 * i
                borders.append(borderRect)
                mainScreen.blit(border, borderRect)

    score = len(havattt)

    #провера столкновения 
    for platformrect in platforms:
        if herorect.colliderect(platformrect) == True:
            # collision = True

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
            havatstr = maps[mapy]
            havatstr = havatstr[:mapx] + ' ' + havatstr[mapx + 1:]
            maps[mapy] = havatstr
            score -=1

    for borderRect in borders:
        if score == 0:
            mapx = borderRect.x // 50
            mapy = borderRect.y // 50
            borderstr = maps[mapy]
            borderstr = borderstr[:mapx] + ' ' + borderstr[mapx + 1:]
            maps[mapy] = borderstr


    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)
    for prostrRect in prostranstvo:
        mainScreen.blit(prostr, prostrRect)
    for havatRect in havattt:
        mainScreen.blit(havat, havatRect )

    mainScreen.blit(hero,herorect)

    

    # print(score)
    pygame.display.flip()
    clock.tick(FPS)
