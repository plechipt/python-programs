import sys 
import time
import random
import pygame

# Basic vars
black_background = (0, 0, 0)
white_color = (255, 255, 255)
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 1000


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
        speed_amount = 0.001

        if pressed[pygame.K_a]:
            self.speed_of_snake += speed_amount 
        elif pressed[pygame.K_d]:
            self.speed_of_snake -= speed_amount 
        elif pressed[pygame.K_s]:
            self.speed_of_snake = 1.25

class Food(Snake):
    def __init__(self, x_food, y_food, x_snake, y_snake, speed_of_snake, current_direction):
        super().__init__(x_snake, y_snake, speed_of_snake, current_direction)
        self.x_food = x_food
        self.y_food = y_food
        self.food_width = 30
        self.food_height = 30
        self.color_of_food = (240, 52, 52, 1)
    
    def draw_food(self, screen):
        positions = self.x_food, self.y_food
        sizes = self.food_width, self.food_height

        pygame.draw.rect(screen, self.color_of_food, ((positions), (sizes)))

    def reset_food(self):
        x_food = random.randint(0, 1150)
        y_food = random.randint(0, 950)

        return x_food, y_food

    def check_snake_ate_food(self):
        x_start =  (self.x_food + self.food_width) > self.x_snake
        x_end = self.x_snake > (self.x_food - self.food_width)
        y_start = (self.y_food + self.food_height) > self.y_snake
        y_end =  self.y_snake > (self.y_food - self.food_height)

        snake_touched_food_x = x_start and x_end
        snake_touched_food_y =  y_start and y_end

        if snake_touched_food_x and snake_touched_food_y:
            return True
        else:
            return False

    def handle_eaten_food(self):
        score_points += 1
        speed_of_snake += 0.1
        x_food, y_food = reset_food()


class Text:
    def __init__(self, score):
        self.score = score
        self.position_of_score = (10, 10)
        self.bigger_font = pygame.font.Font('freesansbold.ttf', 32)
        self.smaller_font = pygame.font.Font('freesansbold.ttf', 20)

    def show_score(self, screen):
        score_text = self.bigger_font.render("Score: " + str(self.score), True, white_color)
        screen.blit(score_text, self.position_of_score)

    def show_keys(self, screen):
        speed_up_text = self.smaller_font.render("A for speed up ", True, white_color)
        slow_down_text = self.smaller_font.render("D for slow down ", True, white_color)
        reset_speed_text = self.smaller_font.render("S for reset speed ", True, white_color)

        screen.blit(speed_up_text, (10, 60))
        screen.blit(slow_down_text, (10, 90))
        screen.blit(reset_speed_text, (10, 120))


class Game(Snake, Text):
    def __init__(self, x_snake, y_snake, speed_of_snake, score):
        super().__init__(x_snake, y_snake, speed_of_snake, score)
        self.snake_width = 30
        self.snake_height = 30
        
    def reset_game(self):
        self.score = 0
        self.speed_of_snake = 1.25
        self.x_snake = (SCREEN_WIDTH - self.snake_width) / 2
        self.y_snake = (SCREEN_HEIGHT - self.snake_height) / 2


def main():
    # Basic config
    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Vars for objects
    width = 250
    height = 250
    speed = 1.25
    score = 0
    direction = 'down'
    random_x = random.randint(0, 1150)
    random_y = random.randint(0, 950)

    # Create objects
    text = Text(score)
    game = Game(height, width, speed, score)
    snake = Snake(width, height, speed, direction)
    food = Food(random_x, random_y, height, width, speed, direction)

    # Main loop
    while True:
        events = pygame.event.get()
        pressed = pygame.key.get_pressed()
        
        for event in events:
            action = event.type

            # Exit
            if action == pygame.QUIT:
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
            game.reset_game()

        ### Food
        # Create food object
        food.draw_food(screen)

        # Check if snake ate food
        snake_ate_food = food.check_snake_ate_food()

        if snake_ate_food:
            food.handle_eaten_food()

        ### Others
        text.show_keys(screen)
        text.show_score(screen)
        snake.handle_speed(pressed)

        pygame.display.update()


if __name__ == '__main__':
    main()