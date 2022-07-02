import pygame
import os

# Screen size
SCREEN_SIZE = (900, 500)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (63, 127, 255)

FPS = 60

PLATE_IMAGE = pygame.image.load("Assets/plate.png")
PLATE_WIDTH = PLATE_IMAGE.get_width()
PLATE_X = 450
PLATE_LEFT = False
PLATE_RIGHT = False
PLATE_SPEED = 5

def draw_window():
    WIN.fill(BLUE)
    WIN.blit(PLATE_IMAGE, (PLATE_X, 400))
    pygame.display.update()

def handle_key_down(key):
    global PLATE_LEFT, PLATE_RIGHT
    if key == pygame.K_LEFT:
        PLATE_LEFT = True
    elif key == pygame.K_RIGHT:
        PLATE_RIGHT = True

def handle_key_up(key):
    global PLATE_LEFT, PLATE_RIGHT
    if key == pygame.K_LEFT:
        PLATE_LEFT = False
    elif key == pygame.K_RIGHT:
        PLATE_RIGHT = False

def physics():
    global PLATE_X, PLATE_LEFT, PLATE_RIGHT
    if PLATE_LEFT:
        PLATE_X -= PLATE_SPEED
    if PLATE_RIGHT:
        PLATE_X += PLATE_SPEED
    PLATE_X = max(0, min(900 - PLATE_WIDTH, PLATE_X))

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
