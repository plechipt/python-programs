import sys 
import time
import random
import pygame

pygame.init()

# Basic vars
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1000
black_background = (0, 0, 0)

speed = 1.25
x_snake = 250
y_snake = 250
snake_width, snake_height = 30, 30
color_of_snake = (255, 255, 255)
current_direction = 'down'

snake_parts = []
snake_parts_count = 0

# Food
def reset_food():
    print('test')
    x_food = random.randint(0, 1150)
    y_food = random.randint(0, 950)

    return x_food, y_food

x_food, y_food = reset_food()
food_width, food_height = 30, 30
color_of_food = (240, 52, 52, 1)

pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    snake_touched_x_border = x_snake < 0 or x_snake + snake_width > SCREEN_WIDTH
    snake_touched_y_border = y_snake < 0 or y_snake + snake_height > SCREEN_HEIGHT

    if (snake_touched_x_border or snake_touched_y_border):
        x_snake = (SCREEN_WIDTH - snake_width) / 2
        y_snake = (SCREEN_HEIGHT - snake_height) / 2

    return x_snake, y_snake

def snake_ate_food(x_snake, y_snake, x_food, y_food):
    snake_touched_food_x = (x_food + food_width) > x_snake and x_snake > (x_food - food_width)
    snake_touched_food_y = (y_food + food_height) > y_snake and y_snake > (y_food - food_height)

    if snake_touched_food_x and snake_touched_food_y:
        x_food, y_food = reset_food()

    return x_food, y_food



while True:
    events = pygame.event.get()
    pressed = pygame.key.get_pressed()
    
    for event in events:
        action = event.type

        # Exit
        if action == pygame.QUIT:
            sys.exit()

    screen.fill(black_background)
    
    ### Snake
    # Snake object
    snake = pygame.draw.rect(screen, color_of_snake, ((x_snake, y_snake), (snake_width, snake_height)))

    # Change direction if user pressed arrow key
    current_direction = change_direction(current_direction, pressed)

    # Move snake in current direction
    x_snake, y_snake = move(current_direction, x_snake, y_snake)

    # Check if snake touched border
    x_snake, y_snake = border(x_snake, y_snake)

    ### Food
    # Food object
    food = pygame.draw.rect(screen, color_of_food, ((x_food, y_food), (food_width, food_height)))

    # Check if snake ate food
    x_food, y_food = snake_ate_food(x_snake, y_snake, x_food, y_food)

    pygame.display.update()
