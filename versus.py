i=0
j=0
def Versus():
    import pygame
    from csv_io import load_fight_heroes
    from sys import exit
    import os
    import random
    from buttonlogic import draw_button
    from main import main



    hero1 = load_fight_heroes(0)
    hero2 = load_fight_heroes(1)


    loc1 = os.path.join("Heroes", (hero1.name + ".jpeg").lower().replace(' ', ''))
    loc2 = os.path.join("Heroes", (hero2.name + ".jpeg").lower().replace(' ', ''))

    pygame.init()

    w, h = 768, 512
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("VERSUS")
    pygame.display.set_caption("Food Heroes")

    clock = pygame.time.Clock()


    backg = pygame.image.load("background/neon_blue_and_white_background (1).jpeg")


    def load_img(loc, name):
        try:
            print(f"[DEBUG] Loading image for {name}: {loc}")
            img = pygame.image.load(loc)
        except:
            print(f"[⚠] Failed to load {loc}. Using fallback.")
            img = pygame.image.load("Heroes/unknown.jpeg")
        return pygame.transform.scale(img, (200, 300))

    img1 = load_img(loc1, hero1.name)
    img2 = load_img(loc2, hero2.name)

    rematch= pygame.image.load("buttons/rematch.png")
    menu = pygame.image.load("buttons/menu.png")
    scalerematch= pygame.transform.scale(rematch, (162.75, 75))
    scalemenu= pygame.transform.scale(menu, (162.75, 75))
    rectrematch= scalerematch.get_rect(center=(81.33,470))
    rectmenu= scalemenu.get_rect(center=(686.67,470))


    attribute = random.choice(["strength", "dexterity", "intelligence", "tactic"])
    val1 = getattr(hero1, attribute)
    val2 = getattr(hero2, attribute)


    if val1 > val2:
            result_text = f"{hero1.name} wins!"
            cov1 = "green"
            cov2 = "red"
            global i
            i+=1
    elif val2 > val1:
            result_text = f"{hero2.name} wins!"
            cov1 = "red"
            cov2 = "green"
            global j
            j+=1
    else:
            result_text = "It's a tie!"
            cov1 = cov2 = "white"
            i+=0.5
            j+=0.5



    font = pygame.font.Font("font/Oswald-VariableFont_wght.ttf", 28)
    big_font = pygame.font.Font("font/SuperShiny-0v0rG.ttf", 40)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if rectrematch.collidepoint(pygame.mouse.get_pos()):
                    Versus()
                    running = False
                elif rectmenu.collidepoint(pygame.mouse.get_pos()):
                    i=0
                    j=0
                    main()
                    running = False


        screen.blit(backg, (0, 0))

        hero_size = (200, 300)
        border_thickness = 4



        img1 = pygame.transform.scale(img1, hero_size)
        img2 = pygame.transform.scale(img2, hero_size)

        rectimg1 = img1.get_rect(center=(130, 270))
        rectimg2 = img2.get_rect(center=(598, 270))


        border_rect1 = rectimg1.inflate(border_thickness * 2, border_thickness * 2)
        border_rect2 = rectimg2.inflate(border_thickness * 2, border_thickness * 2)


        pygame.draw.rect(screen, cov1, border_rect1, border_radius=10)
        screen.blit(img1, rectimg1)

        pygame.draw.rect(screen, cov2, border_rect2, border_radius=10)
        screen.blit(img2, rectimg2)

        mouse_pos = pygame.mouse.get_pos()
        draw_button(screen,scalerematch, rectrematch.center, rectrematch.collidepoint(mouse_pos))
        draw_button(screen,scalemenu, rectmenu.center, rectmenu.collidepoint(mouse_pos))


        attr_text = f"ATTRIBUTE: {attribute.upper()}"
        attr_surf = big_font.render(attr_text, True, (0, 0, 0))
        attr_bg_rect = pygame.Rect(0, 0, attr_surf.get_width() + 20, attr_surf.get_height() + 10)
        attr_bg_rect.center = (w // 2, 30)
        pygame.draw.rect(screen, (255, 255, 0), attr_bg_rect, border_radius=10)  # red+green=yellow

        screen.blit(attr_surf, attr_surf.get_rect(center=attr_bg_rect.center))


        text1 = f"{hero1.name} : {val1} ({i})"
        text_surf1 = font.render(text1, True, (0, 0, 0))
        text_bg1 = pygame.Rect(30, 70, text_surf1.get_width() + 20, text_surf1.get_height() + 10)
        pygame.draw.rect(screen, pygame.Color(cov1), text_bg1, border_radius=10)
        screen.blit(text_surf1, text_surf1.get_rect(center=text_bg1.center))


        text2 = f"{hero2.name} : {val2} ({j})"
        text_surf2 = font.render(text2, True, (0, 0, 0))
        text_bg2 = pygame.Rect(470, 70, text_surf2.get_width() + 20, text_surf2.get_height() + 10)
        pygame.draw.rect(screen, pygame.Color(cov2), text_bg2, border_radius=10)
        screen.blit(text_surf2, text_surf2.get_rect(center=text_bg2.center))


        result_surf = big_font.render(result_text, True, (0, 0, 0))
        result_bg_rect = pygame.Rect(0, 0, result_surf.get_width() + 20, result_surf.get_height() + 10)
        result_bg_rect.center = (w // 2, 460)
        pygame.draw.rect(screen, (255, 165, 0), result_bg_rect, border_radius=10)  # Orange background
        screen.blit(result_surf, result_surf.get_rect(center=result_bg_rect.center))
        pygame.display.update()
        clock.tick(60)
