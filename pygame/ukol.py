import pygame
import sys

pygame.init()

# uzivatelske parametry
sirka_okna = 800
vyska_okna = 600

barva_pozadi = (255, 255, 255) #(180, 140, 240)
barva_ctverecku = (90, 170, 250)

sirka = vyska = 50
pozice_x = (sirka_okna - sirka) / 2
pozice_y = (vyska_okna - vyska) / 2
rychlost = 1.5

# inicializace
pygame.display.set_caption("První aplikace v PyGame")
okno = pygame.display.set_mode((sirka_okna, vyska_okna))

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
    
    pygame.draw.circle(okno, barva_ctverecku, ((pozice_x, pozice_y), 5, 20))
    
    pygame.display.update()
