"""
Multiplayer Car Racing Game

This game allows two players to control their respective cars simultaneously in a multiplayer mode.

Modules:
    - pygame: Main library for developing games in Python.
    - random: Implements pseudo-random number generators.
    - car2: Module defining the Car class.

Functions:
    - car_racing_multiplayer: Main function that initializes the game and runs the game loop for multiplayer mode.

Usage:
    - Run the car_racing_multiplayer function to start the multiplayer game.
    - Player 1 controls: W (accelerate), A (move left), D (move right), S (decelerate).
    - Player 2 controls: UP (accelerate), LEFT (move left), RIGHT (move right), DOWN (decelerate).
    - Avoid collisions with traffic cars to prevent losing points.
    - Players can increase their levels by surviving longer in the game.


"""

import pygame
import random
from car2 import Car
import sys


def car_racing_multiplayer():
    pygame.init()

    GREEN = (20, 255, 140)
    GREY = (210, 210, 210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)
    BLACK = (0, 0, 0)
    shade_of_purple = (255, 0, 255)

    difficulty_level = 1

    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    imageList = ["YeRari.png", "BlackRari.png", "BlueRari.png", "McLauren.png"]

    SCREENWIDTH = 900
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Djogo di Carru")

    playerCar = Car("RedRari.png", 50, 75, 70)
    playerCar.rect.x = (SCREENWIDTH - playerCar.rect.width) / 2
    playerCar.rect.y = SCREENHEIGHT - 100

    playerCar2 = Car("maserati.png", 50, 75, 70)
    playerCar2.rect.x = (SCREENWIDTH - playerCar.rect.width) / 2
    playerCar2.rect.y = SCREENHEIGHT - 100

    car1 = Car("YeRari.png", 50, 75, random.randint(50, 100))
    car1.rect.x = 280
    car1.rect.y = -300

    car2 = Car("BlackRari.png", 50, 75, random.randint(50, 100))
    car2.rect.x = 380
    car2.rect.y = -600

    car3 = Car("BlueRari.png", 50, 75, random.randint(50, 100))
    car3.rect.x = 475
    car3.rect.y = -1200

    car4 = Car("McLauren.png", 50, 75, random.randint(50, 100))
    car4.rect.x = 575
    car4.rect.y = -900

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(playerCar)
    all_sprites_list.add(playerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    cooler_font = pygame.font.SysFont("Eight-Bit Madness", 50)
    blablue = (9, 24, 51)

    def show_game_over_screen_multiplayer(screen, score1, score2, level1, level2):

        from interface import interface

        gameoverback = pygame.image.load("gameoverback.png").convert()
        gameoverback = pygame.transform.scale(gameoverback, (SCREENWIDTH, SCREENHEIGHT))

        # Multiplayer game over screen
        screen.blit(gameoverback, (0, 0))

        text1 = cooler_font.render("Game Over", True, RED)
        text_rect = text1.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 200))
        screen.blit(text1, text_rect)

        text2 = cooler_font.render(f"Player 1 Score: {score1}", True, WHITE)
        text_rect = text2.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 150))
        screen.blit(text2, text_rect)

        text3 = cooler_font.render(f"Player 2 Score: {score2}", True, WHITE)
        text_rect = text3.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 100))
        screen.blit(text3, text_rect)

        level_text1 = cooler_font.render(f"Player 1 Level: {int(level1)}", True, RED)
        level_rect1 = level_text1.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 50))
        screen.blit(level_text1, level_rect1)

        level_text2 = cooler_font.render(f"Player 2 Level: {int(level2)}", True, RED)
        level_rect2 = level_text2.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))
        screen.blit(level_text2, level_rect2)

        # Create buttons
        button_back = pygame.Rect(SCREENWIDTH // 4, SCREENHEIGHT // 2 + 50, 200, 50)
        button_play_again = pygame.Rect(3 * SCREENWIDTH // 4 - 200, SCREENHEIGHT // 2 + 50, 200, 50)

        # Render button text
        back_text = cooler_font.render("Back", True, shade_of_purple)
        play_again_text = cooler_font.render("Restart", True, shade_of_purple)

        # Draw buttons on the screen
        pygame.draw.rect(screen, blablue, button_back)
        pygame.draw.rect(screen, blablue, button_play_again)

        # Draw button text on the screen
        screen.blit(back_text, button_back.move(10, 10).topleft)
        screen.blit(play_again_text, button_play_again.move(10, 10).topleft)

        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Check if the mouse click is inside the button areas
                    if button_back.collidepoint(mouse_pos):
                        interface()
                        waiting_for_input = False
                    elif button_play_again.collidepoint(mouse_pos):
                        car_racing_multiplayer()
                        waiting_for_input = False

            pygame.time.Clock().tick(30)

    # Load the images and sounds
    background_image = pygame.image.load("gameback.png").convert()
    level_up_sound = pygame.mixer.Sound("levelUp.mp3")
    game_over_sound = pygame.mixer.Sound("dun-dun.mp3")

    base_speed = 1
    traffic_car_speed = base_speed
    frame_counter = 0
    frames_to_increase_difficulty = 250
    level1 = 0
    level2 = 0

    carryOn = True
    clock = pygame.time.Clock()
    player1_score = 0
    player2_score = 0

    speed_player1 = 0
    speed_player2 = 0

    player1_lost = False
    player2_lost = False

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playerCar.moveRight(10)
                elif event.key == pygame.K_RIGHT:
                    playerCar2.moveRight(10)

        keys = pygame.key.get_pressed()

        # Player 1 controls
        if keys[pygame.K_a]:
            if playerCar.rect.x > 250:
                playerCar.moveLeft(5)
        if keys[pygame.K_d]:
            if playerCar.rect.x < 600:
                playerCar.moveRight(5)
        if keys[pygame.K_w]:
            speed_player1 += 0.03
            playerCar.moveBackward(speed_player1)
        if keys[pygame.K_s]:
            speed_player1 += 0.03
            playerCar.moveForward(speed_player1)

        # Player 2 controls
        if keys[pygame.K_LEFT]:
            if playerCar2.rect.x > 250:
                playerCar2.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            if playerCar2.rect.x < 600:
                playerCar2.moveRight(5)
        if keys[pygame.K_UP]:
            speed_player2 += 0.03
            playerCar2.moveBackward(speed_player2)
        if keys[pygame.K_DOWN]:
            speed_player2 += 0.03
            playerCar2.moveForward(speed_player2)

        # Increment level every 250 frames
        frame_counter += 1
        if frame_counter >= frames_to_increase_difficulty:
            frame_counter = 0

            # Increment level for Player 1 if not lost
            if not player1_lost:
                level1 += 1  # Increment Player 1's level
                level_up_sound.play()  # Play the level-up sound

            # Increment level for Player 2 if not lost
            if not player2_lost:
                level2 += 1  # Increment Player 2's level
                level_up_sound.play()  # Play the level-up sound

        # Update the speed based on the level
        traffic_car_speed = base_speed * (1 + 0.1 * level1 and level2)

        for car in all_coming_cars:
            car.moveForward(traffic_car_speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50, 100))
                print("Car reached the limit. Changing speed.")
                car.rect.y = -200
                if car == car1:
                    car.rect.x = 250
                elif car == car2:
                    car.rect.x = 350
                elif car == car3:
                    car.rect.x = 450
                elif car == car4:
                    car.rect.x = 550
                    car.load_car_image(random.choice(imageList))

        # Player 1 car collision
        car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
        for car in car_collision_list:
            print("Player 1 car crash!")
            game_over_sound.play()
            player1_lost = True

        # Player 2 car collision
        car_collision_list = pygame.sprite.spritecollide(playerCar2, all_coming_cars, False)
        for car in car_collision_list:
            print("Player 2 car crash!")
            game_over_sound.play()
            player2_lost = True

        if not player1_lost:
            player1_score += 1

        if not player2_lost:
            player2_score += 1

        if player1_lost and player2_lost:
            carryOn = False
            show_game_over_screen_multiplayer(screen, player1_score, player2_score, level1, level2)

        all_sprites_list.update()

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the road surface
        pygame.draw.rect(screen, BLACK, [250, 0, 400, SCREENHEIGHT])

        # Draw the center line
        pygame.draw.line(screen, WHITE, [450, 0], [450, SCREENHEIGHT], 5)

        # Draw the side lines
        pygame.draw.line(screen, WHITE, [250, 0], [250, SCREENHEIGHT], 5)
        pygame.draw.line(screen, shade_of_purple, [350, 0], [350, SCREENHEIGHT], 5)
        pygame.draw.line(screen, shade_of_purple, [550, 0], [550, SCREENHEIGHT], 5)
        pygame.draw.line(screen, WHITE, [650, 0], [650, SCREENHEIGHT], 5)

        # Display the score for Player 1
        text = cooler_font.render(f"Player 1 Score: {player1_score}", True, shade_of_purple)
        screen.blit(text, (10, 10))

        # Display the score for Player 2
        text = cooler_font.render(f"Player 2 Score: {player2_score}", True, shade_of_purple)
        screen.blit(text, (SCREENWIDTH // 2 + 10, 10))

        all_sprites_list.update()
        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
