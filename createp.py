def Createp():
    import pygame
    from buttonlogic import draw_button
    from main import main
    from inputbox import InputBox
    from superhero_class import superhero
    from csv_io import save_heroes_to_csv,load_heroes_from_csv
    from popup import show_popup
    load_heroes_from_csv()
    pygame.init()
    w, h = 768, 512
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Food Heroes")
    clock = pygame.time.Clock()


    back = pygame.image.load('background/dark_neon_blue_breathtaking_di.jpeg')
    img = pygame.image.load('Heroes/luxa.org-opacity-changed-_unknown-removebg-preview.png')
    Back = pygame.image.load('buttons/back.png')
    Enter = pygame.image.load('buttons/enter.png')


    background = pygame.transform.scale(back, (w, h))
    hero_img = pygame.transform.scale(img, (153, 305))
    rectimg = hero_img.get_rect(center=(650, 200))

    back_btn = pygame.transform.scale(Back, (180, 83))
    enter_btn = pygame.transform.scale(Enter, (180, 83))
    rectback = back_btn.get_rect(center=(450, 450))
    rectenter = enter_btn.get_rect(center=(650, 450))


    fields = [
        InputBox(150, 150, 200, 32, "Name"),
        InputBox(150, 200, 200, 32, "Strength"),
        InputBox(150, 250, 200, 32, "Dexterity"),
        InputBox(150, 300, 200, 32, "Intelligence"),
        InputBox(150, 350, 200, 32, "Tactic"),
        InputBox(150, 400, 200, 32, "Catchphrase"),
    ]
    current_field = 0
    fields[current_field].active = True

    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if rectback.collidepoint(event.pos):
                    main()
                    run = False
                    break


                if rectenter.collidepoint(event.pos):
                    i = 0


                    try:
                        name = fields[0].get_value()
                        i+=1
                        strength = int(fields[1].get_value())
                        i+=1
                        dexterity = int(fields[2].get_value())
                        i += 1
                        wisdom = int(fields[3].get_value())
                        i += 1
                        charisma = int(fields[4].get_value())
                        i += 1
                        catchphrase = fields[5].get_value()

                        new_hero = superhero(name, strength, dexterity, wisdom, charisma, catchphrase, location="unknown.jpeg")

                        save_heroes_to_csv()
                        fields[i].color_inactive=pygame.Color('green')

                        show_popup(screen, f"{new_hero.name} Created!")


                    except ValueError:
                         fields[i].color_inactive = pygame.Color("RED")
                         fields[i].text = "error"



            for i, field in enumerate(fields):
                response = field.handle_event(event)
                if response == 'next':
                    field.active = False
                    fields[(i + 1) % len(fields)].active = True
                    break


        screen.blit(background, (0, 0))
        screen.blit(hero_img, rectimg)

        for field in fields:
            field.draw(screen)

        rectback = draw_button(screen, back_btn, rectback.center, rectback.collidepoint(mouse_pos))
        rectenter = draw_button(screen, enter_btn, rectenter.center, rectenter.collidepoint(mouse_pos))

        pygame.display.update()
        clock.tick(60)
