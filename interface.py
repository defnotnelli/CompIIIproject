import pygame
import sys
from game import car_racing


# Creating a function that creates the GUI
def interface():
    # initiating pygames
    pygame.init()
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)

    # Load the background image
    background_image = pygame.image.load("interface.png").convert()

    pygame.display.set_caption("Djogo di Carru")

    # creating some colors (RGB scale)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)
    shade_of_purple = (255, 0, 255)
    cyberpunk_blue = (99, 0, 255)
    blablue = (9, 24, 51)

    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    cooler_font = pygame.font.SysFont("Eight-Bit Madness", 50)
    game1_text = cooler_font.render('Get Started', True, shade_of_purple)
    game2_text = cooler_font.render('Multiplayer', True, shade_of_purple)
    game3_text = cooler_font.render('Instructions', True, shade_of_purple)
    credits_text = cooler_font.render('Credits', True, shade_of_purple)
    quit_text = cooler_font.render(' Quit :(', True, shade_of_purple)
    title_text = cooler_font.render('Best Racing Game Available ! ', True, yellow)

    screen_width = 720
    screen_height = 720
    # Calculate the positions for the interface elements
    button_width = 200
    button_height = 60
    button_margin = 20
    button_x = (screen_width - button_width) // 2
    game1_pos = (button_x, (screen_height - (4 * button_height + 3 * button_margin)) // 2)
    game2_pos = (button_x, game1_pos[1] + button_height + button_margin)
    game3_pos = (button_x, game2_pos[1] + button_height + button_margin)
    credits_pos = (button_x, game3_pos[1] + button_height + button_margin)
    quit_pos = (button_x, credits_pos[1] + button_height + button_margin)

    # interface loop
    while True:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                # Get Started Button
                if game1_pos[0] <= mouse[0] <= game1_pos[0] + button_width and game1_pos[1] <= mouse[1] <= game1_pos[
                    1] + button_height:
                    car_racing()

                # Multiplayer Button
                # elif game2_pos[0] <= mouse[0] <= game2_pos[0] + button_width and game2_pos[1] <= mouse[1] <= game2_pos[1] + button_height:
                #     multiplayer_function()

                # Instructions Button
                elif game3_pos[0] <= mouse[0] <= game3_pos[0] + button_width and game3_pos[1] <= mouse[1] <= game3_pos[
                    1] + button_height:
                    instructions()

                # Credits Button
                elif credits_pos[0] <= mouse[0] <= credits_pos[0] + button_width and credits_pos[1] <= mouse[1] <= \
                        credits_pos[1] + button_height:
                    credits_()

                # Quit Button
                elif quit_pos[0] <= mouse[0] <= quit_pos[0] + button_width and quit_pos[1] <= mouse[1] <= quit_pos[
                    1] + button_height:
                    pygame.quit()

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # print the buttons text and the box(color changing)
        # game 1 text
        mouse = pygame.mouse.get_pos()

        # when the mouse is on the box it changes color
        # Blit text "Get Started"  on the screen
        if game1_pos[0] <= mouse[0] <= game1_pos[0] + button_width and game1_pos[1] <= mouse[1] <= game1_pos[
            1] + button_height:
            pygame.draw.rect(screen, cyberpunk_blue, [game1_pos[0], game1_pos[1], button_width, button_height])
        else:
            pygame.draw.rect(screen, blablue, [game1_pos[0], game1_pos[1], button_width, button_height])

        screen.blit(game1_text, game1_pos)

        # SAME FOR ALL THE OTHER BUTTONS

        # "Multiplayer"  text
        if game2_pos[0] <= mouse[0] <= game2_pos[0] + button_width and game2_pos[1] <= mouse[1] <= game2_pos[
            1] + button_height:
            pygame.draw.rect(screen, cyberpunk_blue, [game2_pos[0], game2_pos[1], button_width, button_height])
        else:
            pygame.draw.rect(screen, blablue, [game2_pos[0], game2_pos[1], button_width, button_height])

        screen.blit(game2_text, game2_pos)

        # Instructions text
        if game3_pos[0] <= mouse[0] <= game3_pos[0] + button_width and game3_pos[1] <= mouse[1] <= game3_pos[
            1] + button_height:
            pygame.draw.rect(screen, cyberpunk_blue, [game3_pos[0], game3_pos[1], button_width, button_height])
        else:
            pygame.draw.rect(screen, blablue, [game3_pos[0], game3_pos[1], button_width, button_height])

        # Blit text on the screen
        screen.blit(game3_text, game3_pos)

        # credits text

        if credits_pos[0] <= mouse[0] <= credits_pos[0] + button_width and credits_pos[1] <= mouse[1] <= credits_pos[
            1] + button_height:
            pygame.draw.rect(screen, cyberpunk_blue, [credits_pos[0], credits_pos[1], button_width, button_height])
        else:
            pygame.draw.rect(screen, blablue, [credits_pos[0], credits_pos[1], button_width, button_height])

        # Blit text on the screen
        screen.blit(credits_text, credits_pos)

        # Quit text
        if quit_pos[0] <= mouse[0] <= quit_pos[0] + button_width and quit_pos[1] <= mouse[1] <= quit_pos[
            1] + button_height:
            pygame.draw.rect(screen, red, [quit_pos[0], quit_pos[1], button_width, button_height])
        else:
            pygame.draw.rect(screen, blablue, [quit_pos[0], quit_pos[1], button_width, button_height])

        # Blit text on the screen
        screen.blit(quit_text, quit_pos)

        # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
        # screen.blit(title_text, (55, 0))
        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.update()


def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    # Load the background image
    background3_image = pygame.image.load("credits.png").convert()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    color_dark = (100, 100, 100)
    shade_of_purple = (255, 0, 255)
    cyberpunk_blue = (99, 0, 255)
    width = screen.get_width()
    height = screen.get_height()
    cooler_font = pygame.font.SysFont("Eight-Bit Madness", 50)
    back_text = cooler_font.render('Back', True, shade_of_purple)

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
                    interface()
        screen.fill((0, 0, 0))

        # Draw the background image
        screen.blit(background3_image, (0, 0))

        # back text
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, cyberpunk_blue, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(back_text, (450, 5 * 120))

        pygame.display.update()


def instructions():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    # Load the background image
    background2_image = pygame.image.load("instructions.png").convert()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    color_dark = (100, 100, 100)
    shade_of_purple = (255, 0, 255)
    cyberpunk_blue = (99, 0, 255)
    width = screen.get_width()
    height = screen.get_height()
    cooler_font = pygame.font.SysFont("Eight-Bit Madness", 50)
    back_text = cooler_font.render('Back', True, shade_of_purple)


    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
                    interface()
        screen.fill((0, 0, 0))

        # Draw the background image
        screen.blit(background2_image, (0, 0))

        # back text
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, cyberpunk_blue, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(back_text, (450, 5 * 120))


        pygame.display.update()


if __name__ == "__main__":
    interface()










