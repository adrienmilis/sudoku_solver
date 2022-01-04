import pygame

# class clickable_rect:


pygame.init()
pygame.mouse.set_visible(1)

screen = pygame.display.set_mode((500, 500))
# button = pygame.Rect(50, 50, 50, 50)
# screen.blit(button, (0, 0))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pressed()[2])
    

    pygame.display.flip()
    