import pygame
import sys

pygame.init()

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

background_color = (58, 58, 58)

image = pygame.image.load("image.png")  
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect()
image_rect.center = (window_size[0] // 2, window_size[1] // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
