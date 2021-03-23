import pygame
import random
import sys

pygame.init()

# uzivatelske parametry
sirka_okna = 800
vyska_okna = 600

barva_pozadi = (255, 255, 255)

sirka = vyska = 50
rychlost = 0.5
pozice_x = (sirka_okna - sirka) / 2
pozice_y = (vyska_okna - vyska) / 2

obrazek = pygame.image.load("logo.png")
obrazek = pygame.transform.scale(obrazek, (sirka, vyska))

# inicializace
pygame.display.set_caption("Mozaika")
okno = pygame.display.set_mode((sirka_okna, vyska_okna))

# legracka
xka = []
yka = []

for i in range(100):
    xka.append((random.randint(0, sirka_okna // sirka) - 1) * sirka)
    yka.append((random.randint(0, vyska_okna // vyska) - 1) * vyska)

# vykreslovaci smycka
while True:
    stisknuto = pygame.key.get_pressed()
    udalosti = pygame.event.get()
    
    # vypinani
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    # ovladani
    if stisknuto[pygame.K_RIGHT]:
        pozice_x += rychlost
    if stisknuto[pygame.K_LEFT]:
        pozice_x -= rychlost
    if stisknuto[pygame.K_DOWN]:
        pozice_y += rychlost
    if stisknuto[pygame.K_UP]:
        pozice_y -= rychlost
    if stisknuto[pygame.K_SPACE]:
        pozice_x = (sirka_okna - sirka) / 2
        pozice_y = (vyska_okna - vyska) / 2
    
    # omezeni pohybu
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    if pozice_x + sirka > sirka_okna:
        pozice_x = sirka_okna - sirka
    if pozice_y + vyska > vyska_okna:
        pozice_y = vyska_okna - vyska
        
    # vykreslovani
    okno.fill(barva_pozadi)
    
    for i in range(len(xka)):
        okno.blit(obrazek, (xka[i], yka[i]))
    else:
        okno.blit(obrazek, (pozice_x, pozice_y))
    
    pygame.display.update()
