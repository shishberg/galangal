import pygame

# Screen size
SCREEN_SIZE = (900, 500)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (63, 127, 255)

FPS = 60

def draw_window():
    WIN.fill(BLUE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()
