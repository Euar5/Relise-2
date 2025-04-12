import pygame
import random

pygame.init()

# Екрану
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (50, 150, 255)

# Пташка
bird_x = 100
bird_y = 300
bird_radius = 20
gravity = 0.5
bird_velocity = 0
jump_strength = -10

# Труби
pipe_width = 80
pipe_gap = 200
pipe_x = width
pipe_height = random.randint(100, 400)
pipe_speed = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

score = 0

running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Стрибок пташки
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = jump_strength

    # Рух пташки
    bird_velocity += gravity
    bird_y += bird_velocity

    # Труби
    pipe_x -= pipe_speed
    if pipe_x + pipe_width < 0:
        pipe_x = width
        pipe_height = random.randint(100, 400)
        score += 1

    # Колізія
    if (pipe_x < bird_x < pipe_x + pipe_width) and not (pipe_height < bird_y < pipe_height + pipe_gap):
        running = False

    if bird_y > height or bird_y < 0:
        running = False

    # Малювання пташки
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Малювання труб
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, height))

    # Рахунок
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
