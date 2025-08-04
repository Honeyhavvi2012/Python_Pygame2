import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game with Background and Sound")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  

font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to My Game!", True, (255, 255, 255))

clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0, 0)) 

    pygame.draw.rect(screen, (0, 128, 255), (300, 250, 200, 100))

    screen.blit(text, (220, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
