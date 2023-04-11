import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)


# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

SPEED = 60
changeX = 0
changeY = 0


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
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '***********************************   *',
    '*                                     *',
    '*                                     *',
    '***************************************',
]



while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    herorect_old = herorect.copy()


    platforms = []

    #движение
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED
        

    if keys[pygame.K_RIGHT]:
        changeX = SPEED
        

    if keys[pygame.K_UP]:
        changeY = -1 * SPEED
        

    if keys[pygame.K_DOWN]:
        changeY = SPEED
        

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
        changeY = 0

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        changeX = 0


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

    # границы

    
    

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    herorect.x += changeX
    herorect.y += changeY

    
    #рисовка плаформ 
    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)

    mainScreen.blit(hero,herorect)

    pygame.display.flip()
    clock.tick(FPS)