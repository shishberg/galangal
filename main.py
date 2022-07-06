import pygame
import os
import random

# Screen size
SCREEN_SIZE = (500, 900)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (15, 31, 63)

FPS = 60

KEY_LEFT = False
KEY_RIGHT = False

class GameObject(object):
    def __init__(self, x, y, image_filename, x_vel=0, y_vel=0):
        self.image = pygame.image.load(os.path.join("Assets", image_filename))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.x_accel = 0
        self.x_vel = x_vel
        self.y_accel = 0
        self.y_vel = y_vel

    def update(self):
        self.x_vel += self.x_accel
        self.x += self.x_vel
        self.y_vel += self.y_accel
        self.y += self.y_vel

    def draw(self, win):
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))


class Bullet(GameObject):
    def __init__(self, player, x, y, y_vel):
        GameObject.__init__(self, x, y, "fork.png", y_vel=-10)


class Player(GameObject):
    def __init__(self):
        GameObject.__init__(self, SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-100, "plate.png")
        self.speed = 5
        self.projectiles = []
    
    def fire(self):
        bullet = Bullet(self, self.x, self.y-30, 10)
        self.projectiles.append(bullet)

    def update(self):
        global KEY_LEFT, KEY_RIGHT
        if KEY_LEFT:
            self.x -= self.speed
        if KEY_RIGHT:
            self.x += self.speed
        self.x = max(50, min(SCREEN_SIZE[0] - 50, self.x))

        for projectile in self.projectiles:
            projectile.update()
        self.projectiles = [p for p in self.projectiles if p.y > -10]

    
    def draw(self, win):
        GameObject.draw(self, win)
        for projectile in self.projectiles:
            projectile.draw(win)


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, "potato.png")

    def update(self):
        if self.x < SCREEN_SIZE[0]/2:
            self.x_accel = 0.15
        else:
            self.x_accel = -0.15

        if self.y < SCREEN_SIZE[1]/3:
            self.y_accel = 0.3
        else:
            self.y_accel = -0.3

        GameObject.update(self)


PLAYER = Player()
ENEMIES = [Enemy(random.randint(50, SCREEN_SIZE[0]-50), random.randint(50, SCREEN_SIZE[1]*2//3))
           for _ in range(20)]


def draw_window():
    WIN.fill(BLUE)
    PLAYER.draw(WIN)
    for enemy in ENEMIES:
        enemy.draw(WIN)
    pygame.display.update()

def handle_key_down(key):
    global KEY_LEFT, KEY_RIGHT
    if key == pygame.K_LEFT or key == pygame.K_a:
        KEY_LEFT = True
    elif key == pygame.K_RIGHT or key == pygame.K_d:
        KEY_RIGHT = True

def handle_key_up(key):
    global KEY_LEFT, KEY_RIGHT
    if key == pygame.K_LEFT or key == pygame.K_a:
        KEY_LEFT = False
    elif key == pygame.K_RIGHT or key == pygame.K_d:
        KEY_RIGHT = False
    elif key == pygame.K_SPACE:
        PLAYER.fire()

def physics():
    PLAYER.update()
    for enemy in ENEMIES:
        enemy.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_down(event.key)
            elif event.type == pygame.KEYUP:
                handle_key_up(event.key)

        physics()
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()
