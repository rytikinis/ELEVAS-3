#SetUp#
import pygame, sys
from Data import Stars as stars
from Data import Time as time
from Data import Intro as intro
pygame.init()
intro.get_info()
WIN = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
time.SetUp()
pygame.display.set_caption("ELEVAS")
pygame.display.set_icon(pygame.image.load("Data/Images/Icon.png"))
fps = pygame.time.Clock()
p = False
pressed = False
play = pygame.transform.scale(pygame.image.load("Data/Images/Play.png"), (30, 30))
pause = pygame.transform.scale(pygame.image.load("Data/Images/Pause.png"), (30, 30))
#Set data to int#
data = list(intro.data)
for a in range(len(data)):
    try:
        data[a] = int(data[a])
    except:
        pass
stars.SetUp(data[7], data[8])
#Keys#
class keys():
    m1 = False
    s = 1
#Loop#
while True:
    #FPS#
    fps.tick(60)
    #Backround#
    WIN.fill((0, 0, 0))
    #Events#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                keys.m1 = True
            if event.button == 4:
                keys.s += 0.05
            if event.button == 5 and keys.s > 0:
                keys.s -= 0.05
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                keys.m1 = False
    #Mouse#
    mx, my = pygame.mouse.get_pos()
    mouser = pygame.Rect(mx, my, 2, 2)
    #Pause#, 
    if p:
        h = WIN.blit(play, (20, 50))
    elif not p:
        h = WIN.blit(pause, (20, 50))
    if mouser.colliderect(h) and keys.m1 and not pressed:
        pressed = True
        if not p:
            p = True
        elif p:
            p = False
    if not keys.m1:
        pressed = False
    #Time#
    if not p:
        time.update(fps.get_fps(), data[9])
    #Stars#
    if not p:
        stars.formate_stars(data[0], True, fps.get_fps(), data[2], data[3], data[5], data[4], data[1], data[6], data[9])
    stars.update(WIN, fps.get_fps(), keys.m1, mx, my, keys.s, p, data[7], data[9])
    #Update display#
    pygame.display.update()