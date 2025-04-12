import pygame

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("flappy Bird")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))

    pygame.display.update()

pygame.quit()