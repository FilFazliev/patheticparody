import pygame, sys
pygame.init()
from os import path
# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

SPEED = 60
changeX = 0
changeY = 0


#платформы 

platform = pygame.image.load('моя игра/block0.png') 

#персонаж

herostand = pygame.image.load('моя игра/pers3.png')
heror = pygame.image.load('моя игра/pers.png')
heromover = pygame.image.load('моя игра/pers2.png')

hero = herostand
herorect = hero.get_rect()
herorect.bottom = HEIGHT-150
herorect.left = WIDTH-1600

SPEED = 10
changeX = 0
changeY = 0

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
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX += -1 * SPEED
            if event.key == pygame.K_RIGHT:
                changeX = SPEED
                herorect.x += changeX
            if event.key == pygame.K_UP:
                changeY = -1 * SPEED
                
            if event.key == pygame.K_DOWN :
                changeY = SPEED
            if pygame.K_ESCAPE:
                sys.exit()
    herorect_old = herorect.copy()

    platforms = []

    
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
            # движемся налево
            if herorect.left < herorect_old.left:
                herorect.x -= changeX
                # herorect.left = platformrect.right

            # движемся направо
            if herorect.right > herorect_old.right:
                herorect.x -= changeX
                # herorect.left = platformrect.right

        if herorect.colliderect(platformrect) == True:
            # движемся вниз
            if herorect.bottom > herorect_old.bottom:
                herorect.bottom = platformrect.top
                
            if herorect.top < herorect_old.top:
                herorect.top = platformrect.bottom


    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)

    mainScreen.blit(hero,herorect)

    pygame.display.flip()
    clock.tick(FPS)
