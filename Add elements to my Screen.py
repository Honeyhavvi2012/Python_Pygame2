import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen with Rectangle and Text")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))  

    text = font.render("Hello, Gamer!", True, BLACK)
    screen.blit(text, (300, 150))  

    pygame.display.flip()

pygame.quit()
sys.exit()