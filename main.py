import pygame
import os

# Screen size
SCREEN_SIZE = (900, 500)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (63, 127, 255)

FPS = 60

PLAYER_IMAGE = pygame.image.load("Assets/plate.png")
PLAYER_WIDTH = PLAYER_IMAGE.get_width()
PLAYER_X = 450
PLAYER_LEFT = False
PLAYER_RIGHT = False
PLAYER_SPEED = 5

def draw_window():
    WIN.fill(BLUE)
    WIN.blit(PLAYER_IMAGE, (PLAYER_X, 400))
    pygame.display.update()

def handle_key_down(key):
    global PLAYER_LEFT, PLAYER_RIGHT
    if key == pygame.K_LEFT:
        PLAYER_LEFT = True
    elif key == pygame.K_RIGHT:
        PLAYER_RIGHT = True

def handle_key_up(key):
    global PLAYER_LEFT, PLAYER_RIGHT
    if key == pygame.K_LEFT:
        PLAYER_LEFT = False
    elif key == pygame.K_RIGHT:
        PLAYER_RIGHT = False

def physics():
    global PLAYER_X, PLAYER_LEFT, PLAYER_RIGHT
    if PLAYER_LEFT:
        PLAYER_X -= PLAYER_SPEED
    if PLAYER_RIGHT:
        PLAYER_X += PLAYER_SPEED
    PLAYER_X = max(0, min(900 - PLAYER_WIDTH, PLAYER_X))

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
