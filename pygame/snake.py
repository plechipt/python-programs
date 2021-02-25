import sys 
import time
import pygame

pygame.init()

# Basic vars
size = width, height = (1200, 1000)
black_background = (0, 0, 0)

# Rectangle
speed = 1 
x_rect = 250
y_rect = 250
size_of_rect = (50, 50)
color_of_rect = (255, 255, 255)

pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode(size)

def move(pressed, x_rect, y_rect):
    if pressed[pygame.K_RIGHT]:
        x_rect += speed
    elif pressed[pygame.K_LEFT]:
        x_rect -= speed
    elif pressed[pygame.K_UP]:
        y_rect -= speed
    elif pressed[pygame.K_DOWN]:
        y_rect += speed

    return x_rect, y_rect


while True :
    events = pygame.event.get()
    pressed = pygame.key.get_pressed()
    screen.fill(black_background)
    
    for event in events:
        action = event.type
        # Exit
        if action == pygame.QUIT:
            sys.exit()

    x_rect, y_rect = move(pressed, x_rect, y_rect)
    rectangle = pygame.draw.rect(screen, color_of_rect, ((x_rect, y_rect), size_of_rect))
    pygame.display.update()
