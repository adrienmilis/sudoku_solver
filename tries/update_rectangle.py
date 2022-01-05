import pygame

# this example shows how to only update certain parts of the screen
# thanks to rectangles.
# This is useful for performance 

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color("White"))
pygame.display.update()
rect1 = pygame.Rect(0, 0, 200, 200)
rect2 = pygame.Rect(450, 450, 50, 50)
pygame.draw.rect(screen, pygame.Color("Black"), rect1)
pygame.draw.rect(screen, pygame.Color("Orange"), rect2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.update(rect2)
            if event.key == pygame.K_RETURN:
                pygame.display.update(rect1)

pygame.quit()
