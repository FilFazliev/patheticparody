import pygame, sys
pygame.init()

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

#платформы 

platform = pygame.image.load('моя игра/block0.png') 

maps =  [
    '***************************************',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '****** *                              *',
    '*      *                              *',
    '*    * ********                       *',
    '*    *        *                       *',
    '*    * ****** *                       *',
    '****** *                              *',
    '*      *                              *',
    '** *** *                              *',
    '*    * ********                       *',
    '*    *        *                       *',
    '*    * ****** *                       *',
    '*    * *    * *   ******* *******     *',
    '*    * *    * *****     * *     * * ***',
    '****** *    *       *** *** *** *** * *',
    '*      *    * ******* *     * *     * *',
    '***************************************',
]



while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    
    #генерация платформ

    platforms = []

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 50 * j
                platformrect.y = 50 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)       

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)

    mainScreen.blit(hero, herorectS)
    pygame.display.flip()
    clock.tick(FPS)