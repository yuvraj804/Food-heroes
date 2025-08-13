

def Fight():
    import pygame
    from buttonlogic import draw_button
    from superhero_class import superhero
    from core import create_default_heroes
    from main import main
    from csv_io import load_heroes_from_csv, register_fight_hero
    from tg import draw_wrapped_text
    import os
    from play import playw
    from versus import Versus

    pygame.init()

    load_heroes_from_csv()
    if not superhero.instances:
        print("[DEBUG] No heroes found in CSV, loading default heroes.")
        create_default_heroes()

    i = 0
    hero = superhero.instances[i]

    w, h = 768, 512
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Food Heroes")

    back_img = pygame.image.load('background/neon_blue_and_white_background.jpeg')


    def load_hero(index):
        h = superhero.instances[index]
        try:
            img = pygame.image.load(h.location)
        except:
            img = pygame.image.load("Heroes/unknown.jpeg")
        hero_img = pygame.transform.scale(img, (200, 300))
        rectimg = hero_img.get_rect(center=(384, 250))
        return h, hero_img, rectimg

    hero, hero_img, rectimg = load_hero(i)


    back_btn_img = pygame.image.load('buttons/back.png')
    back_btn_scaled = pygame.transform.scale(back_btn_img, (217, 100))
    rectback = back_btn_scaled.get_rect(center=(100, 100))

    right_btn_img = pygame.image.load('buttons/right.png')
    right_btn_scaled = pygame.transform.scale(right_btn_img, (100, 100))
    rectright = right_btn_scaled.get_rect(center=(650, 256))

    left_btn_img = pygame.image.load('buttons/left.png')
    left_btn_scaled = pygame.transform.scale(left_btn_img, (100, 100))
    rectleft = left_btn_scaled.get_rect(center=(118, 256))

    fight = pygame.image.load('buttons/fight.png')
    fight_scaled = pygame.transform.scale(fight, (256, 100))
    fight_rect = fight_scaled.get_rect(center=(668, 100))

    Phrase = pygame.font.Font("font/Oswald-VariableFont_wght.ttf", 28)
    nametitle = pygame.font.Font("font/SuperShiny-0v0rG.ttf", 45)
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if rectback.collidepoint(pygame.mouse.get_pos()):
                    superhero.instances.clear()
                    open("fight_heroes.csv", "w").close()

                    run = False
                    playw()

                elif rectright.collidepoint(pygame.mouse.get_pos()):
                    i = (i + 1) % len(superhero.instances)
                    hero, hero_img, rectimg = load_hero(i)
                elif rectleft.collidepoint(pygame.mouse.get_pos()):
                    i = (i - 1) % len(superhero.instances)
                    hero, hero_img, rectimg = load_hero(i)
                elif fight_rect.collidepoint(pygame.mouse.get_pos()):
                    register_fight_hero(superhero.instances[i])
                    Versus()
                    run=False



        screen.blit(back_img, (0, 0))

        border_color = (0, 0, 50)
        border_thickness = 4
        border_rect = rectimg.inflate(border_thickness * 2, border_thickness * 2)
        pygame.draw.rect(screen, border_color, border_rect, border_radius=10)


        screen.blit(hero_img, rectimg)


        catchphrase_surface = Phrase.render(hero.catchphrase, True, "blue")
        text_width, text_height = catchphrase_surface.get_size()


        padding_x = 20
        padding_y = 10
        rect_x = 384 - (text_width + padding_x) // 2
        rect_y = 420
        rect_width = text_width + padding_x
        rect_height = text_height + padding_y


        pygame.draw.rect(screen, "lightblue", pygame.Rect(rect_x, rect_y, rect_width, rect_height), border_radius=10)


        screen.blit(catchphrase_surface, (rect_x + padding_x // 2, rect_y + padding_y // 2))

        name_surface = nametitle.render(hero.name, True, "white")
        name_width, name_height = name_surface.get_size()

        name_padding_x = 40
        name_padding_y = 20
        name_x = (w - name_width - name_padding_x) // 2
        name_y = 20
        name_rect = pygame.Rect(name_x, name_y, name_width + name_padding_x, name_height + name_padding_y)

        pygame.draw.rect(screen, "darkblue", name_rect, border_radius=12)
        screen.blit(name_surface, (name_x + name_padding_x // 2, name_y + name_padding_y // 2))

        screen.blit(back_btn_scaled, rectback)


        mouse_pos = pygame.mouse.get_pos()
        draw_button(screen, back_btn_scaled, rectback.center, rectback.collidepoint(mouse_pos))
        draw_button(screen, right_btn_scaled, rectright.center, rectright.collidepoint(mouse_pos))
        draw_button(screen, left_btn_scaled, rectleft.center, rectleft.collidepoint(mouse_pos))
        draw_button(screen,fight_scaled, fight_rect.center, fight_rect.collidepoint(mouse_pos))

        pygame.display.update()
        clock.tick(60)
