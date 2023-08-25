import time

import pygame
from pygame import mixer
from pygame.color import THECOLORS
from new_random import *
from randomizer.instruction import ins

pygame.init()
mixer.init()
screen = pygame.display.set_mode((1000, 800))

res = main_func()
p_he = res[0]
d_he = res[1]
p_she = res[2]
d_she = res[3]


class Sprite:
    def __init__(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def render(self, scrn, pos=(0, 0), ang=0):
        # Поворачиваем картинку
        image = pygame.transform.rotate(self.image, ang)
        self.rect = image.get_rect(center=pos)
        scrn.blit(image, self.rect)
    image = 0


sprite = Sprite('baraban1.png')
angle = 0

clock = pygame.time.Clock()

pygame.display.set_caption('Equal randomizer')
pygame.display.set_icon(pygame.image.load('baraban.bmp'))
pygame.mixer.music.load('pole.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

surf_she = pygame.Surface((450, 500))    # поверхность для размещения на ней списка дел участника 2
surf_he = pygame.Surface((450, 500))    # поверхность для размещения на ней списка дел участника 1
surf_he.fill((34, 177, 76))
surf_she.fill((34, 177, 76))
surf_mem = pygame.Surface((190, 100))    # поверхность для размещения на ней картинки
surf_mem.blit(pygame.image.load('klass.jpg'), (0, 0))
surf_mem_1 = pygame.Surface((190, 100))    # поверхность для размещения на ней другой картинки
surf_mem_1.blit(pygame.image.load('instruction.jpg'), (0, 0))

font_ins = pygame.font.SysFont('couriernew', 25, True)
font = pygame.font.SysFont('couriernew', 30, True)
text = font.render('НАЖМИТЕ ENTER ДЛЯ СТАРТА', True, THECOLORS['white'])
text_ins = font.render('НАЖМИТЕ SPACE ДЛЯ ЧТЕНИЯ ИНСТРУКЦИИ', True, THECOLORS['white'])
text_esc = font.render('НАЖМИТЕ ESCAPE ДЛЯ ВЫХОДА', True, THECOLORS['white'])

surf = pygame.Surface((1000, 800))    # основная поверхность, на которую накладываем другие поверхности
surf.fill((34, 177, 76))
surf.blit(text, (70, 300))
surf.blit(text_ins, (70, 450))
surf.blit(surf_mem, (590, 250))
surf.blit(surf_mem_1, (780, 400))
screen.blit(surf, (0, 0))    # заполняем игровой экран основной поверхностью
pygame.display.update()
while True:
    sprite.render(screen, (500, 120), angle)
    angle += 1
    pygame.display.update()
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        surf.fill((34, 177, 76))
        pygame.display.update()
        time.sleep(1)
        height = 50
        surf_he.blit(font.render('Участник 1:', True, THECOLORS['white']), (40, 0))
        surf.blit(surf_he, (10, 150))
        pygame.display.update()

        for a in list(d_he.items()):
            deal = f'{a[0]} - {a[1]} раз(а)'
            surf_he.blit(font.render(deal, True, THECOLORS['white']), (0, height))
            height += 30
            surf.blit(surf_he, (10, 150))
            screen.blit(surf, (0, 0))
            pygame.display.update()
            time.sleep(1)

        height = 50
        surf_she.blit(font.render('Участник 2:', True, THECOLORS['white']), (40, 0))
        surf.blit(surf_she, (550, 150))
        pygame.display.update()
        time.sleep(1)

        for b in list(d_she.items()):
            deal_she = f'{b[0]} - {b[1]} раз(а)'
            surf_she.blit(font.render(deal_she, True, THECOLORS['white']), (0, height))
            height += 30

            surf.blit(surf_she, (545, 150))
            screen.blit(surf, (0, 0))
            pygame.display.update()
            time.sleep(1)

        surf.blit(text_esc, (280, 600))
        screen.blit(surf, (0, 0))
        pygame.display.update()
    elif keys[pygame.K_SPACE]:
        surf.fill((34, 177, 76))
        H = 200
        for a in ins:
            surf.blit(font_ins.render(a, True, THECOLORS['white']), (30, H))
            H += 30
        screen.blit(surf, (0, 0))
        pygame.display.update()
    elif keys[pygame.K_ESCAPE]:
        surf.fill((34, 177, 76))
        surf.blit(text, (70, 300))
        surf.blit(text_ins, (70, 450))
        surf.blit(surf_mem, (590, 250))
        surf.blit(surf_mem_1, (780, 400))
        screen.blit(surf, (0, 0))
        pygame.display.update()

    pygame.display.update()



        
