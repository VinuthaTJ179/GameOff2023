import random
import pygame
import time 
import button 

pygame.init()


WIDTH = 900
HEIGHT = 500
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 0)
pygame.display.set_caption('Flappy Space')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',20)
font1 = pygame.font.Font("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\pixelmix.ttf", 45)


x,y = 0,0
clock = pygame.time.Clock()
fps = 60

# Set the dimensions of your screen
screen_width = 900
screen_height = 500
x, y = 0, 0

# Create the screen with double buffering
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)

start_img = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\start_img.png").convert_alpha()
exit_img = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\exit_img.png").convert_alpha()


start_button = button.Button(335, 150, start_img, 0.8)
exit_button = button.Button(350, 280, exit_img, 0.8)

splash_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\cityskyline.png")
second_screen_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\bluemoon.png")

text_color = (255, 255, 255)
text_surface = font.render('', True, text_color)

text_x = 225
text_y = 225

SPLASH_SCREEN = 0
SECOND_SCREEN = 1
current_state = SPLASH_SCREEN

transition_duration = 5000
start_time = pygame.time.get_ticks()
alpha = 255
fade_speed = 2

animation_text = "Flappy space"
animation_speed = 7
current_letter_index = 0
time_last_letter_displayed = time.time()




def run():
    global generate_places, obstacles, y_positions, game_over, score, high_score, player_x, player_y
    global y_change 
    WIDTH = 900
    HEIGHT = 500
    fps = 60
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (128, 128, 128)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    pygame.display.set_caption('Flappy Space')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    timer = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf',20)


    # player
    player_x = 225
    player_y = 225
    y_change = 0
    jump_height = 12
    gravity = 0.9
    obstacles = [400, 700, 1000, 1300, 1600]
    generate_places = True
    y_positions = []
    game_over = False
    speed = 3     
    score = 0
    high_score = 0


    def draw_player(x_pos, y_pos):
        global y_change

        # Load the player image
        player_image = pygame.image.load("C:\\Users\\Vinutha TJ\\OneDrive\\Desktop\\GameOff2023\\honeybee.png").convert_alpha()
        
        # Resize the image if needed
        player_image = pygame.transform.scale(player_image, (90, 110))

        # Draw the player image
        screen.blit(player_image, (x_pos, y_pos))

        return pygame.Rect(x_pos, y_pos, 30, 50)



    def draw_obstacles(obst, y_pos, play):
        global game_over
        for i in range(len(obst)):
            y_coord = y_pos[i]
            top_rect = pygame.draw.rect(screen, grey, [obst[i], 0, 30, y_coord])
            top2 = pygame.draw.rect(screen,grey,[obst[i]-3,y_coord - 20,36,20],0,5)
            bot_rect = pygame.draw.rect(screen, grey, [obst[i], y_coord + 200, 30, HEIGHT - (y_coord + 70)])
            bot2 = pygame.draw.rect(screen,grey,[obst[i]-3,y_coord + 200,36,20],0,5)
            if top_rect.colliderect(player) or bot_rect.colliderect(player):
                game_over = True



    running = True
    while running:
        timer.tick(fps)
        #screen.fill(black)
        screen.blit(second_screen_image, (0, 0))
        if generate_places:
            for i in range(len(obstacles)):
                y_positions.append(random.randint(0, 300))
            generate_places = False

        player = draw_player(player_x, player_y)
        draw_obstacles(obstacles, y_positions, player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    y_change = -jump_height
                if event.key == pygame.K_SPACE and game_over:
                    player_y = 225 
                    player_x = 225
                    y_change = 0
                    generate_places = True
                    obstacles = [400, 700, 1000, 1300, 1600]
                    y_positions = []
                    score = 0
                    game_over = False

        if player_y + y_change < HEIGHT - 30:
            player_y += y_change
            y_change += gravity
        else:
            player_y = HEIGHT - 30

        for i in range(len(obstacles)):
            if not game_over:
                obstacles[i] -= speed
                if obstacles[i] < -30:
                    obstacles.remove(obstacles[i])
                    y_positions.remove(y_positions[i])
                    obstacles.append(random.randint(obstacles[-1] + 280, obstacles[-1] + 320))
                    y_positions.append(random.randint(0,300))
                    score += 1
        if score > high_score:
            high_score = score
        if game_over:
            game_over_text = font.render('Game Over! Press Space Bar to restart',True,white)
            screen.blit(game_over_text,(250,250))



        score_text = font.render('Score: ' + str(score), True, white)
        screen.blit(score_text,(10,450))
        high_score_text = font.render('High Score: ' + str(high_score), True, white)
        screen.blit(high_score_text,(10,470))

        pygame.display.flip()

    pygame.quit()





running = True
while running:
    timer.tick(fps)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if current_state == SPLASH_SCREEN:
        screen.fill((0, 0, 0))
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= transition_duration:
            current_state = SECOND_SCREEN
        screen.blit(splash_image, (x, y))

        time_now = time.time()
        time_since_last_display = time_now - time_last_letter_displayed

        if current_letter_index < len(animation_text) and time_since_last_display >= 1 / animation_speed:
            text_surface = font1.render(animation_text[:current_letter_index + 1], True, (0,0,0))
            time_last_letter_displayed = time_now
            current_letter_index += 1

        screen.blit(text_surface, (text_x, text_y))
    elif current_state == SECOND_SCREEN:
        screen.blit(second_screen_image, (0, 0))

        if start_button.draw(screen):
            run()

        if exit_button.draw(screen):
            running = False

        if alpha > 0:
            overlay = pygame.Surface((900, 500))
            overlay.set_alpha(alpha)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            alpha = max(0, alpha - fade_speed)
    
    pygame.display.update()

pygame.quit()
