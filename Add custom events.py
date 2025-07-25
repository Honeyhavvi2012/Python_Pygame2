import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Two Circles")
window.fill((255, 255, 255))

GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)      # Solid circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)   # Outline circle

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
