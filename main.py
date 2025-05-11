import pygame
import random

pygame.init()

#музика
pygame.mixer.init()
pygame.mixer.music.load('my song.mp3')
# Розмір екрану 1
WIDTH, HEIGHT = 1080, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy Bird")

# Константа для кольорів першого вікна
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0,)
HOVER_BLUE = (100, 160, 210)

# Шрифти
title_font = pygame.font.SysFont(name="Arial", size=60)
desc_font = pygame.font.SysFont(name="Arial", size=30)
button_font = pygame.font.SysFont(name="Arial", size=36)

button_text = button_font.render("Почати гру", True, WHITE)
button_width, button_height = 250, 60
button_x = WIDTH // 2 - button_width // 2
button_y = 400
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

#тексти
title_text = title_font.render('flappy Bird', True, WHITE)
desc_text = desc_font.render('Натискай пробіл і уникай труб', True, WHITE ) 

# Початковий екран
first_screen = True
while first_screen:
    screen.fill(BLACK)

    # Показуємо назву та опис
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
    screen.blit(desc_text, (WIDTH // 2 - desc_text.get_width() // 2, 250))

    # Перевірка наведення миші
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, HOVER_BLUE, button_rect)
    else:
        pygame.draw.rect(screen, BLUE, button_rect)

    # Показуємо кнопку
    screen.blit(button_text, (
        button_x + (button_width - button_text.get_width()) // 2,
        button_y + (button_height - button_text.get_height()) // 2
    ))

    pygame.display.flip()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                first_screen = False

# Розмір екрану 2
width, height = 1080, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

background_image = pygame.transform.scale(pygame.image.load('sky.png'), (WIDTH, HEIGHT))
bird_image = pygame.transform.scale(pygame.image.load("bird_image.png"), (100, 100))

# Константа для кольорів другого вікна 
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

running1 = True
pygame.mixer.music.play()
while running1:


    if score > 5 :
        running1 = False

    screen.blit(background_image, dest=(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running1 = False

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
        running1 = False

    if bird_y > height or bird_y < 0:
        running1 = False

    # Малювання пташки
    screen.blit(bird_image, (bird_x, int(bird_y)))

    # Малювання труб 
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, height))

    # Рахунок
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
 
