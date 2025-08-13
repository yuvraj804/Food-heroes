from superhero_class import superhero
from core import create_default_heroes
from csv_io import load_heroes_from_csv

def rank_heroes():
    from buttonlogic import draw_button
    import pygame
    from main import main


    pygame.init()

    w, h = 768, 512
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Food Heroes")
    clock = pygame.time.Clock()

    back_img = pygame.image.load('background/neon_blue_background_breathtak.jpeg')
    back_btn_img = pygame.image.load('buttons/back.png')
    back_btn_scaled = pygame.transform.scale(back_btn_img, (217, 100))
    rectback = back_btn_scaled.get_rect(center=(660, 300))

    FONT = pygame.font.SysFont(None, 32)
    SMALL = pygame.font.SysFont(None, 24)
    TITLE =  pygame.font.Font("font/SuperShiny-0v0rG.ttf", 50)

    scroll_y = 0
    scroll_speed = 20

    superhero.instances.clear()

    load_heroes_from_csv()

    if not superhero.instances:
        print("[DEBUG] No heroes found in CSV, loading default heroes.")
        create_default_heroes()

    comb = superhero.instances.copy()
    comb.sort(key=lambda hero: hero.power, reverse=True)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_y = min(scroll_y + scroll_speed, 0)
                elif event.button == 5:
                    scroll_y -= scroll_speed
                elif rectback.collidepoint(pygame.mouse.get_pos()):
                    superhero.instances.clear()
                    main()
                    run = False

        screen.blit(back_img, (0, 0))



        title_surface = TITLE.render("POWER RANKING", True, (0, 0, 50))
        screen.blit(title_surface, (w // 1.7 , 10))


        y = 80 + scroll_y
        for i, hero in enumerate(comb, start=1):
            try:
                img = pygame.image.load(hero.location)
            except:
                img = pygame.image.load("Heroes/unknown.jpeg")  # Fallback

            img = pygame.transform.scale(img, (60, 60))
            screen.blit(img, (50, y))


            name_text = FONT.render(f"{i}. {hero.name}", True, (255, 255, 255))
            pow_text = FONT.render(f"Power: {hero.power}", True, (255, 255, 255))
            stat_text = SMALL.render(
                f"STR:{hero.strength} DEX:{hero.dexterity} INT:{hero.intelligence} TAC:{hero.tactic}",
                True, (230, 230, 230))


            block_width = 560
            block_height = 80
            block_x = 120
            block_y = y - 10


            if i == 1:
                border_color = "yellow"
            elif i == 2:
                border_color = "gray"
            elif i == 3:
                border_color = (139, 69, 19)
            else:
                border_color = (0, 0, 50)

            frame_rect = pygame.Rect(block_x - 4, block_y - 4, (block_width // 2) + 8, block_height + 8)
            pygame.draw.rect(screen, border_color, frame_rect, border_radius=14)

            pygame.draw.rect(screen, (0, 0, 50), (block_x, block_y, block_width // 2, block_height),
                             border_radius=12)

            screen.blit(name_text, (block_x + 10, y))
            screen.blit(pow_text, (block_x + 10, y + 25))
            screen.blit(stat_text, (block_x + 10, y + 50))

            y += 100

        mouse_pos = pygame.mouse.get_pos()
        rectback = draw_button(screen, back_btn_scaled, rectback.center, rectback.collidepoint(mouse_pos))

        pygame.display.update()
        clock.tick(60)
