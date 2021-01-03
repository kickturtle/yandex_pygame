import pygame


def draw_redrect(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'red', rect=((1, 1), (width - 2, height - 2)))


if __name__ == '__main__':
    pygame.init()
    try:
        size_check = tuple(input().split())
        width, height = int(size_check[0]), int(size_check[1])
        size = width, height
        screen = pygame.display.set_mode(size)

        draw_redrect(screen)

        pygame.display.set_caption('Прямоугольник')
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except:
        print('Неправильный формат ввода')