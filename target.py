import pygame


def change_color(col):
    if col == 'red':
        col = 'blue'
    elif col == 'blue':
        col = 'green'
    else:
        col = 'red'
    return col


def find_outer_color(n):
    if n % 3 == 0:
        out_col = 'blue'
    elif n % 3 == 2:
        out_col = 'green'
    else:
        out_col = 'red'
    return out_col


def draw_target(surf, wid, num):
    color = find_outer_color(num)
    rad = wid * num
    for layer in range(num):
        pygame.draw.circle(surf, color, (wid * num, wid * num), rad, width=0)
        rad -= wid
        color = change_color(color)


if __name__ == '__main__':
    pygame.init()
    try:
        w, n = tuple(input().split())
        w, n = int(w), int(n)
        size = 2 * n * w, 2 * n * w
        screen = pygame.display.set_mode(size)

        draw_target(screen, w, n)

        pygame.display.set_caption('Мишень')
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except:
        print('Неправильный формат ввода')
