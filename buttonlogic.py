import pygame


def draw_button(display, image, pos, hover, scale=1.2):

    if hover:
        new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
        scaled_img = pygame.transform.scale(image, new_size)
        rect = scaled_img.get_rect(center=pos)
    else:
        scaled_img = image
        rect = image.get_rect(center=pos)

    display.blit(scaled_img, rect)
    return rect