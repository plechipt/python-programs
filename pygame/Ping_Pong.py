import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
    
#main window
screen_width = 1500
screen_height = 1000
backgroud_color = (73, 218, 77)

black_color = (0, 0, 0)
player_color = (45, 200, 227)
white_color = (255, 255, 255)


pygame.display.set_caption("Ping Pong")
window = pygame.display.set_mode((screen_width, screen_height))

#loop
while True:
    events = pygame.event.get()
    pressed = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.quit()

    window.fill(backgroud_color)

    pygame.draw.rect(window, white_color, ((10, 10), (10, 50)))
    pygame.display.flip()
    clock.tick(144)