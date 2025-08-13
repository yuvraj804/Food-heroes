import pygame


class InputBox:
    def __init__(self, x, y, w, h, label,text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('green')
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.label = label
        self.text = text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return 'next'  # Let the main loop know to switch fields
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):

        label_surf = self.font.render(self.label, True, (255, 255, 255))
        screen.blit(label_surf, (self.rect.x - 120, self.rect.y + 5))


        pygame.draw.rect(screen, "white", self.rect)


        pygame.draw.rect(screen, self.color, self.rect, 2)


        txt_surface = self.font.render(self.text, True, (0, 0, 0))  # black text for contrast
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_value(self):
        return self.text
