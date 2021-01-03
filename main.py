import pygame

width, height = tuple(input().split())
width, height = int(width), int(height)
pygame.init()
size = width, height
screen = pygame.display.set_mode(size)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False