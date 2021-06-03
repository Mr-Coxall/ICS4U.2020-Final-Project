import pygame
import sys

MAX_WIDTH = 1200
MAX_HEIGHT = 800
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (219, 20, 20)
GREY = (100, 100, 100)

def main():
    pygame.init()
    pygame.display.set_caption('Virus Simulator')
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    while True:
        screen.fill(GREY)

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.circle(screen, RED, [600, 400], 10)

        # font = pygame.font.SysFont('notosanscjkkrblack', 50)
        # text = font.render("Hello, World!", True, WHITE)
        # screen.blit(text, (5, 10))
        pygame.display.update()
        fps.tick(FPS)

if __name__=="__main__":
    main()
