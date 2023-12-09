"""
Car Racing Game - Main file

This game uses the Pygame library to create a simple car racing game. Players control a car using the arrow keys to avoid traffic cars and collect power-ups while advancing through levels.

Modules:
    - pygame: Main library for developing games in Python.
    - sys: Provides access to some variables used or maintained by the Python interpreter.
    - random: Implements pseudo-random number generators.
    - car2: Module defining the Car class and its subclasses.
    - powerup: Module defining power-up classes used in the game.

Functions:
    - car_racing: Main function that initializes the game and runs the game loop.

Classes:
    - PlayerCar: Represents the player's car, inheriting from the Car class.
    - TrafficCar: Represents traffic cars, inheriting from the Car class.

Attributes:
    - STARTING_X, STARTING_Y: Initial position for the player's car.
    - POWERUP_SPAWN_PROBABILITY: Probability of spawning a power-up.
    - SCREENWIDTH, SCREENHEIGHT: Dimensions of the game window.

Usage:
    - Run the car_racing function to start the game.
    - Use arrow keys for control (left, right, up, down).
    - Collect power-ups to gain advantages and increase your score.
    - Avoid collisions with traffic cars to prevent game over.


"""

import pygame
import sys
import random
from car2 import PlayerCar, TrafficCar, Car
from powerup import InvincibilityPowerUp, SlowingPowerUp, SizeChangePowerUp, ScoreDividerPowerUp


