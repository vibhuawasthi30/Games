import time
import random
import pygame
import cv2
import sys
import mediapipe as mp 

pygame.font.init()

# Initialize the score variable outside the game loop
score = 0

# Set up the window
WIDTH, HEIGHT = 1130, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Basketballs")

# Load images
BG = pygame.image.load("Bg.png")
Net = pygame.image.load("Net.png")
Net_width, Net_height = 150, 150
ball = pygame.image.load("ball.png") 

# Player velocity
PLAYER_VEL = 10
STAR_VEL = 5

# Ball Width & Height
BALL_WIDTH = 50
BALL_HEIGHT = 50 # Corrected the variable name

# Font Game
FONT = pygame.font.SysFont("montserrat", 50)

# Function to draw on the window
def draw(player, player_x, elapsed_time, stars, score):
    WIN.blit(BG, (0, 0))
    WIN.blit(player, (player_x, 500))
    for star in stars: 
        # Scale down the ball image
        ball_scaled = pygame.transform.scale(ball, (BALL_WIDTH, BALL_HEIGHT))
        WIN.blit(ball_scaled, (star[0], star[1]))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Display the score on the screen
    score_text = FONT.render(f"Buckets: {score}", 1, "white")
    WIN.blit(score_text, (10, 60))
    pygame.display.update()
       

# Main function
def main(score):
    pygame.init()
    run = True
    player_x = (WIDTH - Net_width) // 2  # Initial x-coordinate of the player
    player = pygame.transform.scale(Net, (Net_width, Net_height))

    # Making Sure That The LOOP is running at the same time 
    clock = pygame.time.Clock()
    # Making A Clock For The Game
    start_time = time.time()
    elapsed_time = 0

    # Making The Basketballs Drop Faster As The Time Goes On
    star_add_increment = 2000 
    star_count = 0

    stars = []
    hit = False

    while run: 
        star_count += clock.tick(60) # Max Frame Per Second
        elapsed_time = time.time() - start_time

        for star in stars:
               star[1] += STAR_VEL
        
        num_iterations = random.randint(3, 5)

        if star_count > star_add_increment:
            for _ in range(num_iterations):
                star_x = random.randint(0, WIDTH - BALL_WIDTH)
                stars.append([star_x, 0])  # Append coordinates of the star
            star_count = 0  # Reset star_count here to continuously add stars
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # For The Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - PLAYER_VEL >= 0:
            player_x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player_x + Net_width + PLAYER_VEL <= WIDTH:
            player_x += PLAYER_VEL

        # Collision detection between stars and player
        for star in stars[:]:
            star_rect = pygame.Rect(star[0], star[1], BALL_WIDTH, BALL_HEIGHT)
            player_rect = pygame.Rect(player_x, 500, Net_width, Net_height)
            if star_rect.colliderect(player_rect):
                stars.remove(star)
                score += 1 # Increase score by 1 when a collision occurs
        
        draw(player, player_x, elapsed_time, stars, score)

    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    main(score)
