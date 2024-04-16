import random
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
White = (255, 255, 255)
Black = (0, 0, 0)
gray = (128, 128, 128)
blue = (0, 0, 255)
green = (0, 255, 0)

fps = 60
timer = pygame.time.Clock()

rows = 6
cols = 8

correct = [[0] * cols for _ in range(rows)]
new_board = True

option_list = []
spaces = []
used = []
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0

score = 0
matches = 0
lives = 3
high_score = 0

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Vibhu's Matching Game !")
title_font = pygame.font.Font("freesansbold.ttf", 50)
small_font = pygame.font.Font("freesansbold.ttf", 26)

def generate_board():
    global option_list
    global spaces

    for item in range(rows * cols // 2):
        option_list.append(item)
        option_list.append(item)

    random.shuffle(option_list)
    spaces = option_list.copy()

def draw_background():
    screen.fill(Black)
    pygame.draw.rect(screen, White, [0, 0, WIDTH, 100])
    title_text = title_font.render("Vibhu's Matching Game", True, Black)
    screen.blit(title_text, (10, 20))
    pygame.draw.rect(screen, gray, [0, 100, WIDTH, HEIGHT-200], 0)
    pygame.draw.rect(screen, White, [0, HEIGHT - 100, WIDTH, 100], 0)

    # Display lives and high score
    lives_text = small_font.render(f"Lives: {lives}", True, White)
    screen.blit(lives_text, (10, HEIGHT - 80))

    high_score_text = small_font.render(f"High Score: {high_score}", True, White)
    screen.blit(high_score_text, (WIDTH - 200, HEIGHT - 80))

def draw_board():
    global rows 
    global cols
    global correct

    for r in range(rows):
        for c in range(cols):
            x = c * 75 + 12 + 25
            y = r * 65 + 112 + 25
            button_rect = pygame.Rect(c * 75 + 12, r * 65 + 112, 50, 50)
            pygame.draw.rect(screen, blue if button_rect.collidepoint(pygame.mouse.get_pos()) else White, button_rect, 0, 4)
            if not correct[r][c]:
                piece_text = small_font.render(f"{spaces[r * cols + c]}", True, gray)
            else:
                piece_text = small_font.render("", True, gray)
            
            text_rect = piece_text.get_rect(center=(x, y))
            screen.blit(piece_text, text_rect.topleft)
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)

def check_guess(first, second):
    global spaces
    global correct
    global score
    global matches
    global lives

    if spaces[first] == spaces[second]:
        row1 = first // cols
        col1 = first % cols
        row2 = second // cols
        col2 = second % cols

        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
        else:
            score += 1
            lives -= 1
            if lives == 0:
                game_over_text = title_font.render("Game Over!", True, blue)
                screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
                pygame.display.flip()
                pygame.time.wait(2000)  # Wait for 2 seconds
                pygame.quit()
                quit()

running = True
while running:
    timer.tick(fps)
    screen.fill(Black)
    if new_board:
        generate_board()
        new_board = False
    draw_background()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(rows * cols):
                button_rect = pygame.Rect(i % cols * 75 + 12, i // cols * 65 + 112, 50, 50)
                if button_rect.collidepoint(event.pos) and not correct[i // cols][i % cols] and not (first_guess and second_guess):
                    if not first_guess:
                        first_guess = True
                        first_guess_num = i
                        print("First guess:", first_guess_num)
                    elif not second_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
                        print("Second guess:", second_guess_num)

    if first_guess and second_guess:
        check_guess(first_guess_num, second_guess_num)
        first_guess = False
        second_guess = False

    if matches == rows * cols // 2:
        if score > high_score:
            high_score = score
        print("Congratulations! You've completed the game!")
        running = False

    pygame.display.flip()

pygame.quit()
