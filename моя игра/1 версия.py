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

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

    pygame.display.flip()
    clock.tick(FPS)