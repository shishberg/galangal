import pygame

# Screen size
SCREEN_SIZE = (900, 500)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("=== Galangal ===")

BLUE = (63, 127, 255)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False

        WIN.fill(BLUE)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
