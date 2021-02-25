import sys 
import time
import pygame

pygame.init()

# Basic vars
size = width_window, height_window = 1200, 1000
black_background = (0, 0, 0)

# Snake
speed = 1 
x_snake = 250
y_snake = 250
width_snake, height_snake = 30, 30
color_of_snake = (255, 255, 255)
current_direction = 'down'

pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode((width_window, height_window))

def change_direction(current_direction, pressed):
    if pressed[pygame.K_RIGHT]:
        current_direction = 'right'
    if pressed[pygame.K_LEFT]:
        current_direction = 'left'
    if pressed[pygame.K_UP]:
        current_direction = 'up'
    if pressed[pygame.K_DOWN]:
        current_direction = 'down'

    return current_direction

def move(current_direction, x_snake, y_snake):
    if current_direction == 'right':
        x_snake += speed
    if current_direction == 'left':
        x_snake -= speed
    if current_direction == 'up':
        y_snake -= speed
    if current_direction == 'down':
        y_snake += speed

    return x_snake, y_snake

def border(x_snake, y_snake):
    snake_touched_x_border = x_snake < 0 or x_snake + width_snake > width_window
    snake_touched_y_border = y_snake < 0 or y_snake + height_snake > height_window

    if (snake_touched_x_border or snake_touched_y_border):
        x_snake = (width_window - width_snake) / 2
        y_snake = (height_window - height_snake) / 2

    return x_snake, y_snake


while True:
    events = pygame.event.get()
    pressed = pygame.key.get_pressed()
    
    for event in events:
        action = event.type
        # Exit
        if action == pygame.QUIT:
            sys.exit()

    screen.fill(black_background)

    current_direction = change_direction(current_direction, pressed)
    x_snake, y_snake = border(x_snake, y_snake)
    x_snake, y_snake = move(current_direction, x_snake, y_snake)

    snake = pygame.draw.rect(screen, color_of_snake, ((x_snake, y_snake), (width_snake, height_snake)))
    pygame.display.update()
