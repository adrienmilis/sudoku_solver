import pygame


class Button:

    BUTTON_WIDTH = 48

    def __init__(self, pos, number='', bg=pygame.Color("White"), coordinates=()):
        # position in the grid
        self.coord = coordinates
        # position on the screen
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", 38)
        # this Rect is used to check for collisions (hitbox)
        self.rect = pygame.Rect(self.x, self.y, self.BUTTON_WIDTH, self.BUTTON_WIDTH)
        self.surface = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_WIDTH))
        self.surface.fill(bg)
        self.change_text(number, bg)

    def change_text(self, number, bg=pygame.Color("White")):
        if (number == '0'):
            number = ''
        self.text = self.font.render(number, 1, pygame.Color("Black"))
        pygame.draw.rect(self.surface, bg, pygame.Rect(2, 2, self.BUTTON_WIDTH - 4, self.BUTTON_WIDTH - 4))
        self.surface.blit(self.text, (12,2))

    def show(self, screen, update=True, border_color=None):
        screen.blit(self.surface, (self.x, self.y))
        if update == True:
            if border_color is not None:
                self.draw_borders(screen, border_color, show=False)
            pygame.display.update(self.rect)
        else:
            self.draw_borders(screen, pygame.Color("Green"), show=False)

    def draw_borders(self, screen, color, show=True):
        rectangles = []
        rectangles.append(pygame.Rect(0, 0, 2, self.BUTTON_WIDTH))  # left border
        rectangles.append(pygame.Rect(0, 0, self.BUTTON_WIDTH, 2))  # upper border
        rectangles.append(pygame.Rect(self.BUTTON_WIDTH - 2, 0, 2, self.BUTTON_WIDTH)) # right border
        rectangles.append(pygame.Rect(0, self.BUTTON_WIDTH - 2, self.BUTTON_WIDTH, 2)) # lower border
        for rect in rectangles:
            pygame.draw.rect(self.surface, color, rect)
        if show:
            self.show(screen)

    def check_click(self, screen):
        # left click
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.draw_borders(screen, pygame.Color("Orange"))
                return True
