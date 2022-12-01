import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_SPACE
import random

pygame.init()
pygame.display.set_caption("SHOOTING GAME")

Surface = pygame.display.set_mode((600, 500))
FPSCLOCK = pygame.time.Clock()

rect_area = (50, 150, 500, 300)

BigFont = pygame.font.SysFont("Consolas", 40)
SmallFont = pygame.font.SysFont("Verdana", 20)

def main():
    obstacle = False
    Score = 0
    Miss = 0

    textScore = "Score : " + str(Score)
    textMiss = "Miss : " + str(Miss)

    msgTitle = BigFont.render("SHOOTING GAME", True, (255, 255, 255))
    msgSubtitle = SmallFont.render("Missile Button : A (Missile is only one)", True, (255, 255, 255))
    msgScore = SmallFont.render(textScore, True, (255, 255, 255))
    msgMiss = SmallFont.render(textMiss, True, (255, 255, 255))

    while True :
        Surface.fill((30,100,40))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 장애물 영역
        pygame.draw.rect(Surface, (255, 255, 255), rect_area, 2)

        Surface.blit(msgTitle, (150, 30))
        Surface.blit(msgSubtitle, (110, 70))
        Surface.blit(msgScore, (170, 100))
        Surface.blit(msgMiss, (330, 100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__" :
    main()