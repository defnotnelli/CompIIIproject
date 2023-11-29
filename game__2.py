import pygame, random
# Let's import the Car Class
from car import Car
from powerup import InvincibilityPowerUp, SlowingPowerUp, SpeedBoostPowerUp, SizeChangePowerUp, TimeFreezePowerUp, \
    ScoreMultiplierPowerUp, RandomLaneChangePowerUp


def car_racing():
    pygame.init()

    difficulty_level = 1  # Initial difficulty level

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

    speed = 1
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    imageList = ["YeRari.png", "BlackRari.png", "BlueRari.png", "McLauren.png"]

    SCREENWIDTH = 900
    SCREENHEIGHT = 600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Djogo di Carru")

    all_powerups_list = pygame.sprite.Group()
    visible_powerups_group = pygame.sprite.Group()
    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    POWERUP_SPAWN_PROBABILITY = 3

    playerCar = Car("RedRari.png", 50, 75, 70)
    playerCar.rect.x = (SCREENWIDTH - playerCar.rect.width) / 2
    playerCar.rect.y = SCREENHEIGHT - 100

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

    def spawn_powerup(all_powerups_list):
        if random.randint(1, 100) <= POWERUP_SPAWN_PROBABILITY:
            powerup = random.choice([
                InvincibilityPowerUp(), SlowingPowerUp(), SpeedBoostPowerUp(),
                SizeChangePowerUp(), TimeFreezePowerUp(), ScoreMultiplierPowerUp(),
                RandomLaneChangePowerUp()
            ])
            powerup.rect.x = random.randrange(SCREENWIDTH - powerup.rect.width)
            powerup.rect.y = -300
            print(f"Spawned power-up: {type(powerup).__name__} at ({powerup.rect.x}, {powerup.rect.y})")
            all_powerups_list.add(powerup)

    def show_game_over_screen(screen, score):
        # screen
        screen.fill(BLACK)

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
        final_level = cooler_font.render(f"Level: {int(level)}", True, RED)
        final_level_rect = final_level.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 200))
        screen.blit(final_level, final_level_rect)

        pygame.display.flip()
        pygame.time.wait(1000)  # Display the game-over screen for  seconds

    # Load the images and sounds
    background_image = pygame.image.load("gameback.png").convert()
    level_up_sound = pygame.mixer.Sound("levelUp.mp3")
    game_over_sound = pygame.mixer.Sound("dun-dun.mp3")



    base_speed = 1  # Set your desired base speed
    traffic_car_speed = base_speed
    frame_counter = 0
    frames_to_increase_difficulty = 250
    level = 0

    # Allowing the user to close the window...
    carryOn = True
    clock = pygame.time.Clock()
    score = 0

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
            speed += 0.03
            playerCar.moveForward(speed)

        spawn_powerup(all_powerups_list)

        for powerup in all_powerups_list:
            powerup.moveForward(speed)
            if powerup.rect.y > SCREENHEIGHT:
                powerup.kill()

            if pygame.sprite.collide_rect(powerup, playerCar):
                powerup.affect_player(playerCar)
                powerup.kill()

            powerup_collision_list = pygame.sprite.spritecollide(powerup, all_coming_cars, False)
            for car in powerup_collision_list:
                powerup.affect_traffic(car)
                powerup.kill()

        # Increment level every 250 frames
        frame_counter += 1
        if frame_counter >= frames_to_increase_difficulty:
            frame_counter = 0
            level += 1  # Increment level
            level_up_sound.play()  # Play the level-up sound

        # Update the speed based on the level
        traffic_car_speed = base_speed * (1 + 0.2 * level)

        # Game Logic
        for car in all_coming_cars:
            car.moveForward(traffic_car_speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50, 100))
                print("Car reached the limit. Changing speed.")
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



        for car in all_coming_cars:
            if car.rect.y > SCREENHEIGHT:
                print("Changing car image")
                car.load_car_image(random.choice(imageList))

            # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
            for car in car_collision_list:
                print("Car crash with player!")
                game_over_sound.play()  # Play the game_over sound
                show_game_over_screen(screen, score)
                # End Of Game
                carryOn = False

        score += 1


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
        text = cooler_font.render(f"Score: {score}", True, shade_of_purple)
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

        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    car_racing()