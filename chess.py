import pygame


def change_color(col):
    if col == 'black':
        col = 'white'
    else:
        col = 'black'
    return col


def draw_desk(screen, sid, cell):
    screen.fill((0, 0, 0))
    len_cell = sid // cell
    color = 'black'
    for cell_y in range(0, sid, len_cell):
        for cell_x in range(0, sid, len_cell):
            pygame.draw.rect(screen, color, ((cell_x, cell_y), (cell_x + len_cell, cell_y + len_cell)))
            color = change_color(color)
        color = change_color(color)


if __name__ == '__main__':
    pygame.init()
    '''try:'''
    side, cells = tuple(input().split())
    side, cells = int(side), int(cells)
    size = side, side
    screen = pygame.display.set_mode(size)

    draw_desk(screen, side, cells)
    pygame.display.set_caption('Шахматная клетка')
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    '''except:
        print('Неправильный фоомат ввода')'''