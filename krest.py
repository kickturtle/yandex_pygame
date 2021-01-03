import pygame

def draw_x(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), size, 5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)

if __name__ == '__main__':
    pygame.init()
    try:
        size_check = tuple(input().split())
        width, height = int(size_check[0]), int(size_check[1])
        size = width, height
        screen = pygame.display.set_mode(size)

        draw_x(screen)

        pygame.display.set_caption('Крест')
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except:
        print('Неправильный формат ввода')