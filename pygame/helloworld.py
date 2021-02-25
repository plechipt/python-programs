import sys 
import time
import pygame

pygame.init()

# Basic vars
size = width, height = (600, 800)
white = (255, 255, 255)

# Rectangle
speed = 50 
x_rect = 250
y_rect = 250
size_of_rect = (50, 50)
color_of_rect = (0, 0, 0)

pygame.display.set_caption('Prvni appka v PyGame')
screen = pygame.display.set_mode(size)

def move(key, x_rect, y_rect):
    if key == pygame.K_RIGHT:
        x_rect += speed
    elif key == pygame.K_LEFT:
        x_rect -= speed
    elif key == pygame.K_UP:
        y_rect -= speed
    elif key == pygame.K_DOWN:
        y_rect += speed

    return x_rect, y_rect


while True :
    events = pygame.event.get()
    screen.fill(white)

    for event in events:
        action = event.type
        if action == pygame.KEYDOWN:
            key = event.key
            x_rect, y_rect = move(key, x_rect, y_rect)

        # Exit
        if action == pygame.QUIT:
            sys.exit()
    
    if x_rect > 500:
        x_rect = 250

    rectangle = pygame.draw.rect(screen, color_of_rect, ((x_rect, y_rect), size_of_rect))
    pygame.display.update()
