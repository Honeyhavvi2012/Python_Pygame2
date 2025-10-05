import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Easy Sprite Colour Change")

WHITE = (255, 255, 255)

CHANGE_COLOR = pygame.USEREVENT + 1

sprite1 = pygame.Rect(150, 150, 60, 60)
sprite2 = pygame.Rect(300, 150, 60, 60)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR))

        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill(WHITE)
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.flip()

pygame.quit()
