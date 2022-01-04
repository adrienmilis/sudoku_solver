import pygame

from pygame.locals import (
    K_0,
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

BUTTON_WIDTH = 48

class Button:

    def __init__(self, pos):
        # position on the screen
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", 38)
        # this Rect is used to check for collisions (hitbox)
        self.rect = pygame.Rect(self.x, self.y, BUTTON_WIDTH, BUTTON_WIDTH)
        self.surface = pygame.Surface((BUTTON_WIDTH, BUTTON_WIDTH))
        self.surface.fill(pygame.Color("White"))
        self.change_text()

    def change_text(self, text=""):
        self.text = self.font.render(text, 1, pygame.Color("Black"))
        pygame.draw.rect(self.surface, pygame.Color("White"), pygame.Rect(2, 2, BUTTON_WIDTH - 4, BUTTON_WIDTH - 4))
        self.surface.blit(self.text, (12,2))

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def draw_borders(self, screen, color):
        rectangles = []
        rectangles.append(pygame.Rect(0, 0, 2, BUTTON_WIDTH))  # left border
        rectangles.append(pygame.Rect(0, 0, BUTTON_WIDTH, 2))  # upper border
        rectangles.append(pygame.Rect(BUTTON_WIDTH - 2, 0, 2, BUTTON_WIDTH)) # right border
        rectangles.append(pygame.Rect(0, BUTTON_WIDTH - 2, BUTTON_WIDTH, 2)) # lower border
        for rect in rectangles:
            pygame.draw.rect(self.surface, color, rect)
        self.show(screen)

    def check_click(self, screen):
        # left click
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.draw_borders(screen, pygame.Color("Black"))
                return True

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill(pygame.Color("White"))
    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(25, 25, 454, 454), border_radius=3)
    pygame.display.flip()

    keys_possible = {K_0: '', K_1: '1', K_2: '2', K_3: '3', K_4: '4', K_5: '5',
                K_6: '6', K_7: '7', K_8: '8', K_9: '9'}
    
    buttons = []
    x = 27
    for i in range(9):
        y = 27
        for j in range(9):
            buttons.append( Button((x, y)) )
            y += 50
        x += 50

    for button in buttons:
        button.show(screen)

    button1 = Button((50, 50))
    running = True
    current_button = None

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.check_click(screen) == True:
                        print(f'current button coordinates: {button.x} {button.y}')
                        if (current_button is not None):
                            current_button.draw_borders(screen, pygame.Color("White"))
                        current_button = button
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key in keys_possible.keys() and current_button is not None:
                    current_button.change_text(keys_possible[event.key])
                    print('text changed')
                    current_button.show(screen)
        pygame.display.flip()
            
    pygame.quit()
if __name__ == '__main__':
    main()