def car_racing():
    pygame.init()

    difficulty_level = 1  # Initial difficulty level
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    shade_of_purple = (255, 0, 255)
    blablue = (9, 24, 51)

    # Initialize Pygame mixer
    pygame.mixer.init()

    speed = 1
    imageList = ["YeRari.png", "BlackRari.png", "BlueRari.png", "McLauren.png"]

    SCREENWIDTH = 900
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)

    # Load the icon image
    pygame_icon = pygame.image.load("icon.png")
    pygame.display.set_icon(pygame_icon)

    pygame.display.set_caption("Let's go!")

    all_powerups_list = pygame.sprite.Group()
    visible_powerups_group = pygame.sprite.Group()

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    POWERUP_SPAWN_PROBABILITY = 1

    playerCar = PlayerCar("RedRari.png", 50, 75, 70)
    playerCar.rect.x = (SCREENWIDTH - playerCar.rect.width) / 2
    playerCar.rect.y = SCREENHEIGHT - 100

    car1 = TrafficCar("YeRari.png", 50, 75, random.randint(50, 100))
    car1.rect.x = 280
    car1.rect.y = -300

    car2 = TrafficCar("BlackRari.png", 50, 75, random.randint(50, 100))
    car2.rect.x = 380
    car2.rect.y = -600

    car3 = TrafficCar("BlueRari.png", 50, 75, random.randint(50, 100))
    car3.rect.x = 475
    car3.rect.y = -1200

    car4 = TrafficCar("McLauren.png", 50, 75, random.randint(50, 100))
    car4.rect.x = 575
    car4.rect.y = -900

    # Add the car to the list of objects
    all_sprites_list.add(playerCar)
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

    def spawn_powerup(all_powerups_list, road_width, road_height):
        if random.randint(1, 100) <= POWERUP_SPAWN_PROBABILITY:
            Powerup_classes = [
                InvincibilityPowerUp, SlowingPowerUp,
                SizeChangePowerUp, ScoreDividerPowerUp

            ]

            Powerup_class = random.choice(Powerup_classes)

            powerUp = Powerup_class()

            #  set the initial position
            powerUp.spawn_location(road_width, road_height)

            all_powerups_list.add(powerUp)

    def show_game_over_screen(screen, score):

        from interface import interface

        gameoverback = pygame.image.load("gameoverback.png").convert()
        gameoverback = pygame.transform.scale(gameoverback, (SCREENWIDTH, SCREENHEIGHT))

        screen.blit(gameoverback, (0, 0))



        text1 = cooler_font.render("Game Over", True, RED)
        text_rect = text1.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 200))
        screen.blit(text1, text_rect)

        text2 = cooler_font.render(f"Score: {score}", True, WHITE)
        text_rect = text2.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 150))
        screen.blit(text2, text_rect)

        lil_sass = cooler_font.render("Do better next time!", True, RED)
        lil_sass_rect = lil_sass.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 100))
        screen.blit(lil_sass, lil_sass_rect)

        # Display difficulty level
        final_level = cooler_font.render(f"Level: {int(1)}", True, RED)
        final_level_rect = final_level.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 200))
        screen.blit(final_level, final_level_rect)

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
                        car_racing()
                        waiting_for_input = False

            pygame.time.Clock().tick(30)

    # Load the images and sounds
    background_image = pygame.image.load("gameback.png").convert()
    level_up_sound = pygame.mixer.Sound("levelUp.mp3")
    game_over_sound = pygame.mixer.Sound("dun-dun.mp3")

    base_speed = 1
    traffic_car_speed = base_speed
    frame_counter = 0
    frames_to_increase_difficulty = 400
    level = 0
    is_powerup_collided = False

    # Allowing the user to close the window...

    carryOn = True
    clock = pygame.time.Clock()
    playerCar.score = 0

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playerCar.moveRight(10)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if playerCar.rect.x > 250:
                playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            if playerCar.rect.x < 600:
                playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            speed += 0.03
            playerCar.moveBackward(speed)
        if keys[pygame.K_DOWN]:
            if playerCar.rect.x > 500:
                speed += 0.03
                playerCar.moveForward(speed)

        spawn_powerup(all_powerups_list, 400, 400)

        for powerup in all_powerups_list:
            powerup.moveForward(speed)
            if powerup.rect.y > SCREENHEIGHT:
                powerup.kill()

            if pygame.sprite.collide_rect(powerup, playerCar):
                powerup.affect_player(playerCar)
                powerup.kill()

        powerup_classes = [
            InvincibilityPowerUp, SlowingPowerUp,
            SizeChangePowerUp, ScoreDividerPowerUp

        ]
        powerup_class = random.choice(powerup_classes)
        powerup = powerup_class()

        # Check for power-up collisions
        powerup_collision_list = pygame.sprite.spritecollide(playerCar, all_powerups_list, True)
        for powerup in powerup_collision_list:
            powerup.affect_player(playerCar)

        playerCar.update()

        # Check if the player car is currently under the invincibility effect
        if playerCar.invincible:
            # Check if the invincibility duration has expired
            current_time = pygame.time.get_ticks()
            if current_time >= playerCar.invincibility_start_time + playerCar.effect_duration:
                # Reset power-up attributes after the invincibility duration
                playerCar.reset_powerup()
            else:
                # Change the playerCar image when invincible
                playerCar.image = pygame.image.load("invincible_car.png").convert_alpha()
                playerCar.image = pygame.transform.scale(playerCar.image, (playerCar.width + 30, playerCar.height + 30))


        else:
            # Player car is not invincible, handle collisions with traffic cars
            car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
            for car in car_collision_list:

                playerCar.apply_original_image()
                game_over_sound.play()  # Play the game_over sound
                show_game_over_screen(screen, playerCar.score)
                # End Of Game
                carryOn = False

        # Increment level every 400 frames
        frame_counter += 1
        if frame_counter >= frames_to_increase_difficulty:
            frame_counter = 0
            level += 1  # Increment level
            level_up_sound.play()  # Play the level-up sound

        # Update the speed based on the level
        traffic_car_speed = base_speed * (1.5 + 0.2 * level)

        # Game Logic
        for car in all_coming_cars:
            car.moveForward(traffic_car_speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50, 100))
                # print("Car reached the limit. Changing speed.")
                car.rect.y = -200
                if car == car1:
                    car.rect.x = 250  # Reset car1 to the leftmost lane
                elif car == car2:
                    car.rect.x = 350  # Reset car2 to the middle lane
                elif car == car3:
                    car.rect.x = 450  # Reset car3 to the right lane
                elif car == car4:
                    car.rect.x = 550  # Reset car4 to the rightmost lane
                    car.load_car_image(random.choice(imageList))  # Randomize the car image

        # Handle power-up spawning
        spawn_powerup(all_powerups_list, 400, 600)

        # Spawn a random power-up
        powerup_classes = [
            InvincibilityPowerUp, SlowingPowerUp,
            SizeChangePowerUp, ScoreDividerPowerUp

        ]
        powerup_class = random.choice(powerup_classes)
        powerup = powerup_class()

        # Check for collisions between the spawned power-up and traffic cars
        powerup_collision_list = pygame.sprite.spritecollide(powerup, all_coming_cars, False)
        if len(powerup_collision_list) > 0:
            is_powerup_collided = True

        # Handle power-up collisions with traffic cars
        if is_powerup_collided:
            for car in powerup_collision_list:
                if not car.is_traffic_car:  # Check if the collided car is a traffic car
                    powerup.affect_traffic(car)  # If it's not, affect the car as before
            is_powerup_collided = False
        else:
            powerup.kill()

        playerCar.score += 1
        all_sprites_list.update()
        all_powerups_list.update()

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

        # Display the score
        text = cooler_font.render(f"Score: {playerCar.score}", True, shade_of_purple)
        screen.blit(text, (10, 10))

        # Display difficulty level
        level_text = cooler_font.render(f"Level: {int(level)}", True, shade_of_purple)
        screen.blit(level_text, (10, 40))

        # Draw and update visible power-ups
        visible_powerups = [powerup for powerup in all_powerups_list if 0 < powerup.rect.y < SCREENHEIGHT]
        visible_powerups_group.empty()
        visible_powerups_group.add(visible_powerups)
        visible_powerups_group.update()
        visible_powerups_group.draw(screen)

        # Draw all the sprites in one go.
        all_sprites_list.draw(screen)

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second
        clock.tick(60)

    pygame.quit()
