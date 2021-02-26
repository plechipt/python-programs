import sys 
import time
import random
import pygame

pygame.init()

# Basic vars
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1000
black_background = (0, 0, 0)
white_color = (255, 255, 255)

# Font
bigger_font = pygame.font.Font('freesansbold.ttf', 32)
smaller_font = pygame.font.Font('freesansbold.ttf', 20)

# Score
score_points = 0
position_of_font = (10, 10)


class Snake:
    def __init__(self, x_snake, y_snake, speed_of_snake, current_direction):
        self.x_snake = x_snake
        self.y_snake = y_snake
        self.speed_of_snake = speed_of_snake
        self.current_direction = current_direction
        self.snake_width = 30
        self.snake_height = 30
        self.color_of_snake = white_color

class Food:
    def __init__(self, x_food, y_food):
        self.x_food = x_food
        self.y_food = y_food
        self.food_width = 30
        self.food_height = 30
        self.color_of_food = (240, 52, 52, 1)


    def reset_food():
        x_food = random.randint(0, 1150)
        y_food = random.randint(0, 950)

        return x_food, y_food

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

def handle_speed(speed_of_snake, pressed):
    speed_amount = 0.001

    if pressed[pygame.K_a]:
        speed_of_snake += speed_amount 
    elif pressed[pygame.K_d]:
        speed_of_snake -= speed_amount 
    elif pressed[pygame.K_s]:
        speed_of_snake = 1.25

    return speed_of_snake

def show_keys():
    speed_up_text = smaller_font.render("A for speed up ", True, white_color)
    slow_down_text = smaller_font.render("D for slow down ", True, white_color)
    reset_speed_text = smaller_font.render("S for reset speed ", True, white_color)

    screen.blit(speed_up_text, (10, 60))
    screen.blit(slow_down_text, (10, 90))
    screen.blit(reset_speed_text, (10, 120))

def show_score():
    score = bigger_font.render("Score: " + str(score_points), True, white_color)
    screen.blit(score, position_of_font)

snake = Snake(250, 250, 1.25, 'down')
food = Food(random.randint(0, 1150), random.randint(0, 950))

def main():
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
        x_food, y_food, score_points, speed_of_snake = handle_eaten_food(
            x_food, y_food, score_points, speed_of_snake
        )

    ### Others
    show_keys()
    show_score()
    speed_of_snake = handle_speed(speed_of_snake, pressed)

    pygame.display.update()


if main == '__main__':
    main()