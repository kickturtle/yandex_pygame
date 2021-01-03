import pygame


class Landing(pygame.sprite.Sprite):
    image_land = pygame.image.load('data/pt.png')

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Landing.image_land
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)
        else:
            self.image = pygame.image.load('data/pix_mando_160.png')


class Mountain(pygame.sprite.Sprite):
    image_mount = pygame.image.load('data/mountains.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Mountain.image_mount
        self.rect = self.image.get_rect()
        self.rect.bottom = height
        self.mask = pygame.mask.from_surface(self.image)


pygame.init()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Шарики")
# создаём группы спрайтов
all_sprites = pygame.sprite.Group() # для всех спрайтов
all_lands = pygame.sprite.Group() # для движения парашютов
mountain = Mountain(all_sprites)

clock = pygame.time.Clock()
FPS = 30
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            Landing(x, y, all_sprites, all_lands)
    all_lands.update()
    screen.fill('grey')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
