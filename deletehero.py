
def delete_hero(display, font, clock):
    from popup import show_popup
    import pygame
    from superhero_class import superhero
    from csv_io import save_heroes_to_csv,load_heroes_from_csv

    input_text = ''
    active = True

    input_box = pygame.Rect(150, 200, 400, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active
    load_heroes_from_csv()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name_to_delete = input_text.strip().lower()
                    found = False
                    for hero in superhero.instances:
                        if hero.name.strip().lower() == name_to_delete:
                            superhero.instances.remove(hero)
                            save_heroes_to_csv()
                            show_popup(display, f"{hero.name} deleted!")
                            found = True
                            break
                    if not found:
                        show_popup(display, f"{input_text} not found!")
                    return
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        display.fill((0, 0, 30))
        txt_surface = font.render(input_text, True, (255, 255, 255))
        pygame.draw.rect(display, color, input_box, 2)
        display.blit(txt_surface, (input_box.x+5, input_box.y+5))

        prompt = font.render("Enter name to delete:", True, (255, 255, 255))
        display.blit(prompt, (input_box.x, input_box.y - 40))

        pygame.display.flip()
        clock.tick(30)
