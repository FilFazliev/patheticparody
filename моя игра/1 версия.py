import pygame, sys
pygame.init()
from os import path
# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

SPEED = 60
changeX = 0
changeY = 0

move = False
move1 = False
collision = False
#платформы 

platform = pygame.image.load('block0.png') 

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
    '*                        *     *       ',
    '*             *          *          ***',
    '****          ***        *****      * *',
    '*               *                   * *',
    '*               *              *    * *',
    '****** *     ******      *     *    * *',
    '*      *                **     *    * *',
    '*    * ********                     * *',
    '*    *        *  ******************** *',
    '*    * ****** *  *                  * *',
    '****** *    * *  * **************** * *',
    '*      * **** *  * *              * * *',
    '** *** *      *  * * ************ * * *',
    '**   * ********  * *            * * * *',
    '*    *        *  * ************** * * *',
    '*    * ****** *  *                * * *',
    '*    * *    * *  ****************** * *',
    '*    * *    * *****     * *     * * * *',
    '****** *    *       *** *** *** *** * *',
    '*      *    ********* *     * *     * *',
    '***************************************',
]



while 1:
    # проверяем события, которые произошли (если они были)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and move == False :
                changeX += -1 * SPEED
                move = True 
            if event.key == pygame.K_RIGHT and move == False:
                changeX = SPEED
                move = True
            
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
    
    herorect_old = herorect.copy()

    platforms = []

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
                
    #провера столкновения 
    for platformrect in platforms:
        if herorect.colliderect(platformrect) == True:
            # collision = True
            move = False
             # движемся налево
            if herorect.left < herorect_old.left:
                herorect.x -= changeX

            # движемся направо
            if herorect.right > herorect_old.right:
                herorect.x -= changeX

        # else:
        #     collision = False
 

        if herorect.colliderect(platformrect) == True :
            # collision = True
            move = False
            # движемся вниз
            if herorect.bottom > herorect_old.bottom:
                herorect.bottom = platformrect.top
                
            if herorect.top < herorect_old.top:
                herorect.top = platformrect.bottom + 10
        # else:
        #     collision = False


    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)

    mainScreen.blit(hero,herorect)

    # print(move)
    pygame.display.flip()
    clock.tick(FPS)
