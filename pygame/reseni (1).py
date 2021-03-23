# Import knihoven
import pygame
import random
import sys

# Uživatelské parametry
sirka_okna = 800
vyska_okna = 600
pocet_log = 100
barva_pozadi = (255, 255, 255)
pruhlednost_log = 255  # 0 = kompletně průhledné, 255 = neprůhledné
sirka = vyska = 50
rychlost = 1
pozice_x = (sirka_okna - sirka) / 2
pozice_y = (vyska_okna - vyska) / 2
xka = []
yka = []
souradnice_list = []

# Inicializace
pygame.init()
obrazek = pygame.image.load("images/logo.png")
obrazek = pygame.transform.scale(obrazek, (sirka, vyska))
obrazek.set_alpha (pruhlednost_log)
pygame.display.set_caption("Mozaika")
okno = pygame.display.set_mode((sirka_okna, vyska_okna))

# Určení pozic log
for i in range(pocet_log-1):
    xka.append((random.randint(0, sirka_okna // sirka))* sirka)
    while xka[i] >= sirka_okna: # Kontrola, aby se logo nevykreslilo mimo okno
        xka[i] -= 50
        print("xka přesáhla ", sirka_okna)

    yka.append((random.randint(0, vyska_okna // vyska))* vyska)
    while yka[i] >= vyska_okna: # Kontrola, aby se logo nevykreslilo mimo okno
        yka[i] -= 50
        print("yka přesáhla ", vyska_okna)
     
    souradnice = [xka[i],yka[i]] # Sloučení xka a yka do jednoho listu
    while souradnice in souradnice_list: # Hledání souřadnice v listu souřadnic, jestli se zde již vyskytuje, pokud ano tak se vypočítá nová, náhodná souřadnice pro dané logo, pokud se vyskytuje i nová souřadnice v listu, tak se generuje nová dokud se najde souřadnice, která v listu není.
        xka[i] = ((random.randint(0, sirka_okna // sirka))* sirka)
        yka[i] = ((random.randint(0, sirka_okna // sirka))* sirka)
        souradnice = [xka[i],yka[i]] # Aktualizace listu pro souradnice (aby se neloopovalo dokola)
        print("pozice loga", [i],"byla upravena na", souradnice)
        
    souradnice_list.append(souradnice) # Přídání nové souřadnice to listu souřadnic (aby se v budoucnu neopakovala)
              
   # Vykreslovací smyčka
while True:
    stisknuto = pygame.key.get_pressed()
    udalosti = pygame.event.get()
    
    # Vypínaní
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    # Ovládání loga
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
    
    # Omezení pohybu
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    if pozice_x + sirka > sirka_okna:
        pozice_x = sirka_okna - sirka
    if pozice_y + vyska > vyska_okna:
        pozice_y = vyska_okna - vyska
        
    # Vykreslování
    okno.fill(barva_pozadi)
    
    for i in range(len(xka)):
        okno.blit(obrazek, (xka[i], yka[i]))
    else:
        okno.blit(obrazek, (pozice_x, pozice_y))
    
    pygame.display.update()
