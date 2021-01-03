import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, rad, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((2 * rad, 2 * rad), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, 'red', (rad, rad), rad)
        self.rect = pygame.Rect(x, y, 2 * rad, 2 * rad)
        self.vx = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.vy = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    def reverse(self):
        self.vx = -self.vx
        self.vy = -self.vy

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, vertical_bord):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, horizontal_bord):
            self.vy = -self.vy
        balls_collided = pygame.sprite.spritecollide(self, balls, False)
        for ball in balls_collided:
            if ball is not self:
                ball.reverse()


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

for _ in range(30):
    Ball(random.randint(100, width - 100),
         random.randint(100, width - 100),
         random.randint(10, 20), all_sprites, balls)
# создаём границы
Border(0, 0, width, 5, all_sprites, horizontal_bord)
Border(0, height - 5, width, 5, all_sprites, horizontal_bord)

Border(0, 0, 5, height, all_sprites, vertical_bord)
Border(width - 5, 0, 5, height, all_sprites, vertical_bord)

clock = pygame.time.Clock()
FPS = 30
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    balls.update()
    screen.fill('white')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
