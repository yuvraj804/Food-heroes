def show_popup(screen, message, duration=2000):
    import pygame
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)
    popup_surface = pygame.Surface((500, 120))
    popup_surface.fill((30, 30, 30))  # dark background
    pygame.draw.rect(popup_surface, (0, 180, 255), popup_surface.get_rect(), 4)

    text = font.render(message, True, (255, 255, 255))
    popup_surface.blit(text, (popup_surface.get_width() // 2 - text.get_width() // 2, 40))


    screen.blit(popup_surface, (
        screen.get_width() // 2 - popup_surface.get_width() // 2,
        screen.get_height() // 2 - popup_surface.get_height() // 2)
    )
    pygame.display.update()
    pygame.time.delay(duration)