import pygame
import os

# Screen size
SCREEN_SIZE = (900, 500)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (15, 31, 63)

FPS = 60

KEY_LEFT = False
KEY_RIGHT = False

class Player(object):
    def __init__(self):
        self.image = pygame.image.load("Assets/plate.png")
        self.width = self.image.get_width()
        self.x = 450
        self.y = 400
        self.speed = 5

    def update(self):
        global KEY_LEFT, KEY_RIGHT
        if KEY_LEFT:
            self.x -= self.speed
        if KEY_RIGHT:
            self.x += self.speed
        self.x = max(0, min(SCREEN_SIZE[0] - self.width, self.x))

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load("Assets/potato.png")
        self.width = self.image.get_width()
        self.x = 450
        self.y = 50
        self.x_accel = 0
        self.x_vel = 10
        self.y_accel = 0
        self.y_vel = 2

    def update(self):
        if self.x < SCREEN_SIZE[0]/2:
            self.x_accel = 0.15
        else:
            self.x_accel = -0.15
        self.x_vel += self.x_accel
        self.x += self.x_vel

        if self.y < SCREEN_SIZE[1]/5:
            self.y_accel = 0.3
        else:
            self.y_accel = -0.3
        self.y_vel += self.y_accel
        self.y += self.y_vel

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


PLAYER = Player()
ENEMY = Enemy()

def draw_window():
    WIN.fill(BLUE)
    PLAYER.draw(WIN)
    ENEMY.draw(WIN)
    pygame.display.update()

def handle_key_down(key):
    global KEY_LEFT, KEY_RIGHT
    if key == pygame.K_LEFT:
        KEY_LEFT = True
    elif key == pygame.K_RIGHT:
        KEY_RIGHT = True

def handle_key_up(key):
    global KEY_LEFT, KEY_RIGHT
    if key == pygame.K_LEFT:
        KEY_LEFT = False
    elif key == pygame.K_RIGHT:
        KEY_RIGHT = False

def physics():
    PLAYER.update()
    ENEMY.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            print(event)
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
