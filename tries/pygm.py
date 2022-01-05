import pygame

from pygame.locals import (
     K_1,
     K_2,
     K_3,
     K_4,
     K_5,
     K_6,
     K_7,
     K_8,
     K_9,
     K_ESCAPE,
     QUIT
)

SCREEN_WIDTH = 500
SCREEN_HEIGTH = 500
WHITE = (255,255,255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])

screen.fill(WHITE)
# rect = pygame.Rect(50, 50, 0.8 * SCREEN_WIDTH, 0.8 * SCREEN_HEIGTH)
# pygame.draw.rect(screen, BLACK, rect, 2, 10)

running = True

# main game loop
while running:

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

     
     # Flip the display
     pygame.display.flip()

pygame.quit()