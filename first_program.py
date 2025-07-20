import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [width // 2, height - 2 * player_size]
player_speed = 10

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
enemy_speed = 10

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("monospace", 35)

def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed

    screen.fill(black)

    # Enemy movement
    if enemy_pos[1] >= 0 and enemy_pos[1] < height:
        enemy_pos[1] += enemy_speed
    else:
        enemy_pos[0] = random.randint(0, width - enemy_size)
        enemy_pos[1] = 0
        score += 1

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))

    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))

    pygame.display.update()

    clock.tick(30)

pygame.quit()
