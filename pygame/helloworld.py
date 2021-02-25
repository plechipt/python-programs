import sys 
import time
import pygame

pygame.init()

# Basic vars
size = width_window, height_window = 600, 800
white = (255, 255, 255)

# Rectangle
speed = 0.5
x_rect = 250
y_rect = 250
width_rect, height_rect = 50, 50
color_of_rect = (0, 0, 0)

pygame.display.set_caption('Prvni appka v PyGame')
screen = pygame.display.set_mode((width_window, height_window))

def move(x_rect, y_rect):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        x_rect += speed
    if pressed[pygame.K_LEFT]:
        x_rect -= speed
    if pressed[pygame.K_UP]:
        y_rect -= speed
    if pressed[pygame.K_DOWN]:
        y_rect += speed

    return x_rect, y_rect

def border(x_rect, y_rect):
    if x_rect < 0:
        x_rect = 0
    if y_rect < 0:
        y_rect = 0
    if x_rect + width_rect > width_window:
        x_rect = width_window - width_rect
    if y_rect + height_rect > height_window:
        y_rect = height_window - height_rect
    
    return x_rect, y_rect

while True :
    events = pygame.event.get()

    for event in events:
        action = event.type
        
        # Exit
        if action == pygame.QUIT:
            sys.exit()
    
    screen.fill(white)
    x_rect, y_rect = border(x_rect, y_rect)
    x_rect, y_rect = move(x_rect, y_rect)
    
    rectangle = pygame.draw.rect(screen, color_of_rect, ((x_rect, y_rect), (width_rect, height_rect)))
    pygame.display.update()
