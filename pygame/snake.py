import sys 
import time
import random
import pygame

pygame.init()

# Basic vars
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1000
black_background = (0, 0, 0)
white_color = (255, 255, 255)

# Score
score_points = 0
position_of_font = (10, 10)
font = pygame.font.Font('freesansbold.ttf', 32)

# Snake
x_snake = 250
y_snake = 250
speed_of_snake = 1.25
snake_width, snake_height = 30, 30
color_of_snake = white_color
current_direction = 'down'

snake_parts = []
snake_parts_count = 0

# Food
def reset_food():
    x_food = random.randint(0, 1150)
    y_food = random.randint(0, 950)

    return x_food, y_food

x_food, y_food = reset_food()
food_width, food_height = 30, 30
color_of_food = (240, 52, 52, 1)

pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Functions part
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
        x_snake += speed_of_snake
    if current_direction == 'left':
        x_snake -= speed_of_snake
    if current_direction == 'up':
        y_snake -= speed_of_snake
    if current_direction == 'down':
        y_snake += speed_of_snake

    return x_snake, y_snake

def check_snake_touched_border(x_snake, y_snake):
    snake_touched_x_border = x_snake < 0 or x_snake + snake_width > SCREEN_WIDTH
    snake_touched_y_border = y_snake < 0 or y_snake + snake_height > SCREEN_HEIGHT

    if (snake_touched_x_border or snake_touched_y_border):
        return True
    else:
        return False

def handle_snake_touched_border(x_snake, y_snake, score_points, speed_of_snake):
    score_points = 0
    speed_of_snake = 1.25
    x_snake = (SCREEN_WIDTH - snake_width) / 2
    y_snake = (SCREEN_HEIGHT - snake_height) / 2

    return x_snake, y_snake, score_points, speed_of_snake

def check_snake_ate_food(x_snake, y_snake, x_food, y_food):
    snake_touched_food_x = (x_food + food_width) > x_snake and x_snake > (x_food - food_width)
    snake_touched_food_y = (y_food + food_height) > y_snake and y_snake > (y_food - food_height)

    if snake_touched_food_x and snake_touched_food_y:
        return True
    else:
        return False

def handle_eaten_food(x_food, y_food, score_points, speed_of_snake):
    score_points += 1
    speed_of_snake += 0.1
    x_food, y_food = reset_food()

    return x_food, y_food, score_points, speed_of_snake

def show_score():
    score = font.render("Score: " + str(score_points), True, white_color)
    screen.blit(score, position_of_font)


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
    snake_touched_border = check_snake_touched_border(x_snake, y_snake)

    if snake_touched_border:
        x_snake, y_snake, score_points, speed_of_snake = handle_snake_touched_border(
            x_snake, y_snake, score_points, speed_of_snake
        )

    ### Food
    # Food object
    food = pygame.draw.rect(screen, color_of_food, ((x_food, y_food), (food_width, food_height)))

    # Check if snake ate food
    snake_ate_food = check_snake_ate_food(x_snake, y_snake, x_food, y_food)

    if snake_ate_food:
        x_food, y_food, score_points, speed_of_snake = handle_eaten_food(x_food, y_food, score_points, speed_of_snake)

    show_score()
    pygame.display.update()
