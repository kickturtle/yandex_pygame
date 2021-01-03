import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, rad, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((2 * rad, 2 * rad), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, 'white', (rad, rad), rad)
        self.rect = pygame.Rect(x, y, 2 * rad, 2 * rad)
        self.vx = -1
        self.vy = -1

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, vertical_bord):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, horizontal_bord):
            self.vy = -self.vy


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((width, height))
        self.image.fill('black')
        self.rect = pygame.Rect(x, y, width, height)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Шарики")
# создаём группы спрайтов
all_sprites = pygame.sprite.Group() # для всех спрайтов
balls = pygame.sprite.Group() # для движения шариков
vertical_bord = pygame.sprite.Group()
horizontal_bord = pygame.sprite.Group()

# создаём границы
Border(0, 0, width, 1, all_sprites, horizontal_bord)
Border(0, height - 1, width, 1, all_sprites, horizontal_bord)

Border(0, 0, 1, height, all_sprites, vertical_bord)
Border(width - 1, 0, 1, height, all_sprites, vertical_bord)

clock = pygame.time.Clock()
FPS = 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Ball(event.pos[0],
                 event.pos[1],
                 10, all_sprites, balls)
    balls.update()
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()