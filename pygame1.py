import pygame
import sys
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((600, 300))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test")

def main():
    while True:
        # 배경색 설정
        Surface.fill((50,150,70))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        '''
        # 모눈
        for x in range(10, 600, 10) :
            pygame.draw.line(Surface, (60, 170, 100), (x, 0), (x, 600))
        for y in range(10, 600, 10) :
            pygame.draw.line(Surface, (60, 170, 100), (0, y), (600, y))

        # 3x3 격자
        for x in range(100, 500, 100):
            pygame.draw.line(Surface, (255, 255, 255), (x, 100), (x, 400), 10)
        for y in range(100, 500, 100):
            pygame.draw.line(Surface, (255, 255, 255), (100, y), (400, y), 10)
        

        # 검정 가로선
        pygame.draw.line(Surface, (0,0,0), (50, 10), (400, 10))

        # 하얀 가로선
        pygame.draw.line(Surface, (255, 255, 255), (50, 50), (400, 50), 5)
        '''
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()