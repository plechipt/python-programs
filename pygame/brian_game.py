import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
TPS = 60

#screen
screen_width = 1500
screen_height = 1000
backgroud_color = (255, 255, 255)
bg_img = pygame.image.load("images/sky.jpg")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
#player
player_height = 60
player_width = 60
player_pos_x = 720
player_pos_y = 830
player_img = pygame.image.load("images/mushroom.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
score = 0
#falling enteties
block_width = 60
block_height = 60
block_num = 3
block_speed = 4
block_img = pygame.image.load("images/death.png")
block_img = pygame.transform.scale(block_img, (block_width, block_height))
block = []
for q in range(block_num):
    x = random.randrange(0, screen_width - block_width)
    y = random.randrange(0, screen_height)
    print(x,y)
    block.append([x,y])



#tile
tile_pos_x = 620
tile_pos_y = 10
tile_height = 90
tile_width = 90
tile_img = pygame.image.load("images/death.png")
tile_img = pygame.transform.scale(tile_img, (tile_width, tile_height))

pygame.display.set_caption("platformer")
window = pygame.display.set_mode((screen_width, screen_height))

#score
scoreX = 10
scoreY = 10
score_val = 0
#urded
urdedX = screen_width/2 - 170
urdedY = screen_height/2 + 50
#pohyb
rychlost = 10


#loop
while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    #omezeni pohybu
    if player_pos_x >= screen_width - player_width:
        player_pos_x = screen_width - player_width
    if player_pos_x <= 0:
        player_pos_x = 0
    if player_pos_y >= screen_height - player_height:
        player_pos_y = screen_height - player_height
    if player_pos_y <= 0:
        player_pos_y = 0    
    
    #pohyb
    if pressed[pygame.K_RIGHT]:
        player_pos_x += rychlost
    if pressed[pygame.K_UP]:
        player_pos_y -= rychlost
    if pressed[pygame.K_LEFT]:
        player_pos_x -= rychlost
    if pressed[pygame.K_DOWN]:
        player_pos_y += rychlost


    #score
    score_val += 1
    font = pygame.font.Font("freesansbold.ttf",28)
    score = font.render("Score: " + str(score_val),True, (255, 255, 255))
        
    #urded
    urded = font.render("YOU ARE DEAD", True, (0, 0, 0))
    

    
    #drawing
    window.fill(backgroud_color)
    window.blit(bg_img, (0, 0))
    window.blit(player_img, (player_pos_x, player_pos_y))

    #block
    for i in block:
        i[1] += block_speed
        window.blit(block_img, (i))
        if i[1] > screen_height:
            i[1] = random.randrange(-50,-5)
            i[0] = random.randrange(screen_width - block_width)

        if player_pos_y <= i[1] + block_height and player_pos_y + player_height >= i[1] and player_pos_x + player_width >= i[0] and player_pos_x <= i[0] + block_width:
            window.blit(urded, (urdedX, urdedY))
            score_val -= 1
            rychlost = 0
            block_speed = 0

        if i[1] >= screen_height + tile_height:
            i[1] = random.randrange(-300,-30)
            i[0] = random.randrange(0,screen_width - tile_width)



    window.blit(score, (scoreX, scoreY))
    pygame.display.flip()
    clock.tick(TPS)