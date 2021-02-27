import sys 
import time
import random
import pygame

# Basic vars
black_background = (0, 0, 0)
white_color = (255, 255, 255)
directions = ['left', 'right', 'up', 'down']
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 1000


class Snake:
    def __init__(self, x_snake, y_snake, speed_of_snake, current_direction):
        self.x_snake = x_snake
        self.y_snake = y_snake
        self.speed_of_snake = speed_of_snake
        self.current_direction = current_direction
        self.snake_width = 30
        self.snake_height = 30
        self.color_of_snake = white_color

    def draw_snake(self, screen):
        positions = self.x_snake, self.y_snake
        sizes = self.snake_width, self.snake_height

        snake = pygame.draw.rect(screen, self.color_of_snake, ((positions), (sizes)))
    
    def change_direction(self, pressed):
        if pressed[pygame.K_RIGHT]:
            self.current_direction = 'right'
        if pressed[pygame.K_LEFT]:
            self.current_direction = 'left'
        if pressed[pygame.K_UP]:
            self.current_direction = 'up'
        if pressed[pygame.K_DOWN]:
            self.current_direction = 'down'

    def move(self):
        if self.current_direction == 'right':
            self.x_snake += self.speed_of_snake
        if self.current_direction == 'left':
            self.x_snake -= self.speed_of_snake
        if self.current_direction == 'up':
            self.y_snake -= self.speed_of_snake
        if self.current_direction == 'down':
            self.y_snake += self.speed_of_snake

    def check_snake_touched_border(self):
        snake_touched_x_border = self.x_snake < 0 or self.x_snake + self.snake_width > SCREEN_WIDTH
        snake_touched_y_border = self.y_snake < 0 or self.y_snake + self.snake_height > SCREEN_HEIGHT

        if (snake_touched_x_border or snake_touched_y_border):
            return True
        else:
            return False

    def handle_speed(self, pressed):
        speed_amount = 0.01

        if pressed[pygame.K_a]:
            self.speed_of_snake += speed_amount 
        if pressed[pygame.K_d] and self.speed_of_snake >= 0:
            self.speed_of_snake -= speed_amount 
        if pressed[pygame.K_SPACE]:
            self.speed_of_snake = 1.25

class Food:
    def __init__(self, x_food, y_food,):
        self.x_food = x_food
        self.y_food = y_food
        self.food_width = 30
        self.food_height = 30
        self.color_of_food = (240, 52, 52, 1)
    
    def draw_food(self, screen):
        positions = self.x_food, self.y_food
        sizes = self.food_width, self.food_height

        pygame.draw.rect(screen, self.color_of_food, ((positions), (sizes)))

       
class Text:
    def __init__(self, score, last_score, best_score):
        self.score = score
        self.last_score = last_score
        self.best_score = best_score
        self.position_of_key_y = 140
        self.position_of_score = (10, 10)
        self.position_of_last_score = (10, 50)
        self.position_of_best_score = (10, 90)
        self.bigger_font = pygame.font.Font('freesansbold.ttf', 30)
        self.smaller_font = pygame.font.Font('freesansbold.ttf', 20)

    def show_score(self, screen):
        score_text = self.bigger_font.render("Score: " + str(self.score), True, white_color)
        last_score_text = self.bigger_font.render("Last Score: " + str(self.last_score), True, white_color)
        best_score_text = self.bigger_font.render("Best score: " + str(self.best_score), True, white_color)

        screen.blit(score_text, self.position_of_score)
        screen.blit(last_score_text, self.position_of_last_score)
        screen.blit(best_score_text, self.position_of_best_score)

    def show_keys(self, screen):
        speed_up_text = self.smaller_font.render("A for speed up ", True, white_color)
        slow_down_text = self.smaller_font.render("D for slow down ", True, white_color)
        reset_speed_text = self.smaller_font.render("SPACE for reset speed ", True, white_color)

        screen.blit(speed_up_text, (10, self.position_of_key_y))
        screen.blit(slow_down_text, (10, self.position_of_key_y + 30))
        screen.blit(reset_speed_text, (10, self.position_of_key_y + 60))


# Functions
def check_snake_ate_food(snake, food):
    x_start =  (food.x_food + food.food_width) > snake.x_snake
    x_end = snake.x_snake > (food.x_food - food.food_width)
    y_start = (food.y_food + food.food_height) > snake.y_snake
    y_end =  snake.y_snake > (food.y_food - food.food_height)
 
    snake_touched_food_x = x_start and x_end
    snake_touched_food_y =  y_start and y_end

    if snake_touched_food_x and snake_touched_food_y:
        return True
    else:
        return False

def reset_food():
    random_x = random.randint(250, SCREEN_WIDTH - 50)
    random_y = random.randint(0, SCREEN_HEIGHT - 50)

    return random_x, random_y


def main():
    # Basic config
    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Vars for objects
    speed = 1.75
    direction = random.choice(directions)
    width = SCREEN_WIDTH / 2
    height = SCREEN_HEIGHT / 2
    position_x, position_y = reset_food()

    # Create objects
    text = Text(0, 0, 0)
    snake = Snake(width, height, speed, direction)
    food = Food(position_x, position_y)

    # Main loop
    while True:
        events = pygame.event.get()
        pressed = pygame.key.get_pressed()
        
        for event in events:
            action = event.type

            # Exit
            if action == pygame.QUIT or pressed[pygame.K_ESCAPE]:
                sys.exit()

        # Fill background with black color
        screen.fill(black_background)

        ### Snake
        # Create snake object 
        snake.draw_snake(screen)

        # Change direction if user pressed arrow key
        snake.change_direction(pressed)

        # Move snake in current direction
        snake.move()

        # Check if snake touched border
        snake_touched_border = snake.check_snake_touched_border()

        if snake_touched_border:
            # Restart game
            if text.score > text.last_score:
                text.best_score = text.score

            text.last_score = text.score
            text.score = 0
            snake.speed_of_snake = speed
            snake.current_direction = random.choice(directions)
            snake.x_snake = (SCREEN_WIDTH - snake.snake_width) / 2
            snake.y_snake = (SCREEN_HEIGHT - snake.snake_height) / 2

        ### Food
        # Create food object
        food.draw_food(screen)

        # Check if snake ate food
        snake_ate_food = check_snake_ate_food(snake, food)

        if snake_ate_food:
            # Handle snake ate food
            text.score += 1
            snake.speed_of_snake += 0.2
            food.x_food, food.y_food = reset_food()

        ### Others
        text.show_keys(screen)
        text.show_score(screen)
        snake.handle_speed(pressed)

        pygame.display.update()


if __name__ == '__main__':
    main()