import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((10, 10))
        pygame.draw.circle(self.image, 'red', (200, 120), 10)
        self.rect = pygame.Rect(190, 110, 20, 20)
        self.speed = 5

    def update(self, *args):
        self.rect = self.rect.move(self.speed, 0)


class Mandalorian(pygame.sprite.Sprite):
    image_mando = pygame.image.load('data/pix_mando_shootstart.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Mandalorian.image_mando
        self.rect = self.image.get_rect()
        self.rect.bottom = height
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
size = width, height = 500, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Тест выстрелов")

all_sprites = pygame.sprite.Group() # для всех спрайтов
bullet = pygame.sprite.Group() # для движения пули
mandalorian = Mandalorian(all_sprites)

clock = pygame.time.Clock()
FPS = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shot = Bullet(bullet)
    bullet.update()
    screen.fill('white')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
