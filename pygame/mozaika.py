import pygame
import random
import sys

pygame.init()

# uzivatelske parametry
sirka_okna = 800
vyska_okna = 600

barva_pozadi = (255, 255, 255)

sirka = vyska = 50
rychlost = 2
pozice_x = (sirka_okna - sirka) / 2
pozice_y = (vyska_okna - vyska) / 2

obrazek = pygame.image.load("images/logo.png")
obrazek = pygame.transform.scale(obrazek, (sirka, vyska))

# inicializace
pygame.display.set_caption("Mozaika")
okno = pygame.display.set_mode((sirka_okna, vyska_okna))

# legracka
xka = []
yka = []
pouzite_umisteni = []
loop = True

for i in range(100):
    while True:
        umisteni_x = (random.randint(1, sirka_okna // sirka))
        umisteni_y = (random.randint(1, vyska_okna // vyska))

        if (umisteni_x, umisteni_y) in pouzite_umisteni:
            continue
        else:
            break
    
    pozice_x = (umisteni_x  - 1) * sirka 
    pozice_y = (umisteni_y - 1) * vyska 

    xka.append(pozice_x)
    yka.append(pozice_y)
    pouzite_umisteni.append((umisteni_x, umisteni_y))

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
