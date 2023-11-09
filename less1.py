import pygame

pygame.init()

W, H = 800, 600
display = pygame.display.set_mode((W, H))

sprite = pygame.image.load('res/crosshair_small.png')
hitbox = sprite.get_rect()
sprite2 = pygame.image.load('res/target_small.png')
hitbox2 = sprite.get_rect()


def main():
    while True:
        # 1) Считывание ввода
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        # 2) Обновление состояния игры

        # -----------------
        # 3) Отрисовка обновленного состояния
        pygame.display.update()
        # -----------------


main()
