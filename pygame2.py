import pygame
import sys
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

WIDTH = 1000
HEIGHT = 300

pygame.init()
pygame.display.set_caption("TEST 2")
Surface = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

def main() :
    xpos = 0
    ypos = 0

    keyCheck = False

    while True:
        # myfont = pygame.font.SysFont("C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/neodgm.ttf", 30)
        myfont = pygame.font.SysFont("JOKERMAN", 30)
        message1 = myfont.render("GAME OVER", True, (255,255,255))

        Surface.fill((30, 100, 50))
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN :
                if event.key == K_LEFT :
                    xpos -= 10
                elif event.key == K_RIGHT :
                    xpos += 10
                elif event.key == K_DOWN :
                    ypos += 10
                elif event.key == K_UP :
                    ypos -= 10

        # rect 는 좌표 튜플
        pygame.draw.rect(Surface, (0, 230, 130), (300, 40, 350, 90), 4)
        pygame.draw.polygon(Surface, (255, 255, 255), [(xpos,ypos), (300, 300), (140, 30)])

        image = pygame.image.load("D:/Desktop/pythonlogo.jpg")

        Surface.blit(message1, (500, 30))
        Surface.blit(image, (600, 200), Rect(50, 20, 80, 80))
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()