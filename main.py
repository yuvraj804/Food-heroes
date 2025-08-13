

def main():
    import pygame
    from createp import Createp
    from buttonlogic import draw_button
    from sys import exit
    from rank import rank_heroes
    import os
    from csv_io import load_heroes_from_csv
    from play import playw
    from MYSTERY import Mystery
    from popup import show_popup
    pygame.init()
    w=768
    h=512

    display = pygame.display.set_mode((w, h))
    back = pygame.image.load(os.path.join('background', 'dc_logo_backgtround_for_a_game.jpeg'))
    play = pygame.image.load(os.path.join('buttons', 'play.png'))
    create = pygame.image.load(os.path.join('buttons', 'create.png'))
    rank = pygame.image.load(os.path.join('buttons', 'Powrank.png'))
    quit = pygame.image.load(os.path.join('buttons', 'quit.png'))
    mystery = pygame.image.load(os.path.join('buttons', 'mystery.png'))
    deletebutton = pygame.image.load(os.path.join('buttons', 'delete.png'))
    scaleplay = pygame.transform.scale(play, (217, 100))
    scalecreate = pygame.transform.scale(create, (217, 100))
    scalerank = pygame.transform.scale(rank, (217, 100))
    scalequit = pygame.transform.scale(quit, (217, 100))
    scalemystery = pygame.transform.scale(mystery, (217, 100))
    scaledelete = pygame.transform.scale(deletebutton, (217, 100))
    rectplay = scaleplay.get_rect(center=(100, 110))
    reccreate = scalecreate.get_rect(center=(100, 220))
    recrank = scalerank.get_rect(center=(100, 330))
    recquit = scalequit.get_rect(center=(100, 440))
    recmystery = scalemystery.get_rect(center=(100, 550))
    recdelete = scalecreate.get_rect(center=(100, 630))
    pygame.display.set_caption("Food Heroes")
    run = True
    clock = pygame.time.Clock()
    draw_button

    icon = pygame.image.load('icon/favicon.ico')
    scaleicon = pygame.transform.scale(icon, (64, 64))
    pygame.display.set_icon(scaleicon)
    open("fight_heroes.csv", "w").close()

    while run:

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONUP:

                if recrank.collidepoint(pygame.mouse.get_pos()):
                    load_heroes_from_csv()
                    rank_heroes()

                    run=False

                if recquit.collidepoint(pygame.mouse.get_pos()):
                    run=False

                if reccreate.collidepoint(pygame.mouse.get_pos()):
                    Createp()
                    run = False
                if rectplay.collidepoint(pygame.mouse.get_pos()):
                    playw()

                    run = False
                if recdelete.collidepoint(mouse_pos):
                    from deletehero import delete_hero
                    delete_hero(display, pygame.font.SysFont(None, 36), clock)

                from csv_io import load_heroes_from_csv, save_heroes_to_csv

                if recmystery.collidepoint(pygame.mouse.get_pos()):

                    load_heroes_from_csv()
                    mystery_hero = Mystery()
                    save_heroes_to_csv()
                    show_popup(display, f"{mystery_hero.name} Created!")

        display.blit(back, (0, 0))

        rectplay = draw_button(display, scaleplay, (100, 110), rectplay.collidepoint(mouse_pos))
        reccreate = draw_button(display, scalecreate, (100, 220), reccreate.collidepoint(mouse_pos))
        recrank = draw_button(display, scalerank, (100, 330), recrank.collidepoint(mouse_pos))
        recquit = draw_button(display, scalequit, (100, 440), recquit.collidepoint(mouse_pos))
        recmystery = draw_button(display, scalemystery, (668, 440), recmystery.collidepoint(mouse_pos))
        recdelete = draw_button(display, scaledelete, (668, 110), recdelete.collidepoint(mouse_pos))
        pygame.display.update()
        clock.tick(60)
main()