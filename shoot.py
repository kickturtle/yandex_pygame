import pygame

def shoot():
    start_point = [20, 300]
    while moving:
        if hit_object:
            break
        else:
            pygame.draw.rect(screen, 'red', rect=((start_point[0],start_point[1]), (start_point[0]+5,start_point[1]+25)))
            start_point[0] += clock.tick(100)
if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                moving = True
                hit_object = False
                shoot()
    pygame.quit()