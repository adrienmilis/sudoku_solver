import pygame

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